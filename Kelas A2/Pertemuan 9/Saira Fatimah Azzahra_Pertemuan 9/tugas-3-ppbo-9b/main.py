from collections import namedtuple

def tambahkan_method_tampilkan_info(namedtuple_cls):
    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak : ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")
    namedtuple_cls.tampilkan_info = tampilkan_info
    return namedtuple_cls

@tambahkan_method_tampilkan_info
class Orang(namedtuple("Orang", "nama anak")):
    pass

# Penggunaan namedtuple yang telah dimodifikasi
john = Orang("John Doe", ["Timmy", "Jimmy"])
john.tampilkan_info()
