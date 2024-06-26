class Person(object):
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

# Membuat objek Person
emp = Person("Slamet")
print(emp.getName(), emp.isEmployee())

# Membuat objek Employee yang merupakan turunan dari Person
emp = Employee("Santoso")
print(emp.getName(), emp.isEmployee())
