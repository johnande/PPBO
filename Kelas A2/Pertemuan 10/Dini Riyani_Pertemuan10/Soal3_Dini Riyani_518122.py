from abc import ABC, abstractmethod

# Abstract class for drinks
class Drink(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def prepare(self):
        pass

# Concrete classes for different drinks
class Coffee(Drink):
    def prepare(self):
        return f"Preparing {self.name} coffee."

class Tea(Drink):
    def prepare(self):
        return f"Preparing {self.name} tea."

# Abstract factory class
class DrinkFactory(ABC):
    @abstractmethod
    def create_drink(self, name):
        pass

# Concrete factory classes
class CoffeeFactory(DrinkFactory):
    def create_drink(self, name):
        return Coffee(name)

class TeaFactory(DrinkFactory):
    def create_drink(self, name):
        return Tea(name)

# Client code
def main():
    # Asking user for drink type
    drink_type = input("What type of drink do you want? [coffee, tea]: ").lower()

    # Asking user for drink name


    drink_name = input("Enter the name of the drink: ")

    # Creating factory based on user's choice
    if drink_type == "coffee":
        factory = CoffeeFactory()
    elif drink_type == "tea":
        factory = TeaFactory()
    else:
        print("Invalid drink type!")
        return

    # Creating the drink using the factory
    drink = factory.create_drink(drink_name)

    # Preparing the drink
    print(drink.prepare())

if __name__ == "__main__":
    main()