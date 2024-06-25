class HasilUjian:
    def __init__(self, nama_siswa, hasil):
        self.nama_siswa = nama_siswa
        self.hasil = hasil 

    @property
    def hasil(self):
        return self._hasil

    @hasil.setter
    def hasil(self, hasil_baru):
        if not (0 <= hasil_baru <= 100):
            raise ValueError("Score must be between 0 and 100")
        self._hasil = hasil_baru

    @classmethod
    def data(cls, data_string):
        nama_siswa, hasil = data_string.split(',')
        return cls(nama_siswa, float(hasil))

    @staticmethod
    def bila_lulus(hasil):
        return hasil >= 75

hasil1 = HasilUjian('Mala', 87)

print("hasil ujian mala:", hasil1.hasil)

hasil1.hasil = 89
print("Koreksi hasil mala:", hasil1.hasil)

hasil2 = HasilUjian.data('Tejo,80')
print("Nama siswa:", hasil2.nama_siswa)

nilai_lulus = HasilUjian.bila_lulus(70)
print("Nilai 70 apakah lulus :", nilai_lulus)