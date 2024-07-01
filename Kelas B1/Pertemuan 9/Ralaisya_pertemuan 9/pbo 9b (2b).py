class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

# Penggunaan @property
c = Circle(5)
print(c.radius)  # Output: 5

c.radius = 10
print(c.radius)  # Output: 10

try:
    c.radius = -5  # Akan menimbulkan ValueError
except ValueError as e:
    print(e)  # Output: Radius must be positive
