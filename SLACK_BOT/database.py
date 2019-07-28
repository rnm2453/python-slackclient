     
import mysql.connector
import threading
from datetime import datetime

class Database:
    """
        This is the 'DataBase' class.

        This Class Alters a MySQL DataBase.
    """
    def __init__(self, host: str, root: str, passwd: str, db: str): 
        self.host = host
        self.root = root
        self.passwd = passwd
        self.db = db
        self.conn = mysql.connector.connect(host = self.host, user = self.root, passwd = self.passwd, db = self.db)
        self.cursor = self.conn.cursor(dictionary= True)

    def connect(self, host: str, root: str, passwd: str, db: str):
        self.conn = mysql.connector.connect(host= host, user= root, passwd= passwd, db= db)

    def insert(self, name: str, occupied_by: str, start_time: datetime, release_time: datetime):
        query = f"INSERT INTO `products` (`id`, `name`, `occupied_by`, `start_time`, `release_time`) VALUES (NULL, '{name}', '{occupied_by}', '{start_time}', '{release_time}')"
        result = self.cursor.execute(query)
        self.conn.commit()

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

    def get_data_by_name(self, name: str):
        query = f"SELECT * FROM `products` WHERE `name` = '{name}'"
        result = self.cursor.execute(query)
        product = self.cursor.fetchall()
        print(product)
        return product[0]

    def delta_release_by_name(self, name: str):
        # Finds Time Left Till Release Of Item
        product = self.get_data_by_name(name)
        release_time = product["release_time"]
        current_time = datetime.now()
        deltatime = release_time - current_time

        # Format The Time so it will be easy to read
        s = deltatime.total_seconds()
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        
    def is_occupied_by_name(self, name: str):
        product = self.get_data_by_name(name)
        if product["release_time"] is not None:
            if product["release_time"] > datetime.now():
                return True
        return False

    def is_occupied(self, product: dict):
        if product['release_time'] is not None:
            if product['release_time'] > datetime.now():
                return True

        return False
                
    def refresh_occupied(self):
        query = f"SELECT * FROM `products`"
        result = self.cursor.execute(query)
        products = self.cursor.fetchall()
        for product in products:
            if self.is_occupied(product):
                pass
            else:
                self.update(product['name'], "", "", "")
        print("Record refreshed successfully `products` table ")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


   
        



