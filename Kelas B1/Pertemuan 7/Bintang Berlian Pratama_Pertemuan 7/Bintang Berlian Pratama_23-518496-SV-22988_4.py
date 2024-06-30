def kelas_kuliah(nama_matkul):
  def kelas(self):
    self.nama_matkul = nama_matkul
    return self
  return kelas

@kelas_kuliah("Pemrograman Berorientasi Objek")
class PBO:
  def __init__(self):
    print(f"Mempelajari {self.nama_matkul}")

pbo = PBO()