<<<<<<< HEAD
from datetime import datetime
from Type.message import Message
import re

def func(channel, **payload):
    if payload['input'] == "hey":
        return Message(channel, "Hello how are you?")
    if payload['input'] == "bye":
        return Message(channel, "goodbye")
    if payload['input'] == "what are you":
        return Message(channel, "i am a bot")
"""
messageList = [
    {
        "hey" : [
            "Hey There!",
            "S'up",
        ],
    },
]
"""

messageList = {
    "(?P<input>[a-zA-Z]+)" : func,
}

=======
from datetime import datetime
messageList = {
    "hello" : "Hey There!",
    "hey" : "Hey There!",
    "tell me a joke" : "Today, my Robo-son asked: \"Can i have a book Mark?\" And i burst into tears.\n\n\n\'11' years old and he still doesnt know my name is pythonbot",
    "what are you" : "I am a Bot",
    "what is the time" : str(datetime.now().strftime("%H:%M"))
}



>>>>>>> 4ade514413be5d69bc7cd0abeb4ee7d6d18ecc6d
