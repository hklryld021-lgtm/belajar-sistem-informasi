class mahasiswa:
    def __init__(self,nama,nim,jurusan):
        self.nama=nama
        self.nim=nim
        self.jurusan=jurusan

    def tampilkan_data(self):
        print("nama:", self.nama)
        print("nim:", self.nim)
        print("jurusan", self.jurusan)
        print("---------------")
        print("---------------")

m1 = mahasiswa("andi", "202312345", "sistem informasi")
m1.tampilkan_data()

m2 = mahasiswa("budi", "202512345", "sistem informasi")
m2.tampilkan_data()

m3 = mahasiswa("hikal", "054803236", "sistem informasi")
m3.tampilkan_data()
