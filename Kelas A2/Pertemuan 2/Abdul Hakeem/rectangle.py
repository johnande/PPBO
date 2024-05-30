class rectangle:
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    def area(self):
        print('Area:', self.width * self.height)

    def perimeter(self):
        print('Perimeter:', 2 * (self.width + self.height))



# objects!!
rec1 = rectangle(5, 10)
rec1.area()
rec1.perimeter()