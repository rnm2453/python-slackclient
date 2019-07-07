from datetime import datetime
import random
import re
from lists import messageList 
from Type.onboarding import Onboarding
from Type.message import Message

#This Object recives message an assorts them to different classes
class MessageProducer:
    def __init__(self, channel):
        self.channel = channel

    # Assorts the type of response message
    def get_message_type(self, input:str):

        # onboarding type
        if input and input.lower() == 'show onboarding message':
            return Onboarding(self.channel)
        
        # generic message type
        for regex, func in messageList.items():
            match = re.match(regex, input)
            if match and input:
                payload = match.groupdict()
                return func(self.channel, **payload)

"""
        for i in range(len(messageList)):
            for var in messageList[i]:
                if input and input.lower() in var:
                    return Message(self.channel, random.choice(messageList[i][var]))
"""


    