class MathOperations:
    @classmethod
    def add(cls, x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @property
    def pi(self):
        return 3.14159

print("Addition result:", MathOperations.add(5, 3))

print("Multiplication result:", MathOperations.multiply(5, 3))

math_op = MathOperations()
print("Value of pi:", math_op.pi)