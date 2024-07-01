#No2

class Gaji:
    tahun_sekarang = 2024

    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    @classmethod
    def hitung_bonus(cls, tahun_kerja):
        bonus = tahun_kerja * 1000
        return bonus

gaji_bintang = Gaji.hitung_bonus(5)
print("Menggunakan @classmethod:")
print(f"Bonus Bintang sekarang Rp {gaji_bintang}")

print()

class Gaji:
    tahun_sekarang = 2024

    @staticmethod
    def hitung_bonus(tahun_kerja):
        bonus = tahun_kerja * 1000
        return bonus

gaji_bintang = Gaji.hitung_bonus(5)
print("Menggunakan @staticmethod:")
print(f"Bonus Bintang sekarang Rp {gaji_bintang}")

print()

class Karyawan:
    def __init__(self, nama, tahun_masuk):
        self.nama = nama
        self.tahun_masuk = tahun_masuk

    @property
    def bonus(self):
        return Gaji.hitung_bonus(Gaji.tahun_sekarang - self.tahun_masuk)

bintang = Karyawan("Bintang", 2018)
print("Menggunakan @property:")
print(f"Bonus {bintang.nama} sekarang Rp {bintang.bonus}")
