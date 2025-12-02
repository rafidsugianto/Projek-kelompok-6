import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="database_toko"
        )
        self.cursor = self.mydb.cursor()

db = Database()
