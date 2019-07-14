import random
import re
from datetime import datetime
from lists import messageList 
from Type.onboarding import Onboarding
from Type.message import Message

#This Object recives message an assorts them to different classes
class MessageProducer:
    def __init__(self, channel):
        self.channel = channel

        if self.channel[0] == 'D':
            self.channel_type = 'dm'
            
        if self.channel[0] == 'C':
            self.channel_type = "channel"

    # Assorts the type of response message
    def get_message_type(self, input: str):

        if self.channel_type == 'channel':
            # onboarding type
            if input and input.lower() == '@pythonbot show onboarding message':
                return Onboarding(self.channel)
        
        
        if self.channel_type == 'dm':

            if input and input.lower() == 'show onboarding message':
                return Onboarding(self.channel)
            
        # generic message type
        for regex, func in messageList:
            match = re.match(regex, input)
            if match and input:
                payload = match.groupdict()
                print(payload)
                return func(self.channel, self.channel_type, **payload)
            

"""
        for i in range(len(messageList)):
            for var in messageList[i]:
                if input and input.lower() in var:
                    return Message(self.channel, random.choice(messageList[i][var]))
"""


    