class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def Setor_tunai(self, jumlah):
        self.saldo += jumlah
        print("Setor tunai sebesar", jumlah, "berhasil.")
        print("Saldo saat ini:", self.saldo)

    def Tarik_tunai(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print("Tarik tunai sebesar", jumlah, "berhasil.")
            print("Saldo saat ini:", self.saldo)
        else:
            print("Saldo tidak mencukupi untuk tarik tunai sebesar", jumlah)

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo:", self.saldo)

# Membuat dua objek dari class Nasabah
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

# Simulasi transaksi ATM
print("Transaksi ATM:")
nasabah1.Setor_tunai(1000000)  # Nasabah 1 setor tunai 1.000.000
nasabah2.Tarik_tunai(1000000)   # Nasabah 2 tarik tunai 1.000.000

# Menampilkan data nasabah setelah transaksi
print("\nData Nasabah setelah transaksi:")
print("Data Nasabah 1:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2:")
nasabah2.tampilkan_data()

