# python-slackclient
slack client v2.x implementation with python 3.7

Slack Bot Using Slack v2 And Python
========

This is a Slack v2.x Bot Project using the [Real Time Client(RTM)] API written by Slack.
To Create the application and install all of the requirments I followed the [Slack Python Onboarding Tutorial]

More Setup:
  1. Create an Enviormental Variable That Contains The Bot's OAuth Acsess Token
    The Token's format: xoxb-************-************-************************.
    I named it 'SLACK_BOT_TOKEN'

What Can The Following Bot Do:
======== 
  1. Distinguish between DM's and Channels
  2. Respond To Messages
  3. Reply In Threads
  4. React to Reactions
  
  
  
 Listening To Events:
 =======

 <code>
  #NOTE: this code only recives the data, it dosen't do with it anything afterwards
  #The you can use with the RTM can be seen in the link bellow
  
  @slack.RTMClient.run_on(event="message")
  def message(**payload):
    # Get data from message Payload
    data = payload["data"]
    web_client = payload["web_client"]
    user_id = data.get("user")
    channel_id = data.get("channel")
    text = data.get("text")
  
  #Runs The Application  
  if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where()) # Creates Connecton Object
    slack_token = os.environ["SLACK_BOT_TOKEN"] # Fetchs The Slack OAuth Token From The Enviormental Variables
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context) # Creates The Connection With The Bot's Credentials
    rtm_client.start() # Requests Connection with the Web Api
 </code>
 
 ''INSERT LINK""
 So what excactly is the Happening Here?.
 The Messy "__main___" bit Allows The RTM API to send a stream of events to the Web Api
 After we setup the RTM connection to our app, we can use the [Real Time Client(RTM)] to listen to events.
 Each Event recives a payload, this payload contains all the data recived form the Websocket regards to the event.
 
 This is a Basic RTM example.
 


  [Real Time Client(RTM)]: https://api.slack.com/rtm/  "Real Time Client(RTM)"
  [Slack Python Onboarding Tutorial]: https://github.com/rnm2453/python-slackclient-1/tree/master/tutorial  "Slack Python Onboarding Tutorial"




