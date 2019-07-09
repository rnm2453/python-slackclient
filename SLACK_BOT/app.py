import logging
import slack
import ssl as ssl_lib
import os
import certifi
from message_producer import MessageProducer


sent_messages = {}

def process_message(web_client: slack.WebClient, user_id: str, channel: str, text: str):   
    producer = MessageProducer(channel)  
    message_handler = producer.get_message_type(text) # Get the onboarding message payload
    if message_handler is not None:
        message = message_handler.get_message()
        response = web_client.chat_postMessage(**message) # Post the onboarding message in Slack
        message_handler.timestamp = response["ts"] # Capture Time for later use

        # Store the message sent in onboarding_tutorials_sent
        if channel not in sent_messages:
            sent_messages[channel] = {}
        sent_messages[channel][user_id] = message_handler

@slack.RTMClient.run_on(event="message")
def message(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")
    return process_message(web_client, user_id, channel_id,text )
            

if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()

