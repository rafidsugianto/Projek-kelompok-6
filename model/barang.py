from database import db

class barang:
    def __init__(self, nama_barang, kategori_barang, kode_barang):
        self.nama_barang = nama_barang
        self.kategori_barang = kategori_barang
        self.kode_barang = kode_barang
    
    def barang (self):
        query = "INSERT INTO barang (nama_barang, kategori_barang, kode_barang) VALUES (%s, %s, %s)"
        values = (self.nama_barang, self.kategori_barang, self.kode_barang)

        db.insert_data(query, values)
        print("Data masuk")

tes = barang("TV","EK","EK0001")
print(tes.barang())
        