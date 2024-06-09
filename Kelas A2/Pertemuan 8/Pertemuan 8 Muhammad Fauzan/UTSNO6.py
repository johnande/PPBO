class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo
    

    def tampilkan_data(self):
        print("Data Nasabah:")
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo:", self.saldo)

    
    def menyetor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor tunai sebesar {jumlah} telah berhasil. Saldo sekarang yaitu: {self.saldo}")
    

    def menarik_tunai(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Tarik tunai sebesar {jumlah} telah berhasil. Saldo sekarang yaitu : {self.saldo}")
        else:
            print("Saldo tidak mencukupi untuk melakukan penarikan.")


    def transfer(self, penerima, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            penerima.saldo += jumlah
            print(f"Transfer sebesar {jumlah} dari rekening {self.no_rekening} ke rekening {penerima.no_rekening} telah berhasil.")
        else:
            print("Saldo tidak mencukupi untuk melakukan transfer.")

class Nasabah(Rekening):
    pass


# Ini Membuat dua objek Nasabah yaitu Budi dan Wati
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

# Fungsi ini Memanggil method untuk menampilkan data nasabah sebelum melakukan transaksi
print("Data Nasabah Sebelum Transaksi:")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()
print()

# Melakukan transaksi ATM sebesar
nasabah1.menyetor_tunai(1000000)
nasabah2.menarik_tunai(1000000)

# Fungsi ini Memanggil method untuk menampilkan data nasabah setelah transaksi
print("\nData Nasabah Setelah Transaksi:")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()

# Melakukan transaksi transfer sebesar
nasabah1.transfer(nasabah2, 500000)

# Fungsi ini Memanggil method untuk menampilkan data nasabah setelah transaksi
print("\nData Nasabah Setelah Transaksi:")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()