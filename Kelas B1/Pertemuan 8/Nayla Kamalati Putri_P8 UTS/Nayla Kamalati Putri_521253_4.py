#UTS NO 4
class Nasabah:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo: Rp.", self.saldo)

def main():
    nasabah1 = Nasabah("Budi", 5555, "500.000")
    nasabah2 = Nasabah("Wati", 6666, "2.000.000")

    print("Data Nasabah 1:")
    nasabah1.tampilkan_data()
    print("\nData Nasabah 2:")
    nasabah2.tampilkan_data()

if __name__ == "__main__":
    main()
