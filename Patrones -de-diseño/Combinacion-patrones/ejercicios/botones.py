from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendered a Windows button."

class MacOSButton(Button):
    def render(self):
        return "Rendered a MacOS button."

class LinuxButton(Button):
    def render(self):
        return "Rendered a Linux button."

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

class LinuxGUIFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

# Usage
def main():
    factories = [WindowsGUIFactory(), MacOSGUIFactory(), LinuxGUIFactory()]
    for factory in factories:
        button = factory.create_button()
        print(button.render())

if __name__ == "__main__":
    main()
