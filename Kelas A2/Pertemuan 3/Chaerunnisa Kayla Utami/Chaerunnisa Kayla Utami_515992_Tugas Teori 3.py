class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Membuat objek
person1 = Person("John", 30)

# Menampilkan atribut objek sebelum dihapus
print("Sebelum penghapusan:")
print("Nama:", person1.name)
print("Umur:", person1.age)

# Menghapus atribut objek
del person1.age

# Menampilkan atribut objek setelah dihapus
print("\nSetelah penghapusan atribut 'age':")
print("Nama:", person1.name)
# Mencoba mengakses atribut yang telah dihapus akan menghasilkan AttributeError
# print("Umur:", person1.age)

# Menghapus objek itu sendiri
del person1

# Mencoba mengakses objek yang telah dihapus akan menghasilkan NameError
# print(person1)
