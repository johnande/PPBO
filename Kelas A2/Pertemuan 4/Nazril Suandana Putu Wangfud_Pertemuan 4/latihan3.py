class Orang:
    def __init__(self, nama_depan, nama_belakang, no_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.no_id = no_id

class Karyawan(Orang):
    def __init__(self, nama_depan, nama_belakang, no_id, status):
        super().__init__(nama_depan, nama_belakang, no_id)
        self.status = status

class Level(Karyawan):
    TETAP = "TETAP"
    TDK_TETAP = "TIDAK TETAP"

# Example usage:
nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
no_id = input("Masukkan nomer ID: ")
status = input("Masukkan status karyawan (TETAP/TDK_TETAP): ")
karyawan = Karyawan(nama_depan, nama_belakang, no_id, status)

print()
print("---------tampilkan hasil--------------")
print(f"Nama depan: {karyawan.nama_depan}")
print(f"Nama belakang: {karyawan.nama_belakang}")
print(f"Nomer ID: " ,karyawan.no_id)
print(f"Status karyawan: ",karyawan.status)