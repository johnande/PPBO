from collections import namedtuple

def tambahkan_method_tampilkan_info(namedtuple_class):
    def decorator(cls):
        def tampilkan_info(self):
            print("Nama : ", self.nama)
            print("Nama anak : ")
            for i, anak in enumerate(self.anak, start=1):
                print(f"{i}. {anak}")

        setattr(namedtuple_class, 'tampilkan_info', tampilkan_info)
        return cls

    return decorator

Orang = namedtuple("Orang", "nama anak")

Orang = tambahkan_method_tampilkan_info(Orang)(Orang)

john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))

john.tampilkan_info()
