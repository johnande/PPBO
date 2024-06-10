class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id


orang = Orang("Marsa", "Carol", 22513)

print("Nama:", orang.nama_depan, orang.nama_belakang)
print("Nomor ID:", orang.nomor_id)

