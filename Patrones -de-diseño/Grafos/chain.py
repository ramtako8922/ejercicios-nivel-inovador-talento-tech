from abc import ABC, abstractmethod

# Interfaz para las solicitudes de compra
class PurchaseRequest(ABC):
    @abstractmethod
    def amount(self):
        pass

# Interfaz para el manejador de solicitudes
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# Implementación base de PurchaseRequest
class BasePurchaseRequest(PurchaseRequest):
    def __init__(self, amount):
        self._amount = amount

    def amount(self):
        return self._amount

# Implementación base de Handler
class BaseHandler(Handler):
    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

# Clase concreta de PurchaseRequest
class PurchaseRequest500(PurchaseRequest):
    def amount(self):
        return 500

# Clase concreta de Handler
class DirectorHandler(BaseHandler):
    def handle_request(self, request):
        if request.amount() <= 1000:
            print("Director can approve the purchase")
        elif self._successor:
            self._successor.handle_request(request)

# Decorador para añadir funcionalidad adicional
class ApproverDecorator(BaseHandler):
    def __init__(self, successor, approver_name):
        super().__init__(successor)
        self._approver_name = approver_name

    def handle_request(self, request):
        print(f"{self._approver_name} is handling the request")
        if self._successor:
            self._successor.handle_request(request)

if __name__ == "__main__":
    # Configurar la cadena de responsabilidad
    director = DirectorHandler()
    manager = ApproverDecorator(director, "Manager")
    ceo = ApproverDecorator(manager, "CEO")

    # Procesar solicitudes
    request_500 = PurchaseRequest500()
    ceo.handle_request(request_500)

