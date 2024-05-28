# Definisikan class decorator
def add_prefix(cls):
    # Definisikan class baru yang menerima parameter cls
    class NewClass:
        # Method __init__ dari class baru
        def __init__(self, name):
            self.name = name

        # Method baru yang akan menambahkan prefix "Hello, " pada attribute name
        def get_name_with_prefix(self):
            return "Hello, " + self.name

    # Kembalikan class baru yang telah didekorasi
    return NewClass

# Gunakan class decorator untuk mendekorasi class
@add_prefix
class Person:
    def __init__(self, name):
        self.name = name

# Membuat objek dari class yang telah didekorasi
person = Person("John")

# Memanggil method dari objek yang telah didekorasi
print(person.get_name_with_prefix())  # Output: Hello, John
