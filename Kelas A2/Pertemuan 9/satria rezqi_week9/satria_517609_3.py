from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

    def volume(self):
        pass

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        return self.side * self.side
    
class Cube(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side
    
class Factory:
    @staticmethod
    def create_shape(shape, side):
        if shape == "square":
            return Square(side)
        elif shape == "cube":
            return Cube(side)
        else:
            return f"there is no {shape} shape"
        
shape1 = Factory.create_shape("square", 5)
print(f"shape1 is a part of {type(shape1).__name__} with area {shape1.area()}")


