from abc import ABC, abstractmethod

# Product class
class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        print("Product parts:")
        for part in self.parts:
            print(part)

# Builder interface
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

# Concrete Builder class
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A1")

    def build_part_b(self):
        self.product.add_part("Part B1")

    def build_part_c(self):
        self.product.add_part("Part C1")

    def get_product(self):
        return self.product

# Director class
class Director:
    def build(self, builder):
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()

# Factory method
def get_builder(builder_type):
    if builder_type == "ConcreteBuilder":
        return ConcreteBuilder()
    else:
        raise ValueError("Invalid builder type")

# Client code
if __name__ == "__main__":
    builder_type = "ConcreteBuilder"
    builder = get_builder(builder_type)
    director = Director()

    print("Standard basic product: ")
    director.build(builder)
    product = builder.get_product()
    product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    builder = get_builder(builder_type)
    director.build(builder)
    product = builder.get_product()
    product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder = get_builder(builder_type)
    builder.build_part_a()
    builder.build_part_b()
    product = builder.get_product()
    product.list_parts()