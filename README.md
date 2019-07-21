# python-slackclient
slack client v2.x implementation with python 3.7

Slack Bot Using Slack v2 And Python
========

This is a Slack v2.x Bot Project using the [Real Time Client(RTM)] API written by Slack.
To Create the application and install all of the requirments I followed the *[Slack Python Onboarding Tutorial]*

###### More Setup:
1. Remeber to follow the [Slack Python Onboarding Tutorial] to create your application.
2. Create an Enviorment Variable That Contains The Bot's OAuth Acsess Token. a Quick Google search should teach you how to do it. but if you are to lasy follow this [For Windows] or this [For Python] tutorial
3. Please keep in mind the the Token format is: xoxb-\*\*\*\*\*\*\*\*\*\*\*\*\-\*\*\*\*\*\*\*\*\*\*\*\*\-\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**.
4. I named it 'SLACK_BOT_TOKEN'.

What Can The Following Bot Do:
======== 
  1. Distinguish between DM's and Channels
  2. Respond To Messages
  3. Reply In Threads
  4. React to Reactions
  5. And More if you want to :sunny:
  
  
  
 Listening To Events:
 =======

```python
  """ NOTE: The Following code will print the Slack Message Payload using RTM Client"""
  
  @slack.RTMClient.run_on(event="message")
  def message(**payload):
    print(payload)
  
  #Runs The Application  
  if __name__ == __main___:
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where()) # Creates Connecton Object
    slack_token = os.environ["SLACK_BOT_TOKEN"] # Fetchs The Slack OAuth Token From The Enviormental Variables
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context) # Starts The Connection With The Bot's Credentials
    rtm_client.start() # Requests Connection from the Web Api
 </code>
 ```
 
 ###### So what excactly is the Happening Here?.
 The Messy "\_\__main___" bit Allows The [Real Time Client(RTM)] to send a stream of events to the Web Api.
 This is the most complicated part and you dont need to fully understand it to continue creating your bot.
 After we setup the RTM connection to our app, we can use the [Real Time Client(RTM)] to listen to events.
 Each Event recives a payload, the payload contains all the data recived from the Web API.
 
 This is a Basic RTM example.
 
How The Bot Works?
======
1. The bot listen to events as seen before
2. The bot uses the [Real Time Client(RTM)] to react to the events
3. The bot recives a payload and send some data to a processing function
4. The proccesiong function creates a message_producer with given params
5. The message_producer builds the response
6. The response return all the way back to the processing function
7. The processing function posts the response

There are many ways to structure a bot code, but this is the one i used

Project Files
=======
The Project Consists of:
```
| python-slackclient
|── SLACK_BOT
|   |── app.py                        # Application Page
|   |── message_producer.py           # messageProducer Constructor Function
|   |── Type
|   |   |── message.py                # message Constructor Function
|   |   |── onboarding.py             # onboarding Constructor Function
|   |   └── ...
|   |── .gitignore
|   |── requirements.txt              # requirements to install slack  
|   |── README.md                     # README file
|   └── ...
└── ...
```
###### Python File's. What should I change? purpose
 * app.py- listens to different RTM events and runs the application. can add/remove events
 * message_producer.py- recives differnt inputs and creates outputs respectavly. may need to change depends on the events
 * message.py- a generic message constructor. No need to Change 
 * onboarding.py- a onboarding message. Do as you wish, its your bot and you messages 
 *There is really nothing else in this project if you followed the installation tutorial already
 * To Create Messages with different layouts you need to create a new file and follow Slack's 'Message Block layout" page
 

  [Real Time Client(RTM)]: https://api.slack.com/rtm/  "Real Time Client(RTM)"
  [Slack Python Onboarding Tutorial]: https://github.com/rnm2453/python-slackclient-1/tree/master/tutorial  "Slack Python Onboarding Tutorial"
  [For Windows]: https://helpdeskgeek.com/how-to/create-custom-environment-variables-in-windows "For Windows"
  [For Python]: https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python "For Python"
  [Message Block layout]: https://api.slack.com/reference/messaging/blocks "Message Block layout"
