# Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Factory Pattern
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            return None

class Circle:
    def draw(self):
        print("Drawing a circle")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

# Penggunaan Singleton
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True, karena keduanya adalah instance yang sama

# Penggunaan Factory
factory = ShapeFactory()
circle = factory.create_shape("circle")
rectangle = factory.create_shape("rectangle")
circle.draw()  # Output: Drawing a circle
rectangle.draw()  # Output: Drawing a rectangle
