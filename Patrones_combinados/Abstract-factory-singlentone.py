import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product(self):
        pass

class SingletonFactory(AbstractFactory):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def create_product(self):
        return SingletonProduct()

class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass

class SingletonProduct(Product):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def operation(self):
        return "Singleton Product"

# Ejemplo de uso
factory = SingletonFactory()
product1 = factory.create_product()
product2 = factory.create_product()

print(product1.operation())
print(product2.operation())
print(product1 is product2)  # True, porque es la misma instancia de SingletonProduct
