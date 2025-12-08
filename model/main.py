from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Impor Entry standar dari tkinter untuk kontrol warna yang lebih baik
from tkinter import Entry as TkEntry 
from database import check_login, get_barang, insert_barang, delete_barang, update_stok 


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Inventory - Navy Elegance")
        self.root.geometry("1000x700")

        # --- Definisi Warna ---
        self.NAVY_DEEP = "#001f3f"      
        self.NAVY_ACCENT = "#1a4773"    
        self.NAVY_DARK_FIELD = "#0d2c54" # Latar Belakang Input (Gelap)
        self.HIGHLIGHT_BLUE = "#4a90e2" 
        self.TEXT_LIGHT = "#f0f0f0"     
        self.TEXT_WHITE = "#ffffff"     

        # --- KONFIGURASI STYLE NAVY ELEGANCE (Ttk) ---
        style = ttk.Style()
        
        # Gaya Dasar (Root)
        style.configure(".", background=self.NAVY_DEEP, foreground=self.TEXT_LIGHT) 
        
        # Gaya Judul Besar
        style.configure("Title.TLabel", font=("Arial", 25, "bold"), 
                        background=self.NAVY_DEEP, foreground=self.TEXT_WHITE)
        
        # Gaya Card
        style.configure("Card.TFrame", background=self.NAVY_ACCENT) 
        
        # Gaya Tombol
        style.configure("TButton", font=("Arial", 12), 
                        background=self.HIGHLIGHT_BLUE, 
                        foreground=self.TEXT_WHITE, 
                        relief="raised") 
        style.map("TButton", 
                  background=[("active", "#3a80c2")]) 

        # Gaya Label
        style.configure("TLabel", font=("Arial", 12), 
                        background=self.NAVY_DEEP, foreground=self.TEXT_LIGHT)
        style.configure("Card.TLabel", font=("Arial", 12), 
                        background=self.NAVY_ACCENT, foreground=self.TEXT_LIGHT)
        
        # Gaya Tabel
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), 
                        background=self.NAVY_ACCENT, foreground=self.TEXT_WHITE)
        style.configure("Treeview", 
                        background=self.NAVY_DARK_FIELD, 
                        fieldbackground=self.NAVY_DARK_FIELD, 
                        foreground=self.TEXT_LIGHT,
                        rowheight=25) 
        style.map('Treeview', 
                  background=[('selected', self.HIGHLIGHT_BLUE)],
                  foreground=[('selected', self.TEXT_WHITE)])
        # --- AKHIR KONFIGURASI STYLE ---

        self.login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_window()
        
        self.root.configure(bg=self.NAVY_DEEP)

        container = Frame(self.root, bg=self.NAVY_DEEP)
        container.pack(expand=True, fill=BOTH)

        # kiri: title
        left = Frame(container, bg=self.NAVY_DEEP)
        left.pack(side=LEFT, expand=True, fill=BOTH, padx=80, pady=50)

        ttk.Label(left, text="Data Inventory", style="Title.TLabel").pack(anchor="w")

        # kanan: card login
        right = Frame(container, bg=self.NAVY_DEEP)
        right.pack(side=RIGHT, expand=True, fill=BOTH, padx=80, pady=50)

        card = ttk.Frame(right, style="Card.TFrame") 
        card.pack(pady=20, ipadx=30, ipady=30)

        ttk.Label(card, text="Login", font=("Arial", 16, "bold"), 
                  background=self.NAVY_ACCENT, foreground=self.TEXT_WHITE).pack(pady=10) 

        # --- Bagian PENTING: Menggunakan tk.Entry (TkEntry) dengan Kontrol Warna Penuh ---
        
        # Username
        ttk.Label(card, text="Username", style="Card.TLabel").pack(anchor="w", padx=20, pady=5)
        self.entry_username = TkEntry(card, width=28, 
                                      bg=self.NAVY_DARK_FIELD, 
                                      fg=self.TEXT_WHITE, 
                                      insertbackground=self.HIGHLIGHT_BLUE, # Warna kursor
                                      relief=FLAT) # Flat border untuk tampilan modern
        self.entry_username.pack(padx=20, pady=5)

        # Password
        ttk.Label(card, text="Password", style="Card.TLabel").pack(anchor="w", padx=20, pady=5)
        self.entry_password = TkEntry(card, show="*", width=28, 
                                      bg=self.NAVY_DARK_FIELD, 
                                      fg=self.TEXT_WHITE, 
                                      insertbackground=self.HIGHLIGHT_BLUE,
                                      relief=FLAT)
        self.entry_password.pack(padx=20, pady=5)
        # --- Akhir Perbaikan Entry ---

        ttk.Button(card, text="Login", width=20, command=self.proses_login).pack(pady=15)

    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if check_login(username, password):
            messagebox.showinfo("Success", f"Login berhasil sebagai {username}")
            self.admin_login()
        else:
            messagebox.showerror("Error", "Username atau password salah")

    def admin_login(self):
        self.clear_window()
        # ... (Sama seperti sebelumnya)
        self.root.configure(bg=self.NAVY_DEEP)

        frame = Frame(self.root, bg=self.NAVY_DEEP)
        frame.pack(expand=True)

        ttk.Label(frame, text="Dashboard Admin", style="Title.TLabel").pack(pady=20)

        ttk.Button(frame, text="Manajemen Stok", width=25, command=self.lihat_barang).pack(pady=8)
        ttk.Button(frame, text="Data Barang", width=25, command=self.lihat_barang).pack(pady=8)
        ttk.Button(frame, text="Logout", width=25, command=self.login_screen).pack(pady=8)

    def lihat_barang(self):
        self.clear_window()
        # ... (Sama seperti sebelumnya)
        self.root.configure(bg=self.NAVY_DEEP)

        ttk.Label(self.root, text="Manajemen Barang", font=("Arial", 18), 
                  background=self.NAVY_DEEP, foreground=self.TEXT_LIGHT).pack(pady=10)

        button_frame = Frame(self.root, bg=self.NAVY_DEEP)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Tambah Barang", width=20, command=self.form_add_barang).pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Tambah Stok", width=20, command=self.tambah_stok).pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Hapus Barang", width=20, command=self.hapus_barang).pack(side=LEFT, padx=5)
        
        ttk.Button(self.root, text="← Kembali", width=20, command=self.admin_login).pack(pady=10)

        table_card = ttk.Frame(self.root, style="Card.TFrame") 
        table_card.pack(fill=BOTH, expand=True, padx=40, pady=20)

        container = Frame(table_card, bg=self.NAVY_DARK_FIELD)
        container.pack(fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(container, orient=VERTICAL)

        self.tableBarang = ttk.Treeview(
            container,
            columns=("nama_barang", "kategori_barang", "kode_barang", "stok"),
            show="headings",
            yscrollcommand=scrollbar.set
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

        self.tableBarang.pack(side=LEFT, fill=BOTH, expand=True)

        self.load_data_barang()

    def load_data_barang(self):
        # ... (Sama seperti sebelumnya)
        for row in self.tableBarang.get_children():
            self.tableBarang.delete(row)

        data = get_barang()

        if not data:
            return

        for item in data:
            self.tableBarang.insert("", END, values=item)

    def form_add_barang(self):
        
        win = Toplevel(self.root)
        win.title("Tambah Barang")
        win.geometry("350x300")
        win.configure(bg=self.NAVY_ACCENT)

        ttk.Label(win, text="Nama Barang", style="Card.TLabel").pack(pady=5)
        # Entry standar dengan warna eksplisit
        entry_nama = TkEntry(win, width=28, bg=self.NAVY_DARK_FIELD, fg=self.TEXT_WHITE, insertbackground=self.HIGHLIGHT_BLUE, relief=FLAT)
        entry_nama.pack()

        ttk.Label(win, text="Kategori", style="Card.TLabel").pack(pady=5)
        # Entry standar dengan warna eksplisit
        entry_kategori = TkEntry(win, width=28, bg=self.NAVY_DARK_FIELD, fg=self.TEXT_WHITE, insertbackground=self.HIGHLIGHT_BLUE, relief=FLAT)
        entry_kategori.pack()

        ttk.Label(win, text="Kode Barang", style="Card.TLabel").pack(pady=5)
        # Entry standar dengan warna eksplisit
        entry_kode = TkEntry(win, width=28, bg=self.NAVY_DARK_FIELD, fg=self.TEXT_WHITE, insertbackground=self.HIGHLIGHT_BLUE, relief=FLAT)
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
        # ... (Sama seperti sebelumnya)
        if not nama or not kategori or not kode:
            messagebox.showwarning("Peringatan", "Semua field harus diisi")
            return

        insert_barang(nama, kategori, kode)
        messagebox.showinfo("Sukses", "Barang berhasil ditambahkan")
        window.destroy()
        self.load_data_barang()

    def hapus_barang(self):
        # ... (Sama seperti sebelumnya)
        selected = self.tableBarang.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih barang terlebih dahulu")
            return

        values = self.tableBarang.item(selected, "values")
        kode_barang = values[2] 

        if messagebox.askyesno(
                "Konfirmasi",
                f"Yakin ingin menghapus barang: {values[0]} (Kode: {kode_barang})?"):

            delete_barang(kode_barang)
            messagebox.showinfo("Sukses", "Barang berhasil dihapus")
            self.load_data_barang()

    def tambah_stok(self):
        # ... (Sama seperti sebelumnya)
        selected = self.tableBarang.focus()
        if not selected:
            messagebox.showwarning("Warning", "Pilih barang dulu!")
            return

        values = self.tableBarang.item(selected, "values")
        nama = values[0]
        kode_barang = values[2]
        
        try:
            stok = int(values[3])
        except (ValueError, IndexError):
            stok = 0 

        popup = Toplevel(self.root)
        popup.title("Tambah Stok")
        popup.geometry("300x230")
        popup.configure(bg=self.NAVY_ACCENT)

        ttk.Label(popup, text="Nama Barang", style="Card.TLabel").pack(pady=5)
        ttk.Label(popup, text=nama, background=self.NAVY_ACCENT, foreground=self.TEXT_WHITE, font=("Arial", 12, "bold")).pack()

        ttk.Label(popup, text="Stok Sekarang", style="Card.TLabel").pack(pady=5)
        ttk.Label(popup, text=str(stok), background=self.NAVY_ACCENT, foreground=self.TEXT_WHITE, font=("Arial", 12, "bold")).pack()

        ttk.Label(popup, text="Tambah Stok", style="Card.TLabel").pack(pady=5)
        # Entry standar dengan warna eksplisit
        entry_tambah = TkEntry(popup, width=28, bg=self.NAVY_DARK_FIELD, fg=self.TEXT_WHITE, insertbackground=self.HIGHLIGHT_BLUE, relief=FLAT)
        entry_tambah.pack()

        def simpan():
            tambah_str = entry_tambah.get()
            if tambah_str == "":
                messagebox.showwarning("Warning", "Masukkan jumlah stok")
                return
            try:
                tambah = int(tambah_str)
            except ValueError:
                messagebox.showerror("Error", "Input harus angka!")
                return
            
            if tambah < 1:
                 messagebox.showwarning("Warning", "Jumlah stok harus positif")
                 return


            stok_baru = stok + tambah
            update_stok(kode_barang, stok_baru)
            messagebox.showinfo("Sukses", "Stok berhasil ditambah!")
            popup.destroy()
            self.load_data_barang()

        ttk.Button(popup, text="Simpan", command=simpan).pack(pady=10)
    
    def buka_data_barang(self):
        self.lihat_barang()

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()