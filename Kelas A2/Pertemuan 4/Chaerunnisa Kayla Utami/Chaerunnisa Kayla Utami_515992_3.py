class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_ID = nomer_ID

class Karyawan(Orang):
    TETAP = "TETAP"
    TIDAK_TETAP = "TIDAK_TETAP"
    
    def __init__(self, nama_depan, nama_belakang, nomer_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_ID)
        self.status_karyawan = status_karyawan

# Contoh penggunaan
karyawan1 = Karyawan("John", "Doe", "12345", Karyawan.TETAP)
print("Nama:", karyawan1.nama_depan, karyawan1.nama_belakang)
print("Nomer ID:", karyawan1.nomer_ID)
print("Status Karyawan:", karyawan1.status_karyawan)

karyawan2 = Karyawan("Jane", "Smith", "54321", Karyawan.TIDAK_TETAP)
print("Nama:", karyawan2.nama_depan, karyawan2.nama_belakang)
print("Nomer ID:", karyawan2.nomer_ID)
print("Status Karyawan:", karyawan2.status_karyawan)
