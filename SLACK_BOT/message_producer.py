import re
import os
import random
from bot import Bot
from database import Database
from Type.message import Message
from datetime import datetime, timedelta

# Create Connection To Data Base
db = Database('localhost', 'root', 'Game1234monkey', 'slackusers')

# refresh the database
db.refresh_occupied()

# Create Connection To Bot
slack_token = os.environ["SLACK_BOT_TOKEN"]
bot = Bot(slack_token)



#This Object recives message and assorts them to different classes
class MessageProducer:
    def __init__(self, channel: str, user_id: str, attachments : dict):

        self.user_id = user_id
        self.username = bot.get_username(user_id)
        self.bot_username = "<@" +  str(bot.get_ID()) + ">"

        self.channel = channel
        self.channel_type = self.get_channel_type()

        self.thread_ts = attachments["thread_ts"]
        self.in_thread = attachments["in_thread"]
        self.item_user = attachments["item_user"]
        
        self.input_list =  ( # RegEx  for possible input options
            (r"((?P<botname>[@<>0-9A-Z]+)\s+)?(?P<input>(?:create|insert|add)\s(?P<item>[a-z]+)(?:.+)(?:database))", self.insert),
            (r"((?P<botname>[@<>0-9A-Z]+)\s+)?(?P<input>(?:release)\s(?P<item>[a-z]+)(?:.+)(?:database))", self.release),    
            (r"((?P<botname>[@<>0-9A-Z]+)\s+)?(?P<input>(?:take|give me)\s(?P<item>[a-z]+)(?:.+)(?:database\s)[a-zA-z\s]*(?P<time>(?:[0-9]*))(?:\s*)(?P<type>(?:(min|minutes|hour|hours|day|days))))", self.take),    
            (r"((?P<botname>[@<>0-9A-Z]+)\s+)?(?P<input>[!^_a-zA-Z\s@]+)", self.message),
            (r"((?P<botname>[@<>0-9a-zA-Z]+)\s+)?(?P<input>[:^_a-z ]+)", self.reaction_added) 
        )
    
    # Getters and Setters
    def get_user_id(self): 
        return self.user_id

    def get_channel(self):
        return self.channel

    def get_channel_type(self):
        if self.channel[0] == 'D':
            return 'dm'    
        elif self.channel[0] == 'C':
            return "channel"
   
    def get_attachments(self):
        return {
            "thread_ts" : self.thread_ts,
            "in_thread" : self.in_thread,
            "item_user" : self.item_user,
        }
    
    def set_user_id(self, user_id):
        self.user_id = user_id
    
    def set_channel(self, channel):
        self.channel = channel

    def set_channel_type(self, channel_type):
        if channel_type == 'dm' or 'channel': 
            self.channel_type = channel_type
            return True
        return False

    def set_attachments(self, attachments):
        self.thread_ts = attachments["thread_ts"]
        self.in_thread = attachments["in_thread"]
        self.item_user = attachments["item_user"]
    
    # Assorts the type of response message
    def find_message_type(self, input: str):
        # Loop through the input list
        for regex, self.func in self.input_list:
            # Find a Match using the regex func
            match = re.match(regex, input)
            if match and input:
                # Group the mathces to a Dict
                payload = match.groupdict()
                print(payload)
                return self.func(**payload)

    def handle_response(self, input):   ## If ^ -> Must Include. If # -> Mabye Include
        options = []
        if isincluded(input, "#hello#hi#hey#howdy#Hello#Hey#Hi#Howdy"):
            options = ["Hello how are you?", "Hey There, Whats up?", "Yooo, How are you doing today" ]
            return Message(self.channel, random.choice(options))
        if isincluded(input, "^i am#i am#good#great#amazing#fine#ok#okay"):
            return Message(self.channel, "Thats awsome! i hope you will have a good day")
        if input == "!help":
            return Message(self.channel,
                "add to database: 'insert/create/add <item_name> ... database\n" +
                "take an item: 'take\\/give me <item_name>\n ... database for [number] minutes/hours/days" +
                "remove an item 'remove/erase/delete <item_name> from database\n")
        return Message(self.channel, "I can't understand you. type '!help'")
       ### TO RETURN A LIST OF MESSAGE USE THE FOLLOWING SYNTAX
       #return [Message(self.channel, ":hushed:"), Message(self.channel, "I Like This Emoji")]


    def insert(self, **payload): 
        db.insert(payload['item'], "", "", "")
        return Message(self.channel, "Record inserted successfully into database")

    def release(self, **payload):
        product = db.get_data_by_name(payload['item'])
        if product['occupied_by'] == self.username:
            db.update(payload['item'], "", "", "")
        print("record released")

    def take(self, **payload):
        print("reached")
        if db.is_occupied_by_name(payload['item']):
            print("passed")
            return [
                Message(self.channel, "This Item is currently used"),
                Message(self.channel, "it will be released in " + str(db.delta_release_by_name(payload['item'])))
            ]
        else:
            input = payload['type']
            current_time = datetime.now()
            if isincluded(input, "#min#minutes"):
                release_time = current_time + timedelta(minutes= int(payload['time']))
            elif isincluded(input, "#hour#hours"):
                release_time = current_time + timedelta(hours= int(payload['time']))
            elif isincluded(input, "#day#days"):
                release_time = current_time + timedelta(days= int(payload['time']))
            else:
                return Message(self.channel, "I dont know what" + payload['type] + "means'])

            db.update(payload['item'], self.username, current_time, release_time)
            return Message(self.channel, f"You Successfully Took the {payload['item']} for {payload['time']} {payload['type']}")
   
   #Generic Message Constructor
    def message(self, **payload):
        if self.channel_type == "dm":
            if self.bot_username not in payload['input']:
                return self.handle_response(payload['input'])
            else:
                return Message(self.channel, "You Dont Need To @ me in a private conversation")
        elif self.channel_type == "channel":
            if payload["botname"] == self.bot_username: 
                return self.handle_response(payload['input'])
     

    def reaction_added(self, **payload):
        print("passed")
        if self.channel_type == "dm":
            return Message(self.channel, ":smile:")

        elif self.channel_type == "channel":       
            if self.item_user == None: #This means that the reaction was on a Bot Message 
                return [Message(self.channel, ":hushed:"), Message(self.channel, "I Like This Emoji")]




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




