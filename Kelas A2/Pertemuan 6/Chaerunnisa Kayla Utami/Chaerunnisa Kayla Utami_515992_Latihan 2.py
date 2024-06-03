from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

def main():
    # Membuat objek lingkaran dan menghitung luasnya
    circle = Circle(5)
    print("Luas Lingkaran:", circle.calculate_area())

    # Membuat objek persegi panjang dan menghitung luasnya
    rectangle = Rectangle(4, 6)
    print("Luas Persegi Panjang:", rectangle.calculate_area())

if __name__ == "__main__":
    main()