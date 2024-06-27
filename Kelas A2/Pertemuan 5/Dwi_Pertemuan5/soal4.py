class Pekerja:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
    def __add__(self, bonus):
            return self.gaji + bonus
    def __str__(self):
        return f"{self.nama} memiliki gaji sebesar {self.gaji}"

karyawan = Pekerja("Bambang", 5000)
gaji_akhir = karyawan + 1000
print(karyawan)
print(f"Gaji yang didapat setelah bonus: {gaji_akhir}")
