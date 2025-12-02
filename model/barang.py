from database import insert_data

class Barang:
    def __init__(self, nama_barang, kategori_barang, kode_barang):
        self.nama_barang = nama_barang
        self.kategori_barang = kategori_barang
        self.kode_barang = kode_barang

    def simpan(self):
        query = """
        INSERT INTO barang (nama_barang, kategori_barang, kode_barang)
        VALUES (%s, %s, %s)
        """
        values = (self.nama_barang, self.kategori_barang, self.kode_barang)

        insert_data(query, values)
        return "Data berhasil dimasukkan"

tes = Barang("TV", "Elektronik", "EK0001")
print(tes.simpan())