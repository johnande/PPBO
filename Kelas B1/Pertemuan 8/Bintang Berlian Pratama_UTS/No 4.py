class Rekening():
    def __init__(self, nama, norek, saldo):
        self.nama = str(nama)
        self.norek = int(norek)
        self.saldo = float(saldo)

class Nasabah(Rekening):
    def __init__(self, nama, norek, saldo):
        super().__init__(nama, norek, saldo)
    def menampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Rekening: {self.norek}")
        print(f"Saldo: {self.saldo}\n")

nasabah1 = Nasabah("Budi",5555,500000)
nasabah2 = Nasabah("Wati",6666,2000000)

print("Nasabah 1")
nasabah1.menampilkan_data()
print("Nasabah 2")
nasabah2.menampilkan_data()