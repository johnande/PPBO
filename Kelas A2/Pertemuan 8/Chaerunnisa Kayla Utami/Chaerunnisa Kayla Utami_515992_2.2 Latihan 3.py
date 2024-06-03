from collections import namedtuple

# Membuat namedtuple Orang dengan field nama dan anak
Orang = namedtuple("Orang", "nama anak")

# Definisi method tampilkan_info menggunakan @classmethod
@classmethod
def tampilkan_info(cls, self):
    print("Nama:", self.nama)
    print("Nama anak:")
    for i in range(len(self.anak)):
        print(f"{i+1}. {self.anak[i]}")

# Menambahkan method tampilkan_info ke dalam kelas namedtuple Orang
Orang.tampilkan_info = tampilkan_info

# Membuat instance namedtuple Orang dengan data John Doe dan anak-anaknya
john = Orang("John Doe", ["Timmy", "Jimmy"])

# Cetak instance namedtuple john
print(john)
print(id(john.anak))

# Menambahkan "Tina" ke dalam daftar anak-anak john
john.anak.append("Tina")

# Cetak kembali instance namedtuple john setelah penambahan "Tina"
print(john)
print(id(john.anak))

# Memanggil method tampilkan_info
Orang.tampilkan_info(john)