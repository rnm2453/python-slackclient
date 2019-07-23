import mysql.connector
from datetime import datetime

release_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
conn = mysql.connector.connect(host= 'localhost', user= 'root', passwd= 'Game1234monkey', db= 'slackusers')
print(conn)

query = "INSERT INTO `products` (`id`, `name`, `occupied_by`, `start_time`, `release_time`) VALUES (NULL, 'a', 's', CURRENT_TIMESTAMP, '{release_time}')"
#f"INSERT INTO `products` (`id`, `name`, `occupied_by`, `start_time`, `release_time`) VALUES (NULL, 'screen', 'roey', CURRENT_TIMESTAMP, )"
print(query)
cursor = conn.cursor()
result  = cursor.execute(query)
conn.commit()
print ("Record inserted successfully into 'products' table")

