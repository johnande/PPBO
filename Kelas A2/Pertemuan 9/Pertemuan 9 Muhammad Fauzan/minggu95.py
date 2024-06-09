from collections import namedtuple

def dekorator(cls):
    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak : ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")

    cls.tampilkan_info = tampilkan_info
    return cls

@dekorator
class orang(namedtuple("Orang", "nama anak")):
    pass

john = orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)
print(id(john.anak))

john.tampilkan_info()