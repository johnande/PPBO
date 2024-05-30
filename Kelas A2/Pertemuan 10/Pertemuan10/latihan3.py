class Shape:
    def countarea(self):
        pass

class Circle(Shape):
    def countarea(self):
        r = int(input("Masukkan jari-jari lingkaran: "))
        print("Luas lingkaran adalah: ", 3.14 * r * r)

class Rectangle(Shape):
    def countarea(self):
        p = int(input("Masukkan panjang persegi panjang: "))
        l = int(input("Masukkan lebar persegi panjang: "))
        print("Luas persegi panjang adalah: ", p * l)

class Triangle(Shape):
    def countarea(self):
        a = int(input("Masukkan alas segitiga: "))
        t = int(input("Masukkan tinggi segitiga: "))
        print("Luas segitiga adalah: ", 0.5 * a * t)

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("Invalid shape type")

# Usage example
factory = ShapeFactory()
circle = factory.create_shape("circle")
rectangle = factory.create_shape("rectangle")
triangle = factory.create_shape("triangle")

circle.countarea()
rectangle.countarea()
triangle.countarea()