from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

# Fungsi untuk mengeluarkan suara hewan
def make_sound(animal):
    print(f"{animal.name} says {animal.sound()}")

# Membuat objek hewan
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Memanggil fungsi make_sound untuk setiap hewan
make_sound(dog)
make_sound(cat)
make_sound(cow)
