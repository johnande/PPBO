class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("marsa")
print(person1.name)  

del person1

print(person1)  

