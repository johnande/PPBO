class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)
    
    @staticmethod
    def is_valid_circle(radius):
        return radius > 0


# Penggunaan class method
circle1 = Circle.from_diameter(10)
print("Circle 1 - Radius:", circle1.radius)     
print("Circle 1 - Diameter:", circle1.diameter) # 
print("Circle 1 - Area:", circle1.area)        # 

# Penggunaan static method
print(Circle.is_valid_circle(5))  
print(Circle.is_valid_circle(-2)) 

# Penggunaan property
circle2 = Circle(7)
print("Circle 2 - Radius:", circle2.radius)    
print("Circle 2 - Diameter:", circle2.diameter) 
print("Circle 2 - Area:", circle2.area)        
