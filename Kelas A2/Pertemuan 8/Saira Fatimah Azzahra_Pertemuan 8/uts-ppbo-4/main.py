class Rekening:
    def __init__(self, nama, nomor_rekening, saldo):
        self.nama = nama
        self.nomor_rekening = nomor_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.nomor_rekening)
        print("Saldo:", self.saldo)

# Membuat objek untuk Nasabah 1
nasabah1 = Nasabah("Budi", 5555, 500000.00)

# Membuat objek untuk Nasabah 2
nasabah2 = Nasabah("Wati", 6666, 2000000.00)

# Menampilkan data nasabah
print("Data Nasabah 1:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2:")
nasabah2.tampilkan_data()

