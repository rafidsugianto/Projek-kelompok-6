from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import check_login, get_barang, insert_barang, delete_barang, update_stok


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Inventory")
        self.root.geometry("1100x680")
        self.root.configure(bg="#110CB2")

        # Style UI
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton", font=("Arial", 11))
        style.configure("TLabel", font=("Arial", 11))

        # Table style
        style.configure("Treeview",
                        font=("Arial", 11),
                        rowheight=28,
                        background="white",
                        foreground="black",
                        fieldbackground="white")

        style.configure("Treeview.Heading",
                        font=("Arial", 12, "bold"),
                        background="#00CED1",
                        foreground="white")

        style.layout("Treeview",
                     [('Treeview.treearea', {'sticky': 'nswe'})])

        # Title Style
        style.configure("Title.TLabel", font=("Arial", 28, "bold"))

        self.login_screen()

    # Clear Window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ======================== LOGIN SCREEN ===========================
    def login_screen(self):
        self.clear_window()

        container = Frame(self.root, bg="#f4f6f9")
        container.pack(expand=True, fill=BOTH)

        # Left Title
        left = Frame(container, bg="#f4f6f9")
        left.pack(side=LEFT, expand=True, fill=BOTH, padx=80, pady=50)

        ttk.Label(left, text="Data Inventory", style="Title.TLabel").pack(anchor="w")

        # Right Login Card
        right = Frame(container, bg="#f4f6f9")
        right.pack(side=RIGHT, expand=True, fill=BOTH, padx=80, pady=50)

        card = ttk.Frame(right)
        card.pack(pady=20, ipadx=30, ipady=30)

        ttk.Label(card, text="Login", font=("Arial", 16, "bold")).pack(pady=10)

        ttk.Label(card, text="Username").pack(anchor="w", padx=20, pady=5)
        self.entry_username = ttk.Entry(card, width=25)
        self.entry_username.pack(padx=20, pady=5)

        ttk.Label(card, text="Password").pack(anchor="w", padx=20, pady=5)
        self.entry_password = ttk.Entry(card, show="*", width=25)
        self.entry_password.pack(padx=20, pady=5)

        ttk.Button(card, text="Login", width=20, command=self.proses_login).pack(pady=15)

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if check_login(username, password):
            messagebox.showinfo("Success", f"Login berhasil sebagai {username}")
            self.admin_login()
        else:
            messagebox.showerror("Error", "Username atau password salah")

    # =========================== ADMIN MENU ===========================
    def admin_login(self):
        self.clear_window()

        frame = Frame(self.root, bg="#f4f6f9")
        frame.pack(expand=True)

        ttk.Label(frame, text="Dashboard Admin", style="Title.TLabel").pack(pady=20)

        ttk.Button(frame, text="Manajemen Stok", width=25, command=self.lihat_barang).pack(pady=8)
        ttk.Button(frame, text="Data Barang", width=25, command=self.buka_data_barang).pack(pady=8)
        ttk.Button(frame, text="Logout", width=25, command=self.login_screen).pack(pady=8)

    # ====================== HALAMAN DATA BARANG =======================
    def lihat_barang(self):
        self.clear_window()

        container = Frame(self.root, bg="#f4f6f9")
        container.pack(expand=True, fill=BOTH)

        # LEFT TABLE
        left = Frame(container, bg="#f4f6f9")
        left.pack(side=LEFT, expand=True, fill=BOTH, padx=25, pady=20)

        ttk.Label(left, text="Manajemen Barang",
                  font=("Arial", 20, "bold")).pack(pady=10)

        table_card = ttk.Frame(left)
        table_card.pack(fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(table_card, orient=VERTICAL)

        self.tableBarang = ttk.Treeview(
            table_card,
            columns=("nama_barang", "kategori_barang", "kode_barang", "stok"),
            show="headings"
        )

        scrollbar.config(command=self.tableBarang.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # HEADER
        self.tableBarang.heading("nama_barang", text="Nama")
        self.tableBarang.heading("kategori_barang", text="Kategori")
        self.tableBarang.heading("kode_barang", text="Kode")
        self.tableBarang.heading("stok", text="Stok")

        # COLUMN WIDTH
        self.tableBarang.column("nama_barang", width=250)
        self.tableBarang.column("kategori_barang", width=120, anchor="center")
        self.tableBarang.column("kode_barang", width=120, anchor="center")
        self.tableBarang.column("stok", width=80, anchor="center")

        self.tableBarang.pack(fill=BOTH, expand=True)

        # RIGHT ACTION PANEL
        right = Frame(container, bg="white")
        right.pack(side=RIGHT, fill=Y, padx=10, pady=20)

        ttk.Label(right, text="Actions",
                  font=("Arial", 18, "bold")).pack(pady=15)

        ttk.Button(right, text="Tambah Barang",
                   width=20,
                   command=self.form_add_barang).pack(pady=8)

        ttk.Button(right, text="Tambah Stok",
                   width=20,
                   command=self.tambah_stok).pack(pady=8)

        ttk.Button(right, text="Hapus Barang",
                   width=20,
                   command=self.hapus_barang).pack(pady=8)

        ttk.Button(right, text="← Kembali",
                   width=20,
                   command=self.admin_login).pack(side=BOTTOM, pady=15)

        self.load_data_barang()

    def buka_data_barang(self):
        self.clear_window()

        container = Frame(self.root, bg="#f4f6f9")
        container.pack(expand=True, fill=BOTH)

        ttk.Label(container, text="Data Barang",
                font=("Arial", 20, "bold")).pack(pady=10)

        table_card = ttk.Frame(container)
        table_card.pack(fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(table_card, orient=VERTICAL)

        self.tableBarang = ttk.Treeview(
            table_card,
            columns=("nama_barang", "kategori_barang", "kode_barang", "stok"),
            show="headings"
        )

        scrollbar.config(command=self.tableBarang.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # HEADER
        self.tableBarang.heading("nama_barang", text="Nama")
        self.tableBarang.heading("kategori_barang", text="Kategori")
        self.tableBarang.heading("kode_barang", text="Kode")
        self.tableBarang.heading("stok", text="Stok")

        # WIDTH
        self.tableBarang.column("nama_barang", width=250)
        self.tableBarang.column("kategori_barang", width=120)
        self.tableBarang.column("kode_barang", width=120)
        self.tableBarang.column("stok", width=80)

        self.tableBarang.pack(fill=BOTH, expand=True)

        ttk.Button(container, text="← Kembali",
                command=self.admin_login).pack(pady=15)

        self.load_data_barang()

    # ===================== LOAD DATA TABLE ==========================
    def load_data_barang(self):
        for row in self.tableBarang.get_children():
            self.tableBarang.delete(row)

        data = get_barang()

        if not data:
            return

        for item in data:
            self.tableBarang.insert("", END, values=item)

    # ====================== POPUP TAMBAH BARANG ======================
    def form_add_barang(self):
        win = Toplevel(self.root)
        win.title("Tambah Barang")
        win.geometry("400x320")
        win.configure(bg="white")

        ttk.Label(win, text="Tambah Barang",
                  font=("Arial", 16, "bold")).pack(pady=10)

        frame = ttk.Frame(win)
        frame.pack(pady=10)

        ttk.Label(frame, text="Nama Barang").grid(row=0, column=0, pady=5, sticky="w")
        entry_nama = ttk.Entry(frame, width=30)
        entry_nama.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Kategori").grid(row=1, column=0, pady=5, sticky="w")
        entry_kategori = ttk.Entry(frame, width=30)
        entry_kategori.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Kode Barang").grid(row=2, column=0, pady=5, sticky="w")
        entry_kode = ttk.Entry(frame, width=30)
        entry_kode.grid(row=2, column=1, pady=5)

        def simpan():
            nama = entry_nama.get()
            kategori = entry_kategori.get()
            kode = entry_kode.get()

            if not nama or not kategori or not kode:
                messagebox.showwarning("Peringatan", "Semua field harus diisi")
                return

            insert_barang(nama, kategori, kode)
            messagebox.showinfo("Sukses", "Barang berhasil ditambahkan")
            win.destroy()
            self.load_data_barang()

        ttk.Button(win, text="Simpan", command=simpan).pack(pady=20)

    # ========================== HAPUS BARANG ==========================
    def hapus_barang(self):
        selected = self.tableBarang.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih barang terlebih dahulu")
            return

        values = self.tableBarang.item(selected, "values")
        kode_barang = values[2]

        if messagebox.askyesno(
                "Konfirmasi",
                f"Yakin ingin menghapus barang dengan kode {kode_barang}?"):

            delete_barang(kode_barang)
            messagebox.showinfo("Sukses", "Barang berhasil dihapus")
            self.load_data_barang()

    # ======================== POPUP TAMBAH STOK ======================
    def tambah_stok(self):
        selected = self.tableBarang.focus()
        if not selected:
            messagebox.showwarning("Warning", "Pilih barang dulu!")
            return

        values = self.tableBarang.item(selected, "values")

        nama = values[0]
        kode_barang = values[2]
        stok = int(values[3])

        # --- Popup Modern ---
        popup = Toplevel(self.root)
        popup.title("Tambah Stok")
        popup.geometry("350x250")
        popup.configure(bg="white")

        ttk.Label(
            popup, text="Tambah Stok",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        frame = ttk.Frame(popup, padding=10)
        frame.pack()

        ttk.Label(frame, text="Nama Barang").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Label(frame, text=nama, font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="Stok Sekarang").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(frame, text=str(stok)).grid(row=1, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="Tambah Stok").grid(row=2, column=0, sticky="w", pady=5)
        entry_tambah = ttk.Entry(frame, width=10)
        entry_tambah.grid(row=2, column=1, sticky="w", pady=5)

        def simpan():
            tambah = entry_tambah.get()
            if tambah == "":
                messagebox.showwarning("Warning", "Masukkan jumlah stok")
                return
            try:
                tambah = int(tambah)
            except ValueError:
                messagebox.showerror("Error", "Input harus angka!")
                return

            stok_baru = stok + tambah
            update_stok(kode_barang, stok_baru)
            messagebox.showinfo("Sukses", "Stok berhasil ditambah!")
            popup.destroy()
            self.lihat_barang()

        ttk.Button(popup, text="Simpan", command=simpan).pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
