import mysql.connector
from datetime import datetime


class database_alternator:
    def __init__(self, host: str, root: str, passwd: str, db: str): 

        self.host = host
        self.root = root
        self.passwd = passwd
        self.db = db
        self.conn = mysql.connector.connect(host = self.host, user = self.root, passwd = self.passwd, db = self.db)
        self.cursor = self.conn.cursor()

    def connect(self, host: str, root: str, passwd: str, db: str):
        self.conn = mysql.connector.connect(host= host, user= root, passwd= passwd, db= db)

    def insert(self, name: str, occupied_by: str, start_time: datetime, release_time: datetime):
        query = f"INSERT INTO `products` (`id`, `name`, `occupied_by`, `start_time`, `release_time`) VALUES (NULL, '{name}', '{occupied_by}', '{start_time}', '{release_time}')"
        result = self.cursor.execute(query)
        self.conn.commit()
        print ("Record inserted successfully into 'products' table")

    def remove(self, name: str, occupied_by: str, start_time: datetime, release_time: datetime):
        query = f"DELETE FROM `products` WHERE `name` = '{name}'"
        result = self.cursor.execute(query)
        self.conn.commit()
        print("")

    def update(self, name: str, occupied_by: str, start_time: datetime, release_time: datetime):
        query =  f"UPDATE `products` SET `occupied_by` = '{occupied_by}', `start_time` = '{start_time}', `release_time` = '{release_time}' WHERE `name` = '{name}'"
        result = self.cursor.execute(query)
        self.conn.commit()
        print("Record updated successfully from 'products' table")

    def is_occupied(self, name: str):
        query = f"SELECT * FROM `products` WHERE `name` = '{name}'"
        result = self.cursor.execute(query)
        product = result.fetchall()
        
        if product["release_time"] < datetime.now():
            return False
        return Frue
        
        self.conn.commit()
    def close_connection(self):
        self.cursor.close()
        self.conn.close()


        



