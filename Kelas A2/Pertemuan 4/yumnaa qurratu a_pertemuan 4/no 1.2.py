class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang

        if not (nomor_id.isdigit() or nomor_id.isnumeric()) or len(nomor_id) != 6:
            raise ValueError("Nomor ID harus berupa angka atau string dan memiliki panjang 6 digit.")
        
        self.nomor_id = nomor_id

yumnaa = Orang("Yumnaa", "Qurratu", "515239")
print("Nama:", yumnaa.nama_depan, yumnaa.nama_belakang)
print("Nomor ID Yumnaa:", yumnaa.nomor_id)
