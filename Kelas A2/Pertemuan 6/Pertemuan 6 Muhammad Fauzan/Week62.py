from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def area(self):
        return self.sisi * self.sisi

    def perimeter(self):
        return 4 * self.sisi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Membuat objek dan mengakses metode
square = Square(5)
print("Area of square:", square.area())
print("Perimeter of square:", square.perimeter())

circle = Circle(3)
print("Area dari circle:", circle.area())
print("Circumference dari circle:", circle.perimeter())