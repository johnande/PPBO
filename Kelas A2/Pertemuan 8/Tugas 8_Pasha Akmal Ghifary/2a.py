class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  @classmethod
  def dari_tahun_lahir(cls, nama, tahun_lahir):
    tahun_sekarang = 2024
    umur = tahun_sekarang - tahun_lahir
    return cls(nama, umur)

  @staticmethod
  def dewasa(umur):
    return umur >= 18

  @property
  def nama_lengkap(self):
    return f"{self.nama} (umur {self.umur})"

orang1 = Orang("Budi", 25)
orang2 = Orang.dari_tahun_lahir("Ani", 2000)

print(orang1.nama, orang1.umur)  
print(orang2.nama, orang2.umur)  

print(Orang.dewasa(20))  
print(Orang.dewasa(15))  

print(orang1.nama_lengkap)  
print(orang2.nama_lengkap)  