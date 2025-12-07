import database


class DataUser:
    def __init__(self, username_admin, password_admin):
        self.username_admin = username_admin
        self.password_admin = password_admin
     
    def insert_user(self):
        query = """
            INSERT INTO user_admin (username_admin, password_admin)
            VALUES (%s, %s)
        """
        values = (self.username_admin, self.password_admin)
        database.db.cursor.execute(query, values)
        database.db.mydb.commit()
        print("User berhasil ditambahkan:", self.username_admin)

class UserRepo:
    def __init__(self):
        # self.db = connect() 
        self.db = database.db

    def ambil_user(self):
        sql = "SELECT username_admin, password_admin FROM user_admin "
        self.db.cursor.execute(sql)
        results = self.db.cursor.fetchall()
        users = [DataUser(r[0], r[1],) for r in results]
        return users

    def panggil_user(self, username, password):
        sql = """
        SELECT username_admin, password_admin 
        FROM user_admin 
        WHERE username_admin = %s AND password_admin = %s
        """
        values = (username, password)

        self.db.cursor.execute(sql, values)
        row = self.db.cursor.fetchone()

        if row:
            return DataUser(row[0], row[1])

        return None

    
    def ambil_semua_user(self):
        sql = "SELECT no_rek, username_us, balance, role_us FROM datauser"
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()

   