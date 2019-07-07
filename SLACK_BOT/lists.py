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

