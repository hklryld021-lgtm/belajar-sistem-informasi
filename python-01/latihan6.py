class barang:
    def __init__(self,nama,harga,stok):
        self.nama=nama
        self.harga=harga
        self.stok=stok

    def tampilkan_info(self):
        print("nama:", self.nama)
        print("harga:", self.harga)
        print("stok:", self.stok)
        

m1 = barang("lot", "54", "1T")
m1.tampilkan_info()
        