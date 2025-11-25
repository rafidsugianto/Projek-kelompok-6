from model import database as db
class user_admin:
    def __init__(self):
        pass
    def panggil_user(self, username, password):
        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        values = (username, password)

        hasil = db.get_data(query, values)

        return hasil

