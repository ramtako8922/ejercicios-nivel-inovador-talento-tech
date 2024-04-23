# Flyweight (Peso ligero)
class Letra:
    def __init__(self, letra):
        self.letra = letra

    def imprimir(self, fuente, tamaño):
        print(f"Letra {self.letra}, Fuente: {fuente}, Tamaño: {tamaño}")

# FlyweightFactory (Fábrica de pesos ligeros)
class LetraFactory:
    letras = {}

    @staticmethod
    def get_letra(letra):
        if letra not in LetraFactory.letras:
            LetraFactory.letras[letra] = Letra(letra)
        return LetraFactory.letras[letra]

# Cliente
letras_a = LetraFactory.get_letra('A')
letras_b = LetraFactory.get_letra('B')
letras_c = LetraFactory.get_letra('A')

letras_a.imprimir("Arial", 12)
letras_b.imprimir("Times New Roman", 14)
letras_c.imprimir("Arial", 12)

print(f"¿letras_a es letras_c? {letras_a is letras_c}")
