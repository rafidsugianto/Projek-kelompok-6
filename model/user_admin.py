class user_admin: 
    def __init__(self): 
        pass 
    def panggil_user(self, username, password): 
        if username == "RAFID" and password == "170307": 
            return ["OK", username, "Admin"] 
        else: 
            return []

