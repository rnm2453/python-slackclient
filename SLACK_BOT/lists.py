from datetime import datetime
from Type.message import Message
import random
import re

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
        print(True)
        return True
    print(False)
    return False

def func(channel, channel_type, **payload):
    handler = False
    print(channel)
    print(channel_type)
    print(payload)

    if channel_type == 'channel':
        if '<@UKW4RAK1P>' or '<@UKW4RAK1P>'.lower() in payload['input']:
            print(":passes")
            handler = True
        else:
            print("not passes")
    else:
        handler = True
    
    if handler == True:
        options = []
        if isincluded(payload['input'], "#hello#hi#hey#howdy#Hello#Hey#Hi#Howdy"):
            options = ["Hello how are you?", "Hey There, Whats up?", "Yooo, How are you doing today" ]
            return Message(channel, random.choice(options))
        if isincluded(payload['input'], "^i am#i am#good#great#amazing#fine#ok#okay"):
            return Message(channel, "Thats awsome! i hope you will have a good day")
        if payload['input'] == "what are you":
            return Message(channel, "i am a bot")

def handle_channel(channel, **payload):
    channel_correct = True
    print(payload['input'])
    options = []
    if channel == 'channel':
        if '@' and 'pythonbot' in payload['input']:
            print("token in")
            channel_correct = True
        else:
            channel_correct = False

    if channel_correct == True:   
        if isincluded(payload['input'], "#hello#hi#hey#howdy#Hello#Hey#Hi#Howdy"):
            options = ["Hello how are you?", "Hey There, Whats up?", "Yooo, How are you doing today" ] 
            return Message(channel, random.choice(options))



messageList = (
    ("(?P<input>[a-zA-Z-@ ]+)", func),
    #("(?P<botname>[a-zA-Z-@]+)(?P<input>[a-zA-Z ]+)", func),

)





