from typing import List

# Clase que representa un automóvil
class Car:
    def __init__(self):
        self.model = ""
        self.color = ""
        self.features = []

    def set_model(self, model: str):
        self.model = model

    def set_color(self, color: str):
        self.color = color

    def add_feature(self, feature: str):
        self.features.append(feature)

    def __str__(self):
        features_str = ", ".join(self.features)
        return f"Car details:\nModel: {self.model}\nColor: {self.color}\nFeatures: {features_str}"

# Clase Builder para construir un automóvil paso a paso
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model: str):
        self.car.set_model(model)

    def set_color(self, color: str):
        self.car.set_color(color)

    def add_feature(self, feature: str):
        self.car.add_feature(feature)

    def get_car(self):
        return self.car

# Ejemplo de uso
car_builder = CarBuilder()
car_builder.set_model("SUV")
car_builder.set_color("Blue")
car_builder.add_feature("4-wheel drive")
car_builder.add_feature("Sunroof")

car = car_builder.get_car()
print(car)
