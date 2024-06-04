from collections import namedtuple

def tampilkan_info(self):
    print("Nama : ", self.nama)
    print("Nama anak : ")
    for i in range(len(self.anak)):
        print(f"{i+1}. {self.anak[i]}")

# Mendefinisikan namedtuple "Orang" dengan dua bidang,
'nama' dan 'anak'
Orang = namedtuple("Orang", "nama anak")
Orang. tampilkan_info = tampilkan_info

john = Orang("John Doe", ["Timmy", "Jimmy"])
john. tampilkan_info()