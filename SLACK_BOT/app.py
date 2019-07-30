#!C:/Users/Roey Lifshitz/AppData/Local/Programs/Python/Python37/python.exe
""" My Python Path """

print("Content-Type: text/html")
print()
print ("""
    <TITLE>CGI script ! Python</TITLE>
    <H1>This is my first CGI script</H1>
    Hello, world!
"""
)

import os
import slack
import certifi
import datetime
import ssl as ssl_lib
from producer import Producer, bot

print(os.environ)

def process_message(web_client: bot.get_WebClient(), user_id: str, channel_id: str, text: str, attachments: dict): 
    """ The Message Processor Function
        This function recives important data from the payload and decides what to do with it accordingly. """
    
    # Create the producer
    producer = Producer(channel_id, user_id, attachments) 
    
    # Find the specific message type using a list of RegEx possibility
    message_handler = producer.find_message_type(text) 
    
    # If The Message is 'caught' in the regex list
    if message_handler is not None:
        
        # Loop and Post an Array of messages
        if isinstance(message_handler, list): #if array of Messages
            for i in range(len(message_handler)): 
                message = message_handler[i].get_message(attachments)
                response = web_client.chat_postMessage(**message) 
                message_handler[i].timestamp = response["ts"] 
        else: 
            
            # Posts only one Message
            message = message_handler.get_message(attachments)
            response = web_client.chat_postMessage(**message) 
            message_handler.timestamp = response["ts"]
    
    # Delete the producer to save space
    del producer

    

def create_attachments(data) :
    """ This Function Creates Attachments fto a messgae by given payload """
    
    """ Attachments Attributes
        Thread Attachments:
            "ts" = timestamp 
            "thread_ts" = the thread timpstamp
            "in_thread" = if the massage was sent in a thread
            
        Reaction Attributes:
            "item_user" = The user who got reacted 
            
    Returns A Dict"""
        
    attachments = {
        "ts": data.get("ts", ""),
        "thread_ts" : data.get("thread_ts", ""),
        "in_thread" : False,
        "item_user" : data.get("item_user")
    }
    
    if attachments["thread_ts"] != "":
        attachments['in_thread'] = True
        
    return attachments

        
   
""" The Event Reciver Function

    Subscribe to RtM Events: https://api.slack.com/apps?source=post_page
    
    What is The Payload?
        The Payload is a JSON Block that slack sends after each event
        for further reading: https://api.slack.com/reference/messaging/payload
        
    
    @slack.RTMClient.run_on(event="'name_of_the_event'")
    def func(**payload):
        ...
        Write Here What You Want to Happen
        ...
        
"""        
        
@slack.RTMClient.run_on(event="reaction_added")
def reaction_added(**payload):
    print("readtion")
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    user_id = data.get("user")
    channel_id = data.get("item").get("channel")
    text = ":" + data.get("reaction") + ":"
    attachments = create_attachments(data)
    
    # if message sent by user
    if (user_id is not None):
        process_message(web_client, user_id, channel_id, text, attachments)
   

@slack.RTMClient.run_on(event="message")
def message(**payload):
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    user_id = data.get("user")
    channel_id = data.get("channel")
    text = data.get("text")
    attachments = create_attachments(data)
   
    # if message sent by user
    if (user_id is not None):
        process_message(web_client, user_id, channel_id, text, attachments)


if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_TEST"]#os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()
    
    




