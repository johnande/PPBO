class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setoran tunai berhasil. Saldo Anda sekarang: Rp {self.saldo:,.2f}")

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi!")
        else:
            self.saldo -= jumlah
            print(f"Penarikan tunai berhasil. Saldo Anda sekarang: Rp {self.saldo:,.2f}")

class Nasabah(Rekening):
    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo: Rp {self.saldo:,.2f}")

nasabah1 = Nasabah("rara", 1234, 1100000)
nasabah2 = Nasabah("nada", 5678, 2000000)

print("Transaksi ATM:")
print("Nasabah 1 setor tunai Rp 1.000.000")
nasabah1.setor_tunai(1000000)

print("\nNasabah 2 tarik tunai Rp 1.000.000")
nasabah2.tarik_tunai(1000000)

print("\nData Nasabah setelah transaksi:")
print("Data Nasabah 1:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2:")
nasabah2.tampilkan_data()


