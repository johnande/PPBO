class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

class TRPL(Mahasiswa):
    def jurusan(self):
        return f"{self.nama} : Web Programming, UI/UX"

class TRI(Mahasiswa):
    def jurusan(self):
        return f"{self.nama} : Cloud Computing, Cyber Security"

class Factory:
    @staticmethod
    def daftar(jurusan, nama):
        if jurusan == "TRI":
            return TRI(nama)
        elif jurusan == "TRPL":
            return TRPL(nama)
        else:
            raise ValueError("Jurusan Tidak Ada")

# Perbaikan pemanggilan metode jurusan
mahasiswa1 = Factory.daftar("TRI", "Novi Sushmita")
print(mahasiswa1.jurusan())

mahasiswa2 = Factory.daftar("TRPL", "Bayu Nurdiansyah")
print(mahasiswa2.jurusan())