class contohdecorator:
    def __init__(self, kelas):
        self.kelas = kelas
    def __call__(self, kelas):
        print(f"Sebelum {self.kelas.__name__}")
        objek = self.kelas(kelas)
        print(f"Sesudah {self.kelas.__name__}")
        return objek

@contohdecorator
class kelasku:
    def __init__(self, nama):
        self.nama = nama
        print(f"Membuat kelas : {self.nama}")

obj = kelasku("Isi kelas")

