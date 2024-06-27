from collections import namedtuple

Orang = namedtuple("Orang", "nama anak")
john = Orang("John Doe", ["Timmy", "Jimmy"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)
print(id(john.anak))

@property
def tampilkan_info(self):
    print("Nama:", self.nama)
    print("Nama anak:")
    for i, anak in enumerate(self.anak, 1):
        print(f"{i}. {anak}")

Orang.tampilkan_info = tampilkan_info


john.tampilkan_info

# from collections import namedtuple

# def dekor_tampilkan_info(cls):
#     def tampilkan_info(self):
#         print("Nama:", self.nama)
#         print("Nama anak:")
#         for i, anak in enumerate(self.anak, 1):
#             print(f"{i}. {anak}")

#     cls.tampilkan_info = tampilkan_info
#     return cls
# @dekor_tampilkan_info
# class Orang (namedtuple("Orang", "nama anak")):
#     pass

# john = Orang("John Doe", ["Timmy", "Jimmy"])

# print(john)
# print(id(john.anak))

# john.anak.append("Tina")

# print(john)
# print(id(john.anak))

# john.tampilkan_info()