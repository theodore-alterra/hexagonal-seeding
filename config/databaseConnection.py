import os
import mysql.connector as connection
from config.config import get_config

class mysqlConnect():
    def __init__(self):
        get_config()
        self.mydb = connection.connect(
            host     = os.getenv("DB_CONNECTION_HOST"), 
            database = os.getenv("DB_CONNECTION_NAME"),
            user     = os.getenv("DB_CONNECTION_USER"), 
            passwd   = os.getenv("DB_CONNECTION_PASS"),
            use_pure = True    
        )


