### THIS APP USES RTM CLIENT AND NOT EVENT API
import os
import slack
import certifi
import ssl as ssl_lib
from Type.message import Message
from message_producer import MessageProducer


# this variable will contain all sent messages for future use
sent_messages = {}

# Posts the message
def process_message(web_client: slack.WebClient, user_id: str, channel_id: str, text: str, thread_data: dict):
    producer = MessageProducer(channel_id, thread_data)  
    message_handler = producer.get_message_type(text) #
    if message_handler is not None:
        message = message_handler.get_message(thread_data)
        response = web_client.chat_postMessage(**message) # Post the onboarding message in Slack
        message_handler.timestamp = response["ts"] # Capture Time for later use

        # Store the message
        if channel_id not in sent_messages:
            sent_messages[channel_id] = {}
            sent_messages[channel_id][user_id] = message_handler
    
    print(sent_messages)


@slack.RTMClient.run_on(event="reaction_added")
def reaction_added(**payload):
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    user_id = data.get("user")
    channel_id = data.get("item").get("channel")
    text = ":" + data.get("reaction") + ":"
    print(channel_id)
    print(user_id)
    print(text)
    # Allowes to understand if thread or regular message
    thread_data = {
        "ts" : data.get("ts", ""),
        "thread_ts" : data.get("thread_ts", ""),
        "reply_users_count" : int(data.get("reply_users_count", 0)),
        "in_thread" : False
    }

    if thread_data["thread_ts"] != "":
        thread_data['in_thread'] = True

    # if message sent by user
    if (user_id is not None):
        return process_message(web_client, user_id, channel_id, text, thread_data)
   
# On Event Message
@slack.RTMClient.run_on(event="message")
def message(**payload):
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    user_id = data.get("user")
    channel_id = data.get("channel")
    text = data.get("text")
    # Allowes to understand if thread or regular message
    thread_data = {
        "ts" : data.get("ts", ""),
        "thread_ts" : data.get("thread_ts", ""),
        "reply_users_count" : int(data.get("reply_users_count", 0)),
        "in_thread" : False
    }

    if thread_data["thread_ts"] != "":
        thread_data['in_thread'] = True
    

    # if message sent by user
    if (user_id is not None):
        return process_message(web_client, user_id, channel_id, text, thread_data)
    


if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()




