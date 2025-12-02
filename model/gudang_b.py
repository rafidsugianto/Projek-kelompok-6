class GudangB:
    def __init__(self, fungsi_barang=None, kode_gudang=None):
        self.fungsi_barang = fungsi_barang
        self.kode_gudang = kode_gudang

    def tampilkan_data(self):
        print(f"Kode Gudang   : {self.kode_gudang}")
        print(f"Fungsi Barang : {self.fungsi_barang}")

    def update_data(self, fungsi_barang=None, kode_gudang=None):
        if fungsi_barang:
            self.fungsi_barang = fungsi_barang
        if kode_gudang:
            self.kode_gudang = kode_gudang

    def hapus_data(self):
        self.fungsi_barang = None
        self.kode_gudang = None
        print("Data berhasil dihapus!")
