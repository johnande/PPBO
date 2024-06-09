class Shape:
    width = 0
    def __init__(self, width):
        self.width = width

class Square(Shape):
    name = "Square"
    def get_area(self):
        return self.width ** 2

class Triangle(Shape):
    name = "Triangle"
    height = 0
    def __init__(self, widht, height):
        self.width = widht
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height

SquareX = Square(5)
TriangleX = Triangle(5,3)

print(f"Luas SquareX = {SquareX.get_area()}")
print(f"Luas TriangleX = {TriangleX.get_area()}")