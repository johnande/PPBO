class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")

mahasiswa1 = Mahasiswa("Pasha", "123456789")
mahasiswa2 = Mahasiswa("Akmal", "987654321")

print("Informasi Mahasiswa 1:")
mahasiswa1.tampilkan_data()

print("\nInformasi Mahasiswa 2:")
mahasiswa2.tampilkan_data()
