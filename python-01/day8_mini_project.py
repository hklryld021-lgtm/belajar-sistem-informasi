class mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_data(self):
        return f"{self.nama},{self.nim},{self.jurusan}"
    
def simpan_mahasiswa(mahasiswa):
    with open("data_mahasiswa.txt", "a")as file:
        file.write(mahasiswa.tampilkan_data() +"\n")


nama = input("masukan nama: ")
nim = input("masukan nim: ")
jurusan = input("masukan jurusan: ")

mhs = mahasiswa(nama, nim, jurusan)
simpan_mahasiswa(mhs)

print("data mahsiswa berhasil di simpan.")
