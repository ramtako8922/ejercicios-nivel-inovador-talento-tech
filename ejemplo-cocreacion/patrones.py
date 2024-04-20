from abc import ABC, abstractmethod

class ElementFactory(ABC):
    @abstractmethod
    def create_element(self):
        pass

class AreaProtegidaFactory(ElementFactory):
    def create_element(self):
        return "Área Protegida"

class EspecieFactory(ElementFactory):
    def create_element(self):
        return "Especie"

class ActividadFactory(ElementFactory):
    def create_element(self):
        return "Actividad"

# Uso del patrón Abstract Factory
area_protegida_factory = AreaProtegidaFactory()
especie_factory = EspecieFactory()
actividad_factory = ActividadFactory()

print(area_protegida_factory.create_element())
print(especie_factory.create_element())
print(actividad_factory.create_element())
