import os
import mysql.connector as connection

class mysqlConnect():
    def __init__(self):
        self.mydb = connection.connect(
            host     = os.getenv("DB_CONNECTION_HOST"), 
            database = os.getenv("DB_CONNECTION_NAME"),
            user     = os.getenv("DB_CONNECTION_USER"), 
            passwd   = os.getenv("DB_CONNECTION_PASS"),
            use_pure = True    
        )


