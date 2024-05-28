class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
class pelajar:
    def __init__(self):
        self.tambahmatkul = []
    
    def enrol (self,matkul):
        self.tambahmatkul.append(matkul)
        
class pengajar:
    def __init__ (self):
        self.matkul_diajar = []
    
    def mengajar (self,nama_matkul):
        self.matkul_diajar.append(nama_matkul)

class asdos(Orang,pelajar,pengajar):
    def __init__(self,*args):
        super().__init__(*args)
        self.tambahmatkul = []
        self.matkul_diajar = []
    
uswatun=asdos("Uswatun","Hasanah","456456")
uswatun.enrol("Bigdata")
uswatun.mengajar("Kecerdasan Artifisial")
print(uswatun.nama_depan,uswatun.nama_belakang,uswatun.nomor_id,uswatun.tambahmatkul,uswatun.matkul_diajar)
