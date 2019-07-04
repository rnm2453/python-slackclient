import os
import logging
import slack
import ssl as ssl_lib
import certifi
from lists import messageList
from Classes.onMessage import OnMessage
from Classes.onBoarding import OnBoarding


sent_messages = {}

def start_onBoarding(web_client: slack.WebClient, user_id: str, channel: str):
   
    onBoarding = OnBoarding(channel)  # Create a new onboarding.
    message = onBoarding.get_message_payload() # Get the onboarding message payload
    response = web_client.chat_postMessage(**message) # Post the onboarding message in Slack
    onBoarding.timestamp = response["ts"] # Capture Time for later use

    # Store the message sent in onboarding_tutorials_sent
    if channel not in sent_messages:
        sent_messages[channel] = {}
    sent_messages[channel][user_id] = onBoarding

def start_onMessage(web_client: slack.WebClient, user_id: str, channel: str, msg: str):
       
    onMessage = OnMessage(channel, msg)
    message =  onMessage.get_message_payload()
    response = web_client.chat_postMessage(**message)
    onMessage.timestamp = response["ts"]

    # Store the message sent in onboarding_tutorials_sent
    if channel not in sent_messages:
        sent_messages[channel] = {}
    sent_messages[channel][user_id] = onMessage

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the update_share callback to the 'message' event.
@slack.RTMClient.run_on(event="message")
def message(**payload):
    """Display the onboarding welcome message after receiving a message that contains "start" """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    
    if text and text.lower() == "start":
        return start_onBoarding(web_client, user_id, channel_id)

    for var in messageList:
        if text and text.lower() == var:
            return start_onMessage(web_client, user_id, channel_id, messageList[var])
            

if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()
