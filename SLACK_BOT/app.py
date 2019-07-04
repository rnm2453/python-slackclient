import os
import logging
import slack
import ssl as ssl_lib
import certifi
from onboarding import Onboarding

onboarding_sent = {}


def start_onboarding(web_client: slack.WebClient, user_id: str, channel: str):
    # create new Onboarding
    onboarding = Onboarding(channel)
    
    # Get the onboarding message payload
    message = onboarding.get_message_payload()

    # Post the onboarding message in Slack
    response = web_client.chat._postMessage(**message)

    # Capture time Stamp for later user
    Onboarding.timestamp = response["ts"]

    if channel not in onboarding_sent:
        onboarding_sent[channel] = {}
    onboarding_sent[channel][user_id] = onboarding

"""
    DM MESSAGE EVENT
"""

@slack.RTMClient.run_on(event= "team_join")
def message(**payload):
    # Display the onboarding welcome message after reciving the message that containes start

    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if text and text.lower() == "start":
        return start_onboarding(web_client, user_id, channel_id)

if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()

    
"""
The Way to Store Data
{
    "channel" : {
        "user_id": Onboarding
    }
}

"""
"""
import certifi
from onboarding import Onboarding

"""

