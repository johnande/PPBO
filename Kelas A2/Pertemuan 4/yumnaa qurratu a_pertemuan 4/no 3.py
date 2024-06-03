class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

class Karyawan(Orang):
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"
    
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.status_karyawan = status_karyawan

karyawan1 = Karyawan("Yumnaa", "Qurratu", 292929, Karyawan.TETAP)
print("Nama:", karyawan1.nama_depan, karyawan1.nama_belakang)
print("Nomor ID:", karyawan1.nomor_id)
print("Status Karyawan:", karyawan1.status_karyawan)

