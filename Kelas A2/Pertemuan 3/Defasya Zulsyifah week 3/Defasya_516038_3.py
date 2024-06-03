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
        self.width = width
        self.height = height
    
    def get_area(self):
        return 0.5 * self.width * self.height

# Membuat objek SquareX dan TriangleY
SquareX = Square(5)
TriangleY = Triangle(5, 3)

# Menampilkan luas SquareX
print("Luas SquareX:", SquareX.get_area())

# Menampilkan luas TriangleY
print("Luas TriangleY:", TriangleY.get_area())

