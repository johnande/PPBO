class Orang:
    def __init__(self, nama_depan, nama_belakang, no_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.no_id = no_id

# masukan nilai inutan:
nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
no_id = input("Masukkan nomer ID: ")

orang = Orang(nama_depan, nama_belakang, no_id)
print()
print("---------tampilkan hasil--------------")
print(f"Nama depan:" ,orang.nama_depan)
print(f"Nama belakang",orang.nama_belakang)
print(f"Nomer ID: " ,orang.no_id)
