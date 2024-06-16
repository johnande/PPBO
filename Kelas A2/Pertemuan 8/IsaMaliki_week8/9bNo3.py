from collections import namedtuple

Orang = namedtuple("Orang", "nama anak")

john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john))

john.anak.append("Tina")

print(john)
print(id(john))

@property
def tampilkan_info(self):
    print("Nama : ", self.nama)
    print("Nama anak : ")
    for i in range (len(self.anak)):
        print(f"{i+1}. {self.anak[1]}")

Orang.tampilkan_info = tampilkan_info
john.tampilkan_info