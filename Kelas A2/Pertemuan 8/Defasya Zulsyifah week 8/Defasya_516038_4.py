class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def tampilkan_data_nasabah(self):
        print("Data Nasabah:")
        print(f"Nama         : {self.nama}")
        print(f"No. Rekening : {self.no_rekening}")
        print(f"saldo        : Rp {self.saldo:, }")

def main():
    nasabah1 = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    nasabah1.tampilkan_data_nasabah()
    print()
    nasabah2. tampilkan_data_nasabah()

if __name__ == "__main__":
    main()