import re
import random
from Type.message import Message

"""
To find your bot's id, you need to send a message where you mention him and then print the payload text.
you will see that slack automatically swaps the botname to a combination of letters.
"""
bot_id = "<@UKW4RAK1P>" 

#This Object recives message an assorts them to different classes
class MessageProducer:
    def __init__(self, channel, thread: tuple):
        self.channel = channel
        self.channel_type = ''
        self.ts = thread[0], #timestamp
        self.thread_ts = thread[1], #thread timestamp
        self.reply_users_count = thread[2] # how many users in thread
        self.in_thread = False
        self.input_list =  ( # RegEx Options for possible input options
            ("^(?P<input>[a-zA-Z-@ ]+)$", self.message),
            ("^(?P<botname>[@<>0-9a-zA-Z]+)(?P<input>[a-zA-Z ]+)$", self.app_mention),
        )
        if self.ts == self.thread_ts:
            self.in_thread = True

        if self.channel[0] == 'D':
            self.channel_type = 'dm'
            
        if self.channel[0] == 'C':
            self.channel_type = "channel"
        print(self.in_thread)
        print(self.reply_users_count)

    # Assorts the type of response message
    def get_message_type(self, input: str):
        for regex, self.func in self.input_list:
            match = re.match(regex, input)
            if match and input:
                payload = match.groupdict()
                print(payload)
                return self.func(**payload)
    
    def handle_response(self, input):
        options = []
        if isincluded(input, "#hello#hi#hey#howdy#Hello#Hey#Hi#Howdy"):
            options = ["Hello how are you?", "Hey There, Whats up?", "Yooo, How are you doing today" ]
            return Message(self.channel, random.choice(options))
        if isincluded(input, "^i am#i am#good#great#amazing#fine#ok#okay"):
            return Message(self.channel, "Thats awsome! i hope you will have a good day")
        if input == "what are you":
            return Message(self.channel, "i am a bot")

   #Generic Message Constructor
    def message(self, **payload):
        print("message")
        if self.channel_type == "dm":
            return self.handle_response(payload['input'])

        
    #@ Message Constructor
    def app_mention(self, **payload):
        print("app_mention")
        if self.channel_type == "channel":
            if self.reply_users_count <= 2:
                return Message(self.channel, "Only the two of us are in this thread, please dont @ me")
            #Check if user @ the right bot
            if payload["botname"] == bot_id: ##need to write get bot id 
                return self.handle_response(payload['input'])
     
        if self.channel_type == 'dm':  
            # in a thread with other people  
            if self.in_thread and self.reply_users_count > 2:
                return self.handle_response(payload['input'])

            elif self.reply_users_count <= 2:
                return Message(self.channel, "Only the two of us are in this thread, please dont @ me")
            #regular message(not in thread)
            return Message(self.channel, "This is a private conversation, you dont need to @ me")


  




#recives an array of possible inputs and required inputs and create a response acording to the inputs
def isincluded(input, txt):
    # Variable decleration
    must_include = []
    included = []
    has_keyword = False
    has_required_keyword = True

    # Split keywords dtring into array
    keywords = txt.split("#")
    # Loop through Keyword array
    for i in range(len(keywords)):
        if keywords[i] in input and keywords[i] is not '': 
            has_keyword = True
            included.append(keywords[i])

        if '^' in keywords[i]: # if input contains required keyword
            has_required_keyword = False #means there is a required keyword
            must_include.append(keywords[i]) 

    #check if must_icluded keyword appears in included
    for i in range(len(must_include)):
        for j in range(len(included)):
            if included[j] in must_include[i]:
                has_required_keyword = True

    if has_required_keyword and has_keyword:
        return True
    return False



