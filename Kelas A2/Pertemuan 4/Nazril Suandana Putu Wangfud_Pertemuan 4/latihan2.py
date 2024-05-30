class Orang:
    def __init__(self, nama_depan, nama_belakang, no_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.no_id = no_id

class Mahasiswa(Orang):
    def __init__(self, nama_depan, nama_belakang, no_id, level):
        super().__init__(nama_depan, nama_belakang, no_id)
        self.level = level
        self.matkul = []

    def enrol(self, matkul):
        if matkul not in self.matkul:
            self.matkul.append(matkul)
    #     else:
    #         print(f"{matkul} sudah diambil sebelumnya.")

class Level(Mahasiswa):
    SARJANA = 'SARJANA'
    MASTER = 'MASTER'
    DOKTOR = 'DOKTOR'

# masukan inputan :
nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
no_id = input("Masukkan nomer ID: ")
level = input("Masukkan jenjang (SARJANA/MASTER/DOKTOR): ")
mahasiswa = Mahasiswa(nama_depan, nama_belakang, no_id, level)
matkul1 = input("Masukkan nama mata kuliah pertama: ")
matkul2 = input("Masukkan nama mata kuliah kedua: ")
mahasiswa.enrol(matkul1)
mahasiswa.enrol(matkul2)

print()
print("---------tampilkan hasil--------------")
print(f"Nama depan:" ,mahasiswa.nama_depan)
print(f"Nama belakang: ",mahasiswa.nama_belakang)
print(f"Nomer ID: ",mahasiswa.no_id)
print(f"Jenjang: ",mahasiswa.level)
print("Mata kuliah yang diambil:")
for matkul in mahasiswa.matkul:
    print(matkul)