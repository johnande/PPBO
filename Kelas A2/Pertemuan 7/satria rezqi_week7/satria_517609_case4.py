def car (cls):
    def intro (self):
        print(f"Hello, I am {self.name} from {self.brand}")

    def machine (self, cc, fuel, maxSpeed):
        self.cc = cc
        self.fuel = fuel
        self.maxSpeed = maxSpeed
        print(f"{self.name} has engine {self.cc} cc, it can run with max speed {self.maxSpeed} km/h, and it has capacity of fuel tank {self.fuel} Liter")

    cls.intro = intro
    cls.machine = machine
    return cls

@car
class Car:
    def __init__(self, name, brand) -> None:
        self.name = name
        self.brand = brand
    
car1 = Car("GTR", 'suzuki')
car1.intro()
car1.machine(3800, 50, 315)

car2 = Car('CRV', 'honda')
car2.intro()
car2.machine(2000, 60, 200)
