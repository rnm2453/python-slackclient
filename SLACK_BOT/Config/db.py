import mysql.connector
from datetime import datetime

release_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
conn = mysql.connector.connect(host= 'localhost', user= 'root', passwd= 'Game1234monkey', db= 'slackusers')
