class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama Nasabah:", self.nama)
        print("Nomor Rekening:", self.no_rekening)
        print("Saldo:", self.saldo)

def main():
    nasabah1 = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    print("Data Nasabah 1:")
    nasabah1.tampilkan_data()
    print()

    print("Data Nasabah 2:")
    nasabah2.tampilkan_data()

if __name__ == "__main__":
    main()
