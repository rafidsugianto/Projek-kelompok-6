import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          
        database="database_toko"  
    )

def get_data(query, values=None):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, values)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

# print(db.mydb)
        