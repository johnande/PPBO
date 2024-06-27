from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama_depan, nama_belakang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang

    @property
    def nama_lengkap(self):
        return f"{self.nama_depan} {self.nama_belakang}"

    @abstractmethod
    def dapat_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama_depan, nama_belakang, gaji):
        super().__init__(nama_depan, nama_belakang)
        self.gaji = gaji

    def dapat_gaji(self):
        return self.gaji

karyawan_tetap = KaryawanTetap("Pasha", "Akmal", 500)
print(f"Karyawan: {karyawan_tetap.nama_lengkap}")
print(f"Gaji Bulanan: ${karyawan_tetap.dapat_gaji()}")
