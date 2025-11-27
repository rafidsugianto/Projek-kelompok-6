from tkinter import *
from tkinter import ttk
from model import user_admin as us

user_model = us.user_admin()   

class MainApp:
    def __init__(self, root):   
        self.root = root
        self.root.title("Login")
        self.root.geometry("480x210")

        self.label = ttk.Label(root, text="Username")
        self.label.pack()
        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack()

        self.label = ttk.Label(root, text="Password")
        self.label.pack()
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.button = ttk.Button(self.root, text="Login", command=self.proses_login)
        self.button.pack(pady=10)

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        print("Username:", username)
        print("Password:", password)

        user_login = user_model.panggil_user(username, password)

        if len(user_login):
            print("Login berhasil!")
            print(f"Anda login sebagai {user_login[2]}")
        else:
            print("Username atau password salah")


root = Tk()
app = MainApp(root)
root.mainloop()

