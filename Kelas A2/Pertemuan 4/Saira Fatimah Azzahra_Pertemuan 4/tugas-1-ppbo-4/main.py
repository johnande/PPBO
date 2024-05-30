class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        
    def tampilkan_informasi(self):
        print("Nama Anda:", self.nama_depan, self.nama_belakang)
        print("Nomor ID Anda:", self.nomor_id)
        
orang1 = Orang("Saira", "Azzahra", "518201")
orang1.tampilkan_informasi()
print()
orang2 = Orang("Malika", "Ramadani", "918919")
orang2.tampilkan_informasi()