mahasiswa = {
    "nama":input("masukan nama: "),
    "nim":input("masukan nim:"),
    "jurusan":input("masukan jurusan:")
}

for key,value in mahasiswa.items():
    print(key,":",value)