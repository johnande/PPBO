#================================================================ Soal 1 - Class Decorator
class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def fullname(self): # instance method
        # instance object accessible through self
        return "%s %s" % (self.name, self.surname)
    @property
    def fullname2(self):
        return "%s %s" % (self.name, self.surname)
 
    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]
    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
    # no parameter for class or instance object
    # we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]
jane = Person("Jane", "Smith")
print(jane.fullname())
print(jane.fullname2) # no brackets!
print(jane.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))
print(jane.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))

#================================================================ Soal 2 - Class Decorator
class Hewan:
    _jumlah_hewan = 0

    def __init__(self, nama, spesies):
        self._nama = nama
        self._spesies = spesies
        Hewan._jumlah_hewan += 1

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value):
        self._nama = value

    @classmethod
    def jumlah_hewan(cls):
        return cls._jumlah_hewan

    @staticmethod
    def suara_hewan(suara):
        return f"Hewan membuat suara: {suara}"

kucing = Hewan('Leo', 'Kucing')
print(f"Nama hewan: {kucing.nama}")
kucing.nama = 'Simba'
print(f"Nama baru hewan: {kucing.nama}")
print(f"Jumlah hewan: {Hewan.jumlah_hewan()}")
print(Hewan.suara_hewan('Meong'))


#================================================================ Soal 1 - Namedtuple
from collections import namedtuple

koordinat = namedtuple('koordinat',['x', 'y'])
titik1 = koordinat(x=2, y=4)

print(titik1[0])
print(titik1.x)
print(getattr(titik1, 'x',))

#================================================================ Soal 2 - Namedtuple
from collections import namedtuple

Orang = namedtuple("Orang", "nama anak")
john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))

#================================================================ Soal 3 - Namedtuple
from collections import namedtuple

# Mendefinisikan namedtuple 'Orang' dengan field 'nama' dan 'anak'
Orang = namedtuple('Orang', ['nama', 'anak'])

# Fungsi untuk menambahkan metode 'tampilkan_info' ke sebuah kelas
def add_tampilkan_info(cls):
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("Nama anak:")
        for i, anak in enumerate(self.anak):
            print(f"{i+1}. {anak}")
    cls.tampilkan_info = tampilkan_info
    return cls

# Menambahkan metode 'tampilkan_info' ke namedtuple 'Orang'
Orang = add_tampilkan_info(Orang)

# Membuat instance dari 'Orang'
john = Orang('John Doe', ['Jimmy', 'Tina'])

# Menampilkan informasi sebelum perubahan
print(john)
print(id(john.anak))

# Menambahkan anak baru ke list 'anak'
john = john._replace(anak=john.anak + ['Timmy'])

# Menampilkan informasi setelah perubahan
print(john)
print(id(john.anak))

# Menampilkan informasi menggunakan metode 'tampilkan_info'
john.tampilkan_info()
#================================================================ Soal 4 - Namedtuple
from collections import namedtuple

jane = {'name', 'age': 25, 'height': 1.75}
jane['age']= 26
jane['age']
jane['weight'] = 67
jane

person = namedtuple("Person", 'name age height')
jane = Person('Jane', 25, 1.75)
jane
jane.age = 26
jane.weight = 67
#================================================================ Soal 5 - Namedtuple
from collections import namedtuple

# Membuat namedtuple 'Mobil' dengan field 'merk', 'model', dan 'tahun'
Mobil = namedtuple('Mobil', 'merk model tahun')

# Membuat objek mobil
mobil_saya = Mobil(merk='Toyota', model='Corolla', tahun=2020)

# Mengakses data
print(f"Merk mobil: {mobil_saya.merk}")
print(f"Model mobil: {mobil_saya.model}")
print(f"Tahun pembuatan: {mobil_saya.tahun}")

