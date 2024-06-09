def add_car(cls):
    def car(self):
        print(f"Hello, This is {self.__class__.__name__} vrooommm!")

    def jenis_mobil(self):
        print(f"Nissan {self.Nissan}")
        print(f"Toyota {self.Toyota}")
        
    cls.car = car
    cls.jenis_mobil = jenis_mobil
    return cls

@add_car
class MyCar:
    def __init__(self, Nissan, Toyota):
        self.Nissan = Nissan
        self.Toyota = Toyota

obj = MyCar('GTR R34','Supra')
obj.car()
obj.jenis_mobil()
