from abc import ABC, abstractmethod

# Interfaz para el adaptador
class Target(ABC):
    @abstractmethod
    def request(self):
        pass

# Clase concreta que será adaptada
class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request"

# Adaptador que permite a Adaptee trabajar como Target
class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adapter: {self._adaptee.specific_request()}"

# Interfaz para el builder
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

# Clase concreta del builder
class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add("Part A")

    def build_part_b(self):
        self._product.add("Part B")

    def get_result(self):
        return self._product

# Producto que se construirá usando el builder
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)

# Director que utiliza el builder para construir un producto
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request())

    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_result()
    print(f"Product parts: {product.list_parts()}")
