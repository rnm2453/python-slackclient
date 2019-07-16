### THIS APP USES RTM CLIENT AND NOT EVENT API

import os
import slack
import certifi
import flask
import ssl as ssl_lib
from Type.message import Message
from flask import Flask, request, Response
from message_producer import MessageProducer


# this variable will contain all sent messages for future use
sent_messages = {}

# Posts the message
def process_message(web_client: slack.WebClient, user_id: str, channel: str, event_type: str, text: str, *reply): 
    producer = MessageProducer(channel, reply)  
    message_handler = producer.get_message_type(text) #
    if message_handler is not None:
        message = message_handler.get_message(reply)
        response = web_client.chat_postMessage(**message) # Post the onboarding message in Slack
        message_handler.timestamp = response["ts"] # Capture Time for later use

        # Store the message
        if channel not in sent_messages:
            sent_messages[channel] = {}
        sent_messages[channel][user_id] = message_handler

@slack.RTMClient.run_on(event="reaction_added")
def reaction_added(**payload):
    print("reaction")
   

@slack.RTMClient.run_on(event="message_replied")
def message_replied(**payload):
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSss")

# On Event Message
@slack.RTMClient.run_on(event="message")
def message(**payload):
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    event_type = "message"
    text = data.get("text")

    # Allowes to understand if thread or regular message
    ts =  data.get("ts")
    thread_ts = ""

    #in event of reply
    if data.get("thread_ts") is not None:
        thread_ts = data.get("thread_ts")
        reply_user_count = data.get("reply_user_count")
    # if message sent by user
    if (user_id is not None):
        return process_message(web_client, user_id, channel_id, event_type, text, ts, thread_ts, reply_user_count)
    


if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()




