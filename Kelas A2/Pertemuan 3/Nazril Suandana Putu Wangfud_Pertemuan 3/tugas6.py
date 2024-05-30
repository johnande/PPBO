class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Nazril", 19)
print(p1.name) # Output: John

del p1 # Menghapus objek p1

try:
    print(p1.name) # Output: NameError: name 'p1' is not defined
except NameError:
    print("Object p1 telah terhapus")