def ubah_alamat(cls):
    def alamat_baru(self):
        return "Ini adalah alamat baru dari dekorator."

    cls.alamat_baru = alamat_baru
    return cls

@ubah_alamat
class Alamat:
    def alamat_awal(self):
        return "Ini adalah alamat awal."

rumah1 = Alamat()

print("===Kondisi 1===")
print(rumah1.alamat_awal())

print("\n===Kondisi 2===")
print(rumah1.alamat_baru())