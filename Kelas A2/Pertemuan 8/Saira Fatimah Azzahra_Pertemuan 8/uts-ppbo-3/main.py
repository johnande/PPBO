from abc import ABC, abstractmethod

# Abstract Base Class (ABC) untuk orang
class Orang(ABC):
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    @abstractmethod
    def tampilkan_info(self):
        pass

# Kelas turunan pertama: Karyawan
class Karyawan(Orang):
    def __init__(self, nama, umur, gaji):
        super().__init__(nama, umur)
        self.gaji = gaji

    def tampilkan_info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Gaji: {self.gaji}"

# Kelas turunan kedua: Bos
class Bos(Orang):
    def __init__(self, nama, umur, jabatan):
        super().__init__(nama, umur)
        self.jabatan = jabatan

    def tampilkan_info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Jabatan: {self.jabatan}"

# Fungsi untuk menampilkan info orang tanpa peduli dengan tipe orangnya
def tampilkan_info_orang(orang):
    return orang.tampilkan_info()

# Penggunaan konsep polymorphism pada fungsi tampilkanInfoOrang()
karyawan = Karyawan("Budi", 30, 4000000)
bos = Bos("Ahmad", 45, "CEO")

print("Info Karyawan:", tampilkan_info_orang(karyawan))
print("Info Bos:", tampilkan_info_orang(bos))


