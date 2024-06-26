#================================================================= Tugas 2
class Person (object): 
    def __init__ (self, name): 
        self.name = name 
    def getName (self): 
        return self.name 
    def isEmployee (self): 
        return False 

class Employee (Person): 
    def isEmploye (self): 
        return True 

emp = Person("Slamet") 
print(emp.getName(), emp.isEmployee()) 

emp = Employee("Santoso") 
print(emp.getName(), emp.isEmployee()) 

#================================================================ Tugas 3
class Shape: 
    width = 0 
    def __init__ (self, width): 
        self.width = width 
class Square (Shape): 
    name = "Square" 
    def get_area(self): 
        return self.width ** 2 
class Triangle (Shape): 
    name = "Triangle" 
    height = 0 
    def __init__ (self, width, height): 
        self.width = width 
        self.height = height 
    def get_area(self): 
        return 0.5 * self.width * self.height 

SquareX = Square(5) 
print(SquareX.get_area()) 
TriangleY = Triangle(5, 3) 
print(TriangleY.get_area()) 

#================================================================ Tugas 4
class Koordinat2D: 
    x = 0 
    y = 0 
    def __init__ (self, x, y,z): 
        self.x = x  
        self.y = y  

class Koordinat3D (Koordinat2D): 
    z = 0 
    def __init__ (self, x, y, z): 
        super().__init__(x,y) 
        self.z = z  
    def tampilkan_koord (self): 
        print('x = ', self.x) 
        print('y = ', self.y) 
        print('z = ', self.z) 

titik1 = Koordinat3D (1,2,3) 
titik1.tampilkan_koord() 

#tambahkan fungsi (1)
class Koordinat2D: 
    x = 0 
    y = 0 
    def __init__ (self, x, y): 
        self.x = x  
        self.y = y  
class Koordinat3D (Koordinat2D): 
    z = 0 
    def __init__ (self, x, y, z): 
        super().__init__(x,y) 
        self.z = z  
    def tampilkan_koord (self): 
        print('x = ', self.x) 
        print('y = ', self.y) 
        print('z = ', self.z) 

titik1 = Koordinat3D (1,2,3) 
titik1.tampilkan_koord() 
 
delattr(titik1, 'z') 
print('efek fungsi delattr()') 
titik1.tampilkan_koord() 

del titik1.y  
print('efek keyword del') 
titik1.tampilkan_koord() 

#tambahkan fungsi (2)
class Koordinat2D: 
    x = 0 
    y = 0 
    def __init__ (self, x, y): 
        self.x = x  
        self.y = y  

class Koordinat3D (Koordinat2D): 
    z = 0 
    def __init__ (self, x, y, z): 
        super().__init__(x,y) 
        self.z = z  
    def tampilkan_koord (self): 
        print('x = ', self.x) 
        print('y = ', self.y) 
        print('z = ', self.z) 

titik1 = Koordinat3D (1,2,3) 
titik1.tampilkan_koord() 
 
del Koordinat2D.y 
del titik1.y   
print('efek keyword del') 
titik1.tampilkan_koord() 

#================================================================ Tugas 5
# parent class 
class Bird: 
    def __init__(self): 
        print("Bird is ready") 
    def whoisThis(self): 
        print("Bird") 
    def swim(self): 
        print("Swim faster") 
  
# child class 
class Penguin(Bird): 
    def __init__(self): 
        # call super() function 
        super().__init__() 
        print("Penguin is ready") 
    def whoisThis(self): 
        print("Penguin") 
    def run(self): 
        print("Run faster") 
 
peggy = Penguin() 
peggy.whoisThis() 
peggy.swim() 
peggy.run() 