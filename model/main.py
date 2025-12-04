from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Inventory")
        self.root.geometry("1000x700")

        # warma default
        self.GRAY_BG = "#2A1F3D"
        self.LIGHT_BG = "#F1F1F1"
        self.TEXT_COLOR = "black"

        # --- HALAMAN LOGIN ---
        self.login_screen()


    # ==========================================================
    #	SCREEN: LOGIN
    # ==========================================================
    def login_screen(self):
        self.clear_window()

        # Title
        ttk.Label(self.root, text="Username", font=("Arial", 14)).pack(pady=20)
        self.entry_username = ttk.Entry(self.root, width=30)
        self.entry_username.pack()

        ttk.Label(self.root, text="Password", font=("Arial", 14)).pack(pady=10)
        self.entry_password = ttk.Entry(self.root, show="*", width=30)
        self.entry_password.pack()

        ttk.Button(self.root,
                   text="Login",
                   width=20,
                   command=self.proses_login).pack(pady=20)


    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "123":
            messagebox.showinfo("Success", f"Login berhasil sebagai {username}")
            self.admin_login()
        else:
            messagebox.showerror("Error", "Username atau password salah")


    #	SCREEN: MENU ADMIN
    def admin_login(self):
        self.clear_window()
        self.root.title("Admin Panel")
        self.root.configure(bg=self.GRAY_BG)

        Frame(self.root, height=40, bg=self.GRAY_BG).pack()

        ttk.Label(self.root,
                  text="MENU ADMIN INVENTORY",
                  font=("Arial", 18)).pack(pady=10)

        ttk.Button(self.root,
                   text="Lihat Barang",
                   width=25,
                   command=self.lihat_barang).pack(pady=10)

        ttk.Button(self.root,
                   text="Exit",
                   width=25,
                   command=self.root.quit).pack(pady=10)


    # ==========================================================
    #	SCREEN: LIHAT BARANG (TABEL)
    # ==========================================================
    def lihat_barang(self):
        self.clear_window()

        self.root.title("Daftar Barang")
        self.root.configure(bg=self.LIGHT_BG)

        Frame(self.root, height=15, bg=self.LIGHT_BG).pack()

        ttk.Label(self.root,
                  text="Data Barang",
                  font=("Arial", 18)).pack(pady=10)

        # Tombol back
        ttk.Button(self.root,
                   text="← Kembali",
                   width=20,
                   command=self.admin_login).pack(pady=10)

        # Container tabel
        container = Frame(self.root)
        container.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Scrollbar
        scrollbar = ttk.Scrollbar(container, orient=VERTICAL)

        # Treeview
        self.tableBarang = ttk.Treeview(
            container,
            columns=("No", "Nama", "Stok", "Harga"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )

        scrollbar.config(command=self.tableBarang.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Header kolom
        self.tableBarang.heading("No", text="ID")
        self.tableBarang.heading("Nama", text="Nama Barang")
        self.tableBarang.heading("Stok", text="Stok")
        self.tableBarang.heading("Harga", text="Harga")

        # Lebar kolom
        self.tableBarang.column("No", width=50, anchor="center")
        self.tableBarang.column("Nama", width=250)
        self.tableBarang.column("Stok", width=100, anchor="center")
        self.tableBarang.column("Harga", width=150, anchor="center")

        self.tableBarang.pack(fill=BOTH, expand=True)

        # load data
        self.load_data_barang()


    # ==========================================================
    #	FUNGSI LOAD DATA BARANG
    # ==========================================================
    def load_data_barang(self):

        # data dummy contoh
        data = [
            (1, "Kabel HDMI", 10, "Rp 45.000"),
            (2, "Mouse Wireless", 25, "Rp 70.000"),
            (3, "Keyboard Mechanical", 8, "Rp 350.000"),
            (4, "Flashdisk 64GB", 22, "Rp 95.000"),
        ]

        # masukkan data ke tabel
        for item in data:
            self.tableBarang.insert("", END, values=item)


    # ==========================================================
    #	FUNGSI CLEAR WINDOW
    # ==========================================================
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ==========================================================
# MAIN TKINTER
# ==========================================================
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
