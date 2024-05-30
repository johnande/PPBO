from collections import namedtuple

def decorator_tampilkan_info(cls):  
    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak : ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[1]}")
    cls.tampilkan_info = tampilkan_info
    return cls

@decorator_tampilkan_info
class Orang(namedtuple("Orang", "nama anak")):
    pass

john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)
print(id(john.anak))

john.tampilkan_info()