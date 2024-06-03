class Mahasiswa:
    def __init__(self, jenjang, nama_depan, nama_belakang, nomor_ID):
        self.jenjang = jenjang
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID
        self.mata_kuliah = []

    def enrol(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)

bowo = Mahasiswa("SARJANA", "Bowo", "Nugroho", "987654")
bowo.enrol("Basis Data")

print("Jenjang:", bowo.jenjang)
print("Nama Depan:", bowo.nama_depan)
print("Nama Belakang:", bowo.nama_belakang)
print("Nomor ID:", bowo.nomor_ID)
print("Mata Kuliah yang Diambil:", bowo.mata_kuliah)
