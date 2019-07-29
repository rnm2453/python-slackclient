     
import mysql.connector
import threading
from datetime import datetime

class Database:
    """
        This is the 'DataBase' class.

        This Class Alters a MySQL DataBase.
        
        Attributes:
            conn = A Connection to a database
            cursor = MySQL cursor
            
        Methods That Alter The Data Base:
            connect = connects to the database
            insert = insers data to the database
            remove = remove data from the database
            update = updates data from the database
            
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

    def remove(self, name: str):
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
        # Recives a name of a product and return all the data of the prodcut as seen in the database
        query = f"SELECT * FROM `products` WHERE `name` LIKE '%{name}%'"
        result = self.cursor.execute(query)
        product = self.cursor.fetchall()
        print(product)
        return product

    def is_exists(self, name: str):
        # check if the product exisits in database
        products = self.get_data_by_name(name)
        if len(products) == 0:
            return False
        return True

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
        # Recives a name of a prodcut and find if it is currently occupied
        product = self.get_data_by_name(name)[0]
        if product["release_time"] is not None:
            if product["release_time"] > datetime.now():
                return True
        return False

    def is_occupied(self, product: dict):
        # Recives a products and finds if it is occupied
        if product['release_time'] is not None:
            if product['release_time'] > datetime.now():
                return True

        return False
                
    def refresh_occupied(self):
        # Loops through the database and updates if an item is occupied or not
        query = f"SELECT * FROM `products`"
        result = self.cursor.execute(query)
        products = self.cursor.fetchall()
        for product in products:
            if self.is_occupied(product):
                pass
            else:
                self.update(product['name'], "", "", "")
        print("Record refreshed successfully `products` table ")


    def show_all(self):
        # Returns A String of all the prodcuts in the database
        query = f"SELECT * FROM `products`"
        result = self.cursor.execute(query)
        products = self.cursor.fetchall()
        s = ""
        for product in products:
            s = s + self.product_toString(product) + "\n"
        return s

    def show(self, name: str):
        # returns a string of all the products that contain the name
        query = f"SELECT * FROM `products` WHERE `name` LIKE '%{name}%'"
        result = self.cursor.execute(query)
        products = self.cursor.fetchall()
        s = ""
        for product in products:
            s = s + self.product_toString(product) + "\n"
        return s

    def show_all_availlable(self):
        # return a string of all availlavle products that contain the name
        query = f"SELECT * FROM `products`"
        result = self.cursor.execute(query)
        products = self.cursor.fetchall()
        s = ""
        for product in products:
            if self.is_occupied(product) == False:
                s = s + self.product_toString(product) + "\n"
        return s

    def show_availlable(self, name: str):
        # return a string of all availlable products
        query = f"SELECT * FROM `products` WHERE `name` LIKE '%{name}%'"
        result = self.cursor.execute(query)
        products = self.cursor.fetchall()
        print(products)
        s = ""
        for product in products:
            if self.is_occupied(product) == False:
                s = s + self.product_toString(product) + "\n"
        return s
            
    def product_toString(self, product):
        # translates product data into a string
        name = str(product['name'])
        occupied_by = str(product['occupied_by'])
        start_time = str(product['start_time'])
        release_time = str(product['release_time'])

        return f"Name: {name}, Occupied_by: {occupied_by}, start_Time: {start_time}, release_time: {release_time}"
    
    def close_connection(self):
        self.cursor.close()
        self.conn.close()


   
        



