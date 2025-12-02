from database import db

class kategori:
    def __init__(self, nama_kategori, kode_kategori):
        self.nama_kategori = nama_kategori
        self.kode_kategori = kode_kategori

    def simpan(self):
        query = "INSERT INTO kategori (nama_kategori, kode_kategori) VALUES (%s, %s)"
        values = (self.nama_kategori, self.kode_kategori)
        db.insert_data(query, values)
        print("Kategori berhasil disimpan!")

k = kategori("Elektronik", "EL001")
k.simpan()
