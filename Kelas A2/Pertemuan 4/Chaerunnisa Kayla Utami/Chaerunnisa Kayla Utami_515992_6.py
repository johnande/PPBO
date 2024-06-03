class Dosen:
    def __init__(self, status_karyawan, nama_depan, nama_belakang, nomor_id):
        self.status_karyawan = status_karyawan
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        self.matakuliah = []

    def mengajar(self, matkul):
        self.matakuliah.append(matkul)

rizki = Dosen("TETAP", "Rizki", "Setiabudi", "456789")
rizki.mengajar("Statistik")

print(f"Nama Lengkap: {rizki.nama_depan} {rizki.nama_belakang}")
print(f"Nomor ID: {rizki.nomor_id}")
print(f"Status Karyawan: {rizki.status_karyawan}")
print(f"Mata Kuliah yang Diajar: {rizki.matakuliah}")
