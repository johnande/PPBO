class shape:
    width = 0
    def __init__(self, widht):
        self.width = widht

class square(shape):
    name = 'square'
    def area(self):
        return self.width ** 2
    
class triangle(shape):
    name = 'triangle'
    height = 0
    def __init__(self, widht, height):
        self.width = widht
        self.height = height

    def area(self):
        return self.width * self.height / 2
    
squareX = square(5)
triangleY = triangle(5, 3)

print(squareX.name, squareX.area())
print(triangleY.name, triangleY.area())

