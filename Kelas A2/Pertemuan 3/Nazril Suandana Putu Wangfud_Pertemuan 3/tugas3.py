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
    
# Membuat objek SquareX dengan lebar 5
SquareX = Square(5)
print(f"Luas Square X adalah: {SquareX.get_area()}")

# Membuat objek TriangleY dengan lebar 5 dan tinggi 3
TriangleY = Triangle(5, 3)
print(f"Luas Triangle Y adalah: {TriangleY.get_area()}")