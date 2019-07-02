import os
import re
import time
import slack 
from slack import WebClient
#from slack import WebClient

#get bot token
slack_token = os.environ["SLACK_API_TOKEN"]
print (slack_token)

