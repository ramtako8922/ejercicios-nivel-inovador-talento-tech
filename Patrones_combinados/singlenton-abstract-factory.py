import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA()

    def create_product_b(self):
        return ConcreteProductB()

class SingletonFactory(AbstractFactory):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def create_product_a(self):
        return SingletonProductA()

    def create_product_b(self):
        return SingletonProductB()

class ProductA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass

class ProductB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass

class ConcreteProductA(ProductA):
    def operation(self):
        return "Product A"

class ConcreteProductB(ProductB):
    def operation(self):
        return "Product B"

class SingletonProductA(ProductA):
    def operation(self):
        return "Singleton Product A"

class SingletonProductB(ProductB):
    def operation(self):
        return "Singleton Product B"

# Ejemplo de uso
factory = SingletonFactory()
product_a = factory.create_product_a()
product_b = factory.create_product_b()

print(product_a.operation())
print(product_b.operation())
