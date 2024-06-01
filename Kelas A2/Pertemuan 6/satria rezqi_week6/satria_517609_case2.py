from abc import ABC, abstractmethod

class Transportation (ABC):
    def __init__(self, name, launch):
        self.name = name
        self.launch = launch

    @abstractmethod
    def machine (self, cc, maxSpeed, fuel):
        pass

    @abstractmethod
    def Merk(self, merk):
        pass

class Car (Transportation):
    def machine (self, cc, maxSpeed, fuel):
        self.cc = cc
        self.maxSpeed = maxSpeed
        self.fuel = fuel
        print(f"{self.name} has Machine {self.cc} cc, it can run with max speed {self.maxSpeed} km/h, and it has capacity of fuel tank {self.fuel} Liter")

    def Merk (self, merk):
        self.merk = merk
        print(f"{self.name} is launched by {self.merk} on {self.launch}")

GTR = Car("Nissan GTR", 2023)
GTR.machine(3800, 315, 50)
GTR.Merk("Nissan")

