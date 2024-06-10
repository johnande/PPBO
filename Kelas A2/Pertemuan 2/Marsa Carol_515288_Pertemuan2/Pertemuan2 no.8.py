class Mahasiswa:
    def __init__(self, nama, prodi, angkatan):
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan

    def informasi(self):
        print("Nama:", self.nama)
        print("Program Studi:", self.prodi)
        print("Angkatan:", self.angkatan)


def main():
    nama = input("Masukkan nama mahasiswa: ")
    prodi = input("Masukkan program studi mahasiswa: ")
    angkatan = input("Masukkan angkatan mahasiswa: ")

    mahasiswa1 = Mahasiswa(nama, prodi, angkatan)

    print("\nInformasi Mahasiswa:")
    mahasiswa1.informasi()


if __name__ == "__main__":
    main()

