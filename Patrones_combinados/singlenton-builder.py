import abc


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_part_a(self):
        pass

    @abc.abstractmethod
    def build_part_b(self):
        pass

    @abc.abstractmethod
    def get_product(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add_part("Part A")

    def build_part_b(self):
        self._product.add_part("Part B")

    def get_product(self):
        return self._product

class Product:
    def __init__(self):
        self._parts = []

    def add_part(self, part):
        self._parts.append(part)

    def list_parts(self):
        return self._parts

# Singleton Builder
class SingletonBuilder(Singleton, Builder):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add_part("Singleton Part A")

    def build_part_b(self):
        self._product.add_part("Singleton Part B")

    def get_product(self):
        return self._product

# Director
class Director:
    def construct(self, builder):
        builder.build_part_a()
        builder.build_part_b()

# Uso del patrón
director = Director()

# Usando el Builder normal
builder = ConcreteBuilder()
director.construct(builder)
product = builder.get_product()
print("Parts built by normal builder:", product.list_parts())

# Usando el Singleton Builder
singleton_builder = SingletonBuilder()
director.construct(singleton_builder)
singleton_product = singleton_builder.get_product()
print("Parts built by singleton builder:", singleton_product.list_parts())

# Verificar que es la misma instancia de SingletonBuilder
another_singleton_builder = SingletonBuilder()
print("Is the same instance of SingletonBuilder?", singleton_builder is another_singleton_builder)
