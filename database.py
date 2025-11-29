import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   
        database="database_toko"
    )

def insert_data(query, values):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()

def get_data(query, values=None):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, values)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
