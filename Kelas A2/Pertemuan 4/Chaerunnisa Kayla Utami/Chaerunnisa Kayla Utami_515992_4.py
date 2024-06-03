class Karyawan:
    def __init__(self, nama, umur, jabatan, gaji):
        self.nama = nama
        self.umur = umur
        self.jabatan = jabatan
        self.gaji = gaji

# Buat kelas Dosen turunan dari kelas Karyawan
class Dosen(Karyawan):
    def __init__(self, nama, umur, jabatan, gaji):
        super().__init__(nama, umur, jabatan, gaji)
        self.matkul_diajar = []

    # Method untuk menambahkan mata kuliah yang diajar ke dalam list matkul_diajar
    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

# Contoh penggunaan
dosen1 = Dosen("Dr. John", 40, "Dosen", 10000000)
print("Nama Dosen:", dosen1.nama)
print("Umur Dosen:", dosen1.umur)
print("Jabatan Dosen:", dosen1.jabatan)
print("Gaji Dosen:", dosen1.gaji)
print("Mata Kuliah yang Diajar:", dosen1.matkul_diajar)

# Menambahkan mata kuliah yang diajar
dosen1.mengajar("Pemrograman Python")
dosen1.mengajar("Basis Data")
print("Mata Kuliah yang Diajar setelah ditambahkan:", dosen1.matkul_diajar)
