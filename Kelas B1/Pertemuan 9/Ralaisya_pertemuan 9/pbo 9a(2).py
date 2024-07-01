class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def create_from_list(cls, data_list):
        return cls(*data_list)

data = [10, 20]
obj = MyClass.create_from_list(data)
print(obj.x, obj.y)  # Output: 10 20

