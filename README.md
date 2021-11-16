# python-slackclient
slack client v2.x implemetation with python 3.7
Slack Bot Using Slack v2, Python And MySQl

What Can The Following Bot Do:
======== 
  1. Distinguish between DM's and Channels
  2. Respond To Messages
  3. Reply In Threads
  4. React to Reactions
  5. Alter A Database
  6. And More if you want to :sunny:
  

Setup:
======== 
This is a Slack v2.x Bot Project using the [Real Time Client(RTM)] API written by Slack And a MySQL Database.

1. Install requirements. 
    * To do so, just follow the first page of [Slack Python Onboarding Tutorial]
    
2. Install the bot to your workspace and Create a Enviorment Variable that contains the Bot's OAuth acsess token named SLACK_BOT_TOKEN (The name isnt really important).
    * To do so, follow this [For Windows] or this [For Python] tutorial
    * Please keep in mind the the Token format is: xoxb-\*\*\*\*\*\*\*\*\*\*\*\*\-\*\*\*\*\*\*\*\*\*\*\*\*\-\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**.
   
3. restart your computer to save the enviorment variable (if on windows)

3. Install Xampp, And Pip install mysql-connector, or mysql-connector-python

4. Enable python in Xampp.
    * How to [Run Python With Xampp]

5. Head to the xampp/htdocs folder on your computer, and create a new one for your project

6. Create a Database.
    * To do so, Run Apchae and MySQL on the Xampp control pannel.
    * head to localhost/phpmyadmin
    * create a new table on the menu at the right side
    * create a new table inside the database and add the values you want. 
  
  
 Listening To Events:
======== 

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
    rtm_client.start() # Requests Connection from the Web API

 ```
 
 ###### So what excactly is the Happening Here?.
 The Messy "\_\__main___" Allows The [Real Time Client(RTM)] to send a stream of events to the Web API.
 This is the most complicated part and you dont need to fully understand it to create your own bot.
 After we setup the RTM connection to our app, we can use the RTM to listen to events.
 Each Event recives a payload, the payload contains all the data sent from the Web API.
 

Connect Bot to Database
======== 
After creating a database, installing myslq-connector, configuring xampp to work with python. copy the following code.
```python
  import mysql.connector
    """ This is a basic example on how to connect a python script to a MySQL xampp database """         
    def connect_to_db(host: str, root: str, passwd: str, db: str): 
      """ The Function Creates a Connection to a DB

        Attributes:
          host = 'your_host_name'
          root = 'root'
          passw = 
            no password by default
          db = 'your database name' """

        self.host = host
        self.root = root
        self.passwd = passwd
        self.db = db
        self.conn = mysql.connector.connect(host = self.host, user = self.root, passwd = self.passwd, db = self.db)
        
```
  The [Database Connection] link can help you find the values of each argument for your computer to run the bot locally.

 
How The Bot Works?
======
1. The bot listen to events as seen before
2. The bot uses the [Real Time Client(RTM)] to react to the events
3. The bot recives a payload and send some data to a processing function
4. The proccesiong function creates a producer with given params
5. The producer builds the response
6. The response return all the way back to the processing function
7. The processing function posts the response


Project Files
=======
The Project Consists of:
```
| python-slackclient
|── SLACK_BOT
|   |── app.py                        # Application Page
|   |── producer.py                   # Producer Constructor Function
|   |── bot.py                        # Bot Constructor Function
|   |── database.py                   # Database Constructor Function
|   |── Type
|   |   |── message.py                # message Constructor Function
|   |   └── ...
|   |── .gitignore
|   |── requirements.txt              # requirements to install slack  
|   |── README.md                     # README file
|   └── ...
└── ...
```
Purpose OF Each File
=======
 * app.py- listens to different RTM events and runs the application. can add/remove events
 * producer.py- recives differnt inputs and creates outputs respectavly. may need to change depends on the events
 * bot.py- find the bot username, id and connects everything to the WebClient
 * database.py- alters the database, you may need to change it depeneding on your database
 * message.py- a generic message constructor. No need to Change 
 * 
 * To Create Messages with different layouts you need to create a new file and follow Slack's 'Message Block layout" page
 


  [Real Time Client(RTM)]: https://api.slack.com/rtm/  "Real Time Client(RTM)"
  [Slack Python Onboarding Tutorial]: https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/docs/Section-2.md  "Slack Python Onboarding Tutorial"
  [For Windows]: https://helpdeskgeek.com/how-to/create-custom-environment-variables-in-windows "For Windows"
  [For Python]: https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python "For Python"
  [Message Block layout]: https://api.slack.com/reference/messaging/blocks "Message Block layout"
  [Run Python With Xampp]: https://stackoverflow.com/questions/42704846/running-python-scripts-with-xampp "Run Python With Xammpp"
  [Database Connection]: https://www.quora.com/Where-do-I-find-my-localhost-name-and-my-user-name-on-phpMyAdmin "Database Connection"
