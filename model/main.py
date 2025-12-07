from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import check_login, get_barang, insert_barang, delete_barang, update_stok


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Inventory")
        self.root.geometry("1000x700")
        self.login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # LOGIN SCREEN
    def login_screen(self):
        self.clear_window()

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

        if check_login(username, password):
            messagebox.showinfo("Success", f"Login berhasil sebagai {username}")
            self.admin_login()
        else:
            messagebox.showerror("Error", "Username atau password salah")

    # DASHBOARD
    def admin_login(self):
        self.clear_window()

        ttk.Label(self.root, text="Dashboard Admin", font=("Arial", 18)).pack(pady=20)

        ttk.Button(self.root,
                   text="Manajemen Stok",
                   width=20,
                   command=self.lihat_barang).pack(pady=10)
        
        ttk.Button(
                   self.root,
                   text="Data Barang",
                   width=20,
                   command=self.buka_data_barang).pack(pady=10)
        
        ttk.Button(self.root,
                   text="Logout",
                   width=20,
                   command=self.login_screen).pack(pady=10)


    # DATA BARANG
    def lihat_barang(self):
        self.clear_window()

        ttk.Label(self.root, text="Manajemen Barang", font=("Arial", 18)).pack(pady=10)

        ttk.Button(self.root,
                   text="Tambah Barang",
                   width=20,
                   command=self.form_add_barang).pack(pady=5)

        ttk.Button(self.root,
                   text="Tambah Stok",
                   width=20,
                   command=self.tambah_stok).pack(pady=5)

        ttk.Button(self.root,
                   text="Hapus Barang",
                   width=20,
                   command=self.hapus_barang).pack(pady=5)

        ttk.Button(self.root,
                   text="← Kembali",
                   width=20,
                   command=self.admin_login).pack(pady=10)

        # Table Container
        container = Frame(self.root)
        container.pack(fill=BOTH, expand=True, padx=20, pady=20)

        scrollbar = ttk.Scrollbar(container, orient=VERTICAL)

        self.tableBarang = ttk.Treeview(
            container,
            columns=("nama_barang", "kategori_barang", "kode_barang", "stok"),
            show="headings"
        )

        scrollbar.config(command=self.tableBarang.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tableBarang.heading("nama_barang", text="Nama")
        self.tableBarang.heading("kategori_barang", text="Kategori")
        self.tableBarang.heading("kode_barang", text="Kode")
        self.tableBarang.heading("stok", text="Stok")

        self.tableBarang.column("nama_barang", width=250)
        self.tableBarang.column("kategori_barang", width=100, anchor="center")
        self.tableBarang.column("kode_barang", width=150, anchor="center")
        self.tableBarang.column("stok", width=80, anchor="center")

        self.tableBarang.pack(fill=BOTH, expand=True)

        self.load_data_barang()

    def data_barang(self):
        self.clear_window()

        ttk.Label(self.root, text="Data Barang", font=("Arial", 18)).pack(pady=10)

        ttk.Button(
            self.root,
            text="← Kembali",
            width=20,
            command=self.admin_login
        ).pack(pady=10)

        # Table Container
        container = Frame(self.root)
        container.pack(fill=BOTH, expand=True, padx=20, pady=20)

        scrollbar = ttk.Scrollbar(container, orient=VERTICAL)

        self.tableBarang = ttk.Treeview(
            container,
            columns=("nama_barang", "kategori_barang", "kode_barang", "stok"),
            show="headings"
        )

        scrollbar.config(command=self.tableBarang.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tableBarang.heading("nama_barang", text="Nama")
        self.tableBarang.heading("kategori_barang", text="Kategori")
        self.tableBarang.heading("kode_barang", text="Kode")
        self.tableBarang.heading("stok", text="Stok")

        self.tableBarang.column("nama_barang", width=250)
        self.tableBarang.column("kategori_barang", width=100, anchor="center")
        self.tableBarang.column("kode_barang", width=150, anchor="center")
        self.tableBarang.column("stok", width=80, anchor="center")

        self.tableBarang.pack(fill=BOTH, expand=True)

        self.load_data_barang()


    def load_data_barang(self):
        for row in self.tableBarang.get_children():
            self.tableBarang.delete(row)

        data = get_barang()
        print("DATA DARI DATABASE:", data)  

        if not data:
            messagebox.showinfo("Info", "Data barang kosong")
            return

        for item in data:
            self.tableBarang.insert("", END, values=item)


    # ==================
    # TAMBAH BARANG
    # ==================
    def form_add_barang(self):
        win = Toplevel(self.root)
        win.title("Tambah Barang")
        win.geometry("350x300")

        ttk.Label(win, text="Nama Barang").pack(pady=5)
        entry_nama = ttk.Entry(win)
        entry_nama.pack()

        ttk.Label(win, text="Kategori").pack(pady=5)
        entry_kategori = ttk.Entry(win)
        entry_kategori.pack()

        ttk.Label(win, text="Kode Barang").pack(pady=5)
        entry_kode = ttk.Entry(win)
        entry_kode.pack()

        ttk.Button(
            win,
            text="Simpan",
            command=lambda: self.simpan_barang(
                entry_nama.get(),
                entry_kategori.get(),
                entry_kode.get(),
                win
            )
        ).pack(pady=20)

    def simpan_barang(self, nama, kategori, kode, window):
        if not nama or not kategori or not kode:
            messagebox.showwarning("Peringatan", "Semua field harus diisi")
            return

        insert_barang(nama, kategori, kode)
        messagebox.showinfo("Sukses", "Barang berhasil ditambahkan")
        window.destroy()
        self.load_data_barang()

    # ==================
    # HAPUS BARANG
    # ==================
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

    
    # TAMBAH STOK
    def tambah_stok(self):
        selected = self.tableBarang.focus()
        if not selected:
            messagebox.showwarning("Warning", "Pilih barang dulu!")
            return

        values = self.tableBarang.item(selected, "values")

        nama = values[0]
        kode_barang = values[2]

        stok = values[3] if len(values) > 3 else 0
        stok = int(stok) if stok else 0

        popup = Toplevel(self.root)
        popup.title("Tambah Stok")
        popup.geometry("300x230")

        ttk.Label(popup, text="Nama Barang").pack(pady=5)
        ttk.Label(popup, text=nama).pack()

        ttk.Label(popup, text="Stok Sekarang").pack(pady=5)
        ttk.Label(popup, text=stok).pack()

        ttk.Label(popup, text="Tambah Stok").pack(pady=5)
        entry_tambah = ttk.Entry(popup)
        entry_tambah.pack()

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
    
    def buka_data_barang(self):
        self.data_barang()

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
