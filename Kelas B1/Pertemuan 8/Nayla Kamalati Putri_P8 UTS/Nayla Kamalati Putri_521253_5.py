#UTS NO 5
class Nasabah:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo: Rp. {:,}".format(self.saldo))


class Rekening(Nasabah):
    def __init__(self, nama, no_rekening, saldo):
        super().__init__(nama, no_rekening, saldo)

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print("Setor tunai berhasil. Saldo Anda sekarang Rp. {:,}".format(self.saldo))

    def tarik_tunai(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print("Tarik tunai berhasil. Saldo Anda sekarang Rp. {:,}".format(self.saldo))
        else:
            print("Saldo tidak mencukupi untuk melakukan penarikan tunai.")


def main():
    nasabah1 = Rekening("Budi", 5555, 500000)
    nasabah2 = Rekening("Wati", 6666, 2000000)

    print("Data Nasabah sebelum transaksi:")
    print("\nData Nasabah 1:")
    nasabah1.tampilkan_data()
    print("\nData Nasabah 2:")
    nasabah2.tampilkan_data()

    print("=" * 30)
    print("\nTransaksi ATM:")

    print("\nSetor tunai Rp. 1.000.000 ke Nasabah 1")
    nasabah1.setor_tunai(1000000)

    print("\nTarik tunai Rp. 1.000.000 dari Nasabah 2")
    nasabah2.tarik_tunai(1000000)

    print("=" * 30)
    print("\nData Nasabah setelah transaksi:")
    print("\nData Nasabah 1:")
    nasabah1.tampilkan_data()
    print("\nData Nasabah 2:")
    nasabah2.tampilkan_data()


if __name__ == "__main__":
    main()
