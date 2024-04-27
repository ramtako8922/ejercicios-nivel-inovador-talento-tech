from abc import ABC, abstractmethod

# Subject (Sujeto)
class ForumTopic:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Observer (Observador)
class User(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Concrete Observer (Observador Concreto)
class Subscriber(User):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")

if __name__ == "__main__":
    topic = ForumTopic()
    user1 = Subscriber("Alice")
    user2 = Subscriber("Bob")

    topic.attach(user1)
    topic.attach(user2)

    topic.notify("New message in the forum!")
