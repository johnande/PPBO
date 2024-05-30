class Rekening:
    def __init__(self, nama, nomor_rekening, saldo):
        self.nama = nama
        self.nomor_rekening = nomor_rekening
        self.saldo = saldo

    def setor_tunai(self, total):
        self.saldo += total
        print("Setor tunai sebesar", total, "succeed.")

    def tarik_tunai(self, total):
        if self.saldo >= total:
            self.saldo -= total
            print("Tarik tunai sebesar", total, "succeed.")
        else:
            print("Saldo tidak mencukupi untuk melakukan tarik tunai.")

    def transfer(self, penerima, total):
        if self.saldo >= total:
            self.saldo -= total
            penerima.saldo += total
            print(f"Transfer sebesar {total} dari rekening {self.nomor_rekening} "
                  f"ke rekening {penerima.nomor_rekening} succeed.")
        else:
            print("Saldo tidak mencukupi untuk melakukan transfer.")

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.nomor_rekening)
        print("Saldo:", self.saldo)


# Membuat objek untuk Nasabah 1
nasabah1 = Rekening("Budi", 5555, 500000.00)

# Membuat objek untuk Nasabah 2
nasabah2 = Rekening("Wati", 6666, 2000000.00)

# Simulasi transaksi ATM
print("Transaksi ATM Bank Chan:")
nasabah1.setor_tunai(1000000)
nasabah2.tarik_tunai(1000000)

# Simulasi transaksi transfer
print("\nTransaksi Transfer:")
nasabah1.transfer(nasabah2, 500000)

# Menampilkan data nasabah setelah transaksi
print("\nData Nasabah 1 setelah transaksi:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2 setelah transaksi:")
nasabah2.tampilkan_data()

