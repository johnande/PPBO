class Ana:
    def nama(self):
        print("Ana")
    def jurusan(self):
        print("TRI")

class Budi:
    def nama(self):
        print("Budi")
    def jurusan(self):
        print("TRI")

class Citra:
    def nama(self):
        print("Citra")
    def jurusan(self):
        print("TRI")

mahasiswa1 = Ana()
mahasiswa2 = Budi()
mahasiswa3 = Citra()

for mahasiswa in (mahasiswa1, mahasiswa2, mahasiswa3):
    mahasiswa.nama()
    mahasiswa.jurusan()
    print()