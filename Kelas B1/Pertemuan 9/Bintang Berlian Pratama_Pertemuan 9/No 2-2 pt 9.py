from collections import namedtuple

def add_tampilkan_info(cls):
    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak : ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")
    cls.tampilkan_info = tampilkan_info
    return cls

Orang = namedtuple("Orang", "nama anak")
Orang = add_tampilkan_info(Orang)

john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))

john.tampilkan_info()