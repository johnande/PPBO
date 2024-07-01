from collections import namedtuple

def tambahkan_metode_tampilkan_info(namedtuple_class):
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("Nama anak:")
        for i, anak in enumerate(self.anak, start=1):
            print(f"{i}. {anak}")

    setattr(namedtuple_class, 'tampilkan_info', tampilkan_info)
    return namedtuple_class

@tambahkan_metode_tampilkan_info
class Orang:
    def __init__(self, nama, anak):
        self.nama = nama
        self.anak = anak

john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)
print(id(john.anak))

john.tampilkan_info()
