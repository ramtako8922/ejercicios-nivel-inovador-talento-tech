from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_info(self):
        pass

class Car(Vehicle):
    def get_info(self):
        return "This is a car."

class Motorcycle(Vehicle):
    def get_info(self):
        return "This is a motorcycle."

class Truck(Vehicle):
    def get_info(self):
        return "This is a truck."

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()

class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()

# Usage
def main():
    factories = [CarFactory(), MotorcycleFactory(), TruckFactory()]
    for factory in factories:
        vehicle = factory.create_vehicle()
        print(vehicle.get_info())

if __name__ == "__main__":
    main()
