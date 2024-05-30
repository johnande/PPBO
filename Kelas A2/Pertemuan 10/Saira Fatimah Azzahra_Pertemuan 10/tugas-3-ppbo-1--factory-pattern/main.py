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
    @staticmethod
    def create_fruit(fruit_type):
        if fruit_type == "apple":
            return Apple()
        elif fruit_type == "banana":
            return Banana()
        elif fruit_type == "orange":
            return Orange()
        else:
            raise ValueError("Unknown fruit type")

# Contoh penggunaan Factory Pattern untuk membuat buah
fruit_factory = FruitFactory()
apple = fruit_factory.create_fruit("apple")
banana = fruit_factory.create_fruit("banana")
orange = fruit_factory.create_fruit("orange")

print(apple)   # Output: Apple
print(banana)  # Output: Banana
print(orange)  # Output: Orange
