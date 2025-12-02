from model import database as db
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
    @staticmethod
    def get_all_barang():
        query = "select * from barang"
        return db.fetch(query)
    def update_barang(self, kode_lama):
        query = """
        UPDATE barang
        SET nama_barang=%s,
kategori_barang=%s, kode_barang=%s
        WHERE kode_barang=%s
        """
        values = (
            self.nama_barang, 
            self.kategori_barang,
            self.kode_barang, 
            kode_lama
        )
        db.insert_data(query, values)
        @staticmethod
    def delete_barang(kode):
        query = "DELETE FROM barang WHERE kode_barang=%s"
        db.insert_data(query, [kode])



if __name__ == "__main__":
    tes = barang("TV","EK","EK0001")
    print(tes.barang())
    
    data = barang.get_all_barang()
    print("Data barang:")
    for d in data:
        print(d)
