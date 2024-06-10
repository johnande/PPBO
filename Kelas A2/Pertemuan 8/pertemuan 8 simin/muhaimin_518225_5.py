class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor tunai sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}")

    def tarik_tunai(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Tarik tunai sebesar {jumlah} berhasil. Saldo sekarang: {self.saldo}")
        else:
            print("Saldo tidak mencukupi. Transaksi tidak dapat dilakukan.")

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama Nasabah:", self.nama)
        print("Nomor Rekening:", self.no_rekening)
        print("Saldo:", self.saldo)

def main():
    nasabah1 = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    print("Data Nasabah sebelum transaksi:")
    print("Nasabah 1:")
    nasabah1.tampilkan_data()
    print()
    print("Nasabah 2:")
    nasabah2.tampilkan_data()
    print()

    # Transaksi setor tunai dan tarik tunai
    nasabah1.setor_tunai(1000000)
    nasabah2.tarik_tunai(1000000)

    print("\nData Nasabah setelah transaksi:")
    print("Nasabah 1:")
    nasabah1.tampilkan_data()
    print()
    print("Nasabah 2:")
    nasabah2.tampilkan_data()

if __name__ == "__main__":
    main()
