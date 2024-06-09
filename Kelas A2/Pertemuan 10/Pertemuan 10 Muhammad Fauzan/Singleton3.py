# Singleton Pattern

class Singleton:
    _instance = None
    data = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_data(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data

Narasumber1 = Singleton()
Narasumber2 = Singleton()

Narasumber1.add_data("Data 1 dari Narasumber1")
Narasumber2.add_data("Data 2 dari Narasumber2")

print("Data dari Narasumber1:", Narasumber1.get_data())
print("Data dari Narasumber2:", Narasumber2.get_data())
print("Apakah mereka sama?", Narasumber1 is Narasumber2)
print()


# Factory Pattern

class Cow:
    def speak(self):
        return "Moooooooooo!"

class Goat:
    def speak(self):
        return "Mbeeeeeee!"

class AnimalFactory:
    def create(self, animal):
        if animal == 'cow':
            return Cow()
        elif animal == 'goat':
            return Goat()
        else:
            return None

factory = AnimalFactory()

cow = factory.create('cow')
goat = factory.create('goat')

print("Factory Pattern Test:")
print("Cow says:", cow.speak())
print("Goat says:", goat.speak())
