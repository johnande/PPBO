from collections import namedtuple

def tambahkan_metode_tampilkan_info(cls):
    def tampilkan_info(self):
        print("Nama :", self.nama)
        print("Nama anak :")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")
    cls.tampilkan_info = tampilkan_info
    return cls

# Membuat namedtuple Orang dengan decorator
@tambahkan_metode_tampilkan_info
class Orang(namedtuple("Orang", "nama anak")):
    pass

# Inisialisasi objek Orang
john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))
print()
# menambahkan anak
john.anak.append("Tina")

print(john)
print(id(john.anak))
print()
# Memanggil metode tampilkan_info
john.tampilkan_info()
