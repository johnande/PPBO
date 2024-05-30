class Fruit:
    def __str__(self):
        pass

class Apple(Fruit):
    def __str__(self):
        return "Apple"

class Banana(Fruit):
    def __str__(self):
        return "Banana"

class Orange(Fruit):
    def __str__(self):
        return "Orange"

class FruitFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_fruit(self, fruit_type):
        if fruit_type.lower() == "apple":
            return Apple()
        elif fruit_type.lower() == "banana":
            return Banana()
        elif fruit_type.lower() == "orange":
            return Orange()
        else:
            raise ValueError("Unknown fruit type")

# Contoh penggunaan Factory Pattern untuk membuat buah
fruit_factory = FruitFactory()

apple = fruit_factory.create_fruit("Apple")
banana = fruit_factory.create_fruit("Banana")
orange = fruit_factory.create_fruit("Orange")

print(apple)   # Output: Apple
print(banana)  # Output: Banana
print(orange)  # Output: Orange

# Mengecek apakah fruit_factory merupakan singleton
fruit_factory_2 = FruitFactory()
print(fruit_factory is fruit_factory_2)  # Output: True, karena keduanya adalah instansi yang sama
