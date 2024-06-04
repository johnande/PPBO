class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai(self, jumlah):
        self.saldo += jumlah

    def tarik_tunai(self, jumlah):
        if jumlah ≤ self.saldo:
            self.saldo -= jumlah
        else:
            print("Maaf, saldo Anda tidak mencukupi untuk melakukan
transaksi ini.")

class Nasabah(Rekening):
    def tampilkan_data_nasabah(self):
        print("Data Nasabah:")
        print(f"Nama         : {self.nama}")
        print(f"No. Rekening : {self.no_rekening}")
        print(f"Saldo        : Rp {self.saldo:,}")

def main():
    nasabahi = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    print("Data Nasabah sebelum transaksi:")
    nasabahi.tampilkan_data_nasabah()
    nasabah2. tampilkan_data_nasabah()
    print()

    # Simulasi transaksi ATM
    nasabahi.setor_tunai(1000000)
    nasabah2.tarik_tunai(1000000)

    print("\nData Nasabah setelah transaksi:")
    nasabahi.tampilkan_data_nasabah()
    nasabah2.tampilkan_data_nasabah()

if __name__ == "_main_":
    main()