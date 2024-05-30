class shape:
    width = 0
    def __init__(self, width):
        self.width = width

class sq(shape):
    name = "Square"
    def get_area(self):
        return self.width ** 2
    
class tri(shape):
    name = "Triangle"
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height
    

sqx = sq(5)
triy = tri(5, 3)

print(f"luas squarex = {sqx.get_area()}")
print(f"luas triangley = {triy.get_area()}")
