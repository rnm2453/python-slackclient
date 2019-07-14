import re
import random
from Type.message import Message

#This Object recives message an assorts them to different classes
class MessageProducer:
    def __init__(self, channel):
        self.channel = channel
        self.input_list =  ( # RegEx Options for possible input options
            ("(?P<input>[a-zA-Z ]+)", self.message),
            ("^(?P<botname>[@<>0-9a-zA-Z]+)(?P<input>[a-zA-Z ]+)", self.app_mention),
        )

        if self.channel[0] == 'D':
            self.channel_type = 'dm'
            
        if self.channel[0] == 'C':
            self.channel_type = "channel"

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
        print("mes")
        if self.channel_type == "dm":
            return self.handle_response(payload['input'])

        
    #@ Message Constructor
    def app_mention(self, **payload):
        print(",en")
        if self.channel_type == "channel":
            #Check if user @ the right bot
            if payload["botname"] == "<@UKW4RAK1P>": ##need to write get bot id 
                return self.handle_response(payload['input'])
        if self.channel_type == 'dm':    
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




#@ Message Constructor
def app_mention(channel, channel_type, **payload):
    if channel_type == "channel":
        #Check if user @ the right bot
        if payload["botname"] == "<@UKW4RAK1P>": ##need to write get bot id 
            return handle_message(payload["input"], channel)

    if channel_type == 'dm':    
        return Message(channel, "This is a private conversation, you dont need to @ me")
