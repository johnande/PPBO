class person(object):
    def __init__(self, name) :
        self.name = name
    
    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(person):
    def isEmployee(self):
        return True

emp = person ("Slamet")
print(emp.getName (), emp.isEmployee())

emp = Employee ("Santoso")
print(emp.getName(), emp.isEmployee())