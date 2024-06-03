class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is moving"

class Truck(Vehicle):
    def move(self):
        return "Truck is moving"

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")

factory = VehicleFactory()
car = factory.create_vehicle("car")
truck = factory.create_vehicle("truck")

print(car.move())    
print(truck.move())  