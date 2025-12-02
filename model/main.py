from tkinter import *
from tkinter import ttk
import user_admin as us
from user_admin import UserRepo
from tkinter import messagebox


user_repo = us.UserRepo()

class MainApp:
    def __init__(self, root):   
        self.root = root
        self.root.title("Data Inventory")
        self.root.geometry("1000x1000")

        self.label = ttk.Label(root, text="Username", font=("Arial", 14))
        self.label.pack(pady=200)
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
        self.current_user = user_repo.panggil_user(username,password)

        print("Username:", username)
        print("Password:", password)

        
        if len(username):
            print("Login berhasil!")
            print(f"Anda login sebagai {self.current_user.username_admin}")
            messagebox.showinfo("Success", f"login berhasil {self.current_user.username_admin}")
            self.admin_login()
        else:
            print("Username atau password salah")

    def admin_login(self):
        self.clear_window()

        self.root.title("admin login")
        self.root.geometry("600x410")
        self.root.configure(bg="#2A1F3D")

   
        ttk.Label(self.root, text="MENU ADMIN BANK", font=("Arial", 16)).pack(pady=20)
        ttk.Button(self.root, text="Lihat Nasabah", width=25, ).pack(pady=5)
        ttk.Button(self.root, text="Tambah Nasabah", width=25, ).pack(pady=5)
        ttk.Button(self.root, text="Lihat Transaksi", width=25).pack(pady=5)
        ttk.Button(self.root, text="Keluar", width=25, command=quit).pack(pady=20)

    def clear_window(self):
	    for widget in self.root.winfo_children():
	        widget.destroy()
root = Tk()
app = MainApp(root)
root.mainloop()

