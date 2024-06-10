class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo:", self.saldo)

# Membuat dua objek dari class Nasabah
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

# Memanggil method untuk menampilkan data nasabah
print("Data Nasabah 1:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2:")
nasabah2.tampilkan_data()

