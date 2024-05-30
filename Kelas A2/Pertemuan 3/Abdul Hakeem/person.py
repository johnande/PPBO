class Person(object): # CLASS
    def __init__(self,name): # CONSTRUCTOR
        self.name = name

    def getname(self):
        return self.name
    
    def isemployee(self):
        return False
    
class Employee(Person):
    def isemployee(self):
        return True
    

noemp = Person("Bees")
print(noemp.getname(), noemp.isemployee()) #using noemp for clarity
yesemp = Employee("Gees")
print(yesemp.getname(), yesemp.isemployee()) # using yesemp for clarity