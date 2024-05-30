class coords2d:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y 

class coords3d(coords2d):
    z = 0

    def __init__(self, x, y, z):
        super().__init__(x, y) #inits based on parent class
        self.z = z

    def showcoords(self):
        print(f"x = {self.x}")
        print(f"y = {self.y}")
        print(f"z = {self.z}")

point1 = coords3d(1, 2, 3)
point1.showcoords() 

#b;comment accordingly
delattr(point1, 'z')
print('delattr effect:')
point1.showcoords()

del point1.y
print('del effect:')
point1.showcoords()

#c;comment accordingly
del coords2d.y
del point1.y
print('del keyword effect:')
point1.showcoords()