from abc import ABC, abstractmethod
import copy

# Observer (Observador)
class Observer(ABC):
    @abstractmethod
    def update(self, package):
        pass

# Prototype (Prototipo)
class PackagePrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Prototype (Prototipo Concreto)
class Package(PackagePrototype):
    def __init__(self, tracking_number, status="Pending"):
        self.tracking_number = tracking_number
        self.status = status

    def clone(self):
        return copy.deepcopy(self)

# Concrete Observer (Observador Concreto)
class PackageObserver(Observer):
    def update(self, package):
        print(f"Package with tracking number {package.tracking_number} has status: {package.status}")

# Subject (Sujeto)
class PackageTracker:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, package):
        for observer in self._observers:
            observer.update(package)

if __name__ == "__main__":
    # Crear un paquete prototipo
    prototype_package = Package("ABC123")

    # Crear un rastreador de paquetes y suscribir observadores
    tracker = PackageTracker()
    observer1 = PackageObserver()
    observer2 = PackageObserver()

    tracker.attach(observer1)
    tracker.attach(observer2)

    # Clonar el paquete prototipo y notificar a los observadores
    cloned_package = prototype_package.clone()
    tracker.notify(cloned_package)
