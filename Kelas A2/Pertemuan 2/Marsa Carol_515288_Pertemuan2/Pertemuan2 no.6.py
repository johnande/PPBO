class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)


def main():
    # Menerima input nama dan umur dari pengguna
    nama = input("Masukkan nama: ")
    umur = int(input("Masukkan umur: "))

    # Membuat objek Manusia dengan input pengguna
    manusia = Manusia(nama, umur)

    # Mencetak informasi pribadi dari manusia
    print("\nInformasi Pribadi")
    manusia.cetak_info()


if __name__ == "__main__":
    main()

