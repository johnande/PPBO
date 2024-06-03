class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

# Membuat objek Orang dengan nama Yumna
yumna = Orang("Yumnaa", "Qurratu", "987654")

# Mengakses atribut dari objek Yumna
print("Nama:", yumna.nama_depan, yumna.nama_belakang)
print("Nomor ID Yumna:", yumna.nomor_id)

