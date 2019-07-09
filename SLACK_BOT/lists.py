from datetime import datetime
from Type.message import Message
import random
import re

def func(channel, **payload):
    options = []
    if payload['input'] in "hey hello howdy hi":
        options = ["Hello how are you?", "Hey There, Whats up?", "Yooo, How are you doing today" ]
        return Message(channel, random.choice(options))
    if payload['input'] in "good fine great amazing":
        return Message(channel, "Thats amazing!")
    if payload['input'] == "what are you":
        return Message(channel, "i am a bot")

messageList = {
    "(?P<input>[a-zA-Z]+)" : func,
}


