#!C:/Users/Roey Lifshitz/AppData/Local/Programs/Python/Python37/python.exe
#My Python Path
print("Content-Type: text/html")
print()
print ("""
    <TITLE>CGI script ! Python</TITLE>
    <H1>The Bot is Running</H1>
    Hello, world!
"""
)
### THIS APP USES RTM CLIENT AND NOT EVENT API
import os
import slack
import certifi
import datetime
import ssl as ssl_lib
from message_producer import MessageProducer, bot


# Posts the message
def process_message(web_client: bot.get_WebClient(), user_id: str, channel_id: str, text: str, attachments: dict):
    producer = MessageProducer(channel_id, user_id, attachments)
    print(bot.get_username(user_id))  
    message_handler = producer.find_message_type(text) 
    if message_handler is not None:
        if isinstance(message_handler, list): #if array of Messages
            for i in range(len(message_handler)): 
                message = message_handler[i].get_message(attachments)
                response = web_client.chat_postMessage(**message) # Post the onboarding message in Slack
                message_handler[i].timestamp = response["ts"] # Capture Time for later use
        else: 
            message = message_handler.get_message(attachments)
            response = web_client.chat_postMessage(**message) # Post the onboarding message in Slack
            message_handler.timestamp = response["ts"] # Capture Time for later use
    del producer
        
      


@slack.RTMClient.run_on(event="reaction_added")
def reaction_added(**payload):
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    user_id = data.get("user")
    channel_id = data.get("item").get("channel")
    text = ":" + data.get("reaction") + ":"
    attachments = create_attachments(data)
    # if message sent by user
    if (user_id is not None):
        return process_message(web_client, user_id, channel_id, text, attachments)
   
# On Event Message
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
        return process_message(web_client, user_id, channel_id, text, attachments)
    

def create_attachments(data) :
    attachments = {
        #thread_attachments
        "ts": data.get("ts", ""),
        "thread_ts" : data.get("thread_ts", ""),
        "in_thread" : False,
        #reaction_attachments
        "item_user" : data.get("item_user", None)
    }
    if attachments["thread_ts"] != "":
        attachments['in_thread'] = True
    return attachments

if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()
    
    




