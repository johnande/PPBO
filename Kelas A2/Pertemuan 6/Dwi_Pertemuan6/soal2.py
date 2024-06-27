from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama, jam_kerja):
        self.nama = nama
        self.jam_kerja = jam_kerja
    @abstractmethod
    def hitung(self):
        pass

class Karyawanpanggilan(Karyawan):
    def __init__(self, nama, jam_kerja, nilai_jam):
        super().__init__(nama, jam_kerja)
        self.nilai_jam = nilai_jam
    def hitung(self):
        return self.jam_kerja * self.nilai_jam

class Karyawantetap(Karyawan):
    def __init__(self, nama, gaji):
        super().__init__(nama, None)
        self.gaji = gaji
    def hitung(self):
        return self.gaji

parttime = Karyawanpanggilan("Budi", 30, 15000)
tetap = Karyawantetap("Bambang", 2500000)

print(f"{parttime.nama} menerima gaji sebesar {parttime.hitung()} per minggu.")
print(f"{tetap.nama} menerima gaji sebesar {tetap.hitung()} per bulan.")
