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

    def __init__(self, width, height):
        super().__init__(width)
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height

squareX = Square(5)
triangleY = Triangle(5, 3)

print(f"Luas {squareX.name}: {squareX.get_area()}")
print(f"Luas {triangleY.name}: {triangleY.get_area()}")
