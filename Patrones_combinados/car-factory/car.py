from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    
class SportCar(Car):
    def start(self):
        print("Sport car engine started")

class FamilyCar(Car):
    def start(self):
        print("Family car engine started")

class FlyingCar(Car):
    def start(self):
        print("Flying car engine started")
        
        from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def manufacture_car(self):
        pass
    
class SportCarFactory(CarFactory):
    def manufacture_car(self):
        return SportCar()

class FamilyCarFactory(CarFactory):
    def manufacture_car(self):
        return FamilyCar()

class FlyingCarFactory(CarFactory):
    def manufacture_car(self):
        return FlyingCar()
    
class CarShop:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.car_factory = None

    def set_car_factory(self, car_factory):
        self.car_factory = car_factory

    def manufacture_car(self):
        return self.car_factory.manufacture_car()