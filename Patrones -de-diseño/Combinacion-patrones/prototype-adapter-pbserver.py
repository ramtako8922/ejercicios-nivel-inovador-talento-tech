from abc import ABC, abstractmethod
import copy

# Observer (Observador)
class Observer(ABC):
    @abstractmethod
    def update(self, document):
        pass

# Concrete Observer (Observador Concreto)
class DocumentObserver(Observer):
    def update(self, document):
        print(f"Observer received update for document '{document.title}'")

# Prototype (Prototipo)
class DocumentPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Prototype (Prototipo Concreto)
class Document(DocumentPrototype):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def clone(self):
        return copy.deepcopy(self)

# Adapter
class DocumentAdapter(DocumentPrototype):
    def __init__(self, document):
        self._document = document

    def clone(self):
        return copy.deepcopy(self._document)

# Subject (Sujeto)
class DocumentManager:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, document):
        for observer in self._observers:
            observer.update(document)

if __name__ == "__main__":
    # Crear un documento prototipo
    prototype_document = Document("Prototype Document", "Content")

    # Crear un gestor de documentos y suscribir observadores
    manager = DocumentManager()
    observer1 = DocumentObserver()
    observer2 = DocumentObserver()

    manager.attach(observer1)
    manager.attach(observer2)

    # Clonar el documento prototipo con un adaptador y notificar a los observadores
    adapter = DocumentAdapter(prototype_document)
    cloned_document = adapter.clone()
    manager.notify(cloned_document)
