#No4

def add_birthday_celebration(cls):
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age} years old!")

    cls.celebrate_birthday = celebrate_birthday
    return cls

@add_birthday_celebration
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Elsa", 25)

person.celebrate_birthday()
