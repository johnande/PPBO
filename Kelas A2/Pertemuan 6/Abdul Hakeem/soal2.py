from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height

# main program
rect = Rectangle(5, 10)
tri = Triangle(4, 6)

print("Rectangle area:", rect.area())
print("Triangle area:", tri.area())
