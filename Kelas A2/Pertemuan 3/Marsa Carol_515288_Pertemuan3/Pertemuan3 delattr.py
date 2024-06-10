class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("marsa")
print(person1.name)  

delattr (person1, 'name')

print(person1.name)  

