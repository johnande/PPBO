#No5

from collections import namedtuple

Orang = namedtuple("Orang", "nama anak")

@classmethod
def tampilkan_info(cls, self):
    print("Nama:", self.nama)
    print("Nama anak:")
    for i in range(len(self.anak)):
        print(f"{i+1}. {self.anak[i]}")

Orang.tampilkan_info = tampilkan_info

john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)

print(id(john.anak))

Orang.tampilkan_info(john)
