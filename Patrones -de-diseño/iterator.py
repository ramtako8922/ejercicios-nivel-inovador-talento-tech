# Clase iterable
class ListaReproduccion:
    def __init__(self):
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def __iter__(self):
        return IteradorListaReproduccion(self)

# Clase iterador
class IteradorListaReproduccion:
    def __init__(self, lista_reproduccion):
        self.lista_reproduccion = lista_reproduccion
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.lista_reproduccion.canciones):
            resultado = self.lista_reproduccion.canciones[self.indice]
            self.indice += 1
            return resultado
        else:
            raise StopIteration

# Uso del patrón Iterator
lista_reproduccion = ListaReproduccion()
lista_reproduccion.agregar_cancion("Canción 1")
lista_reproduccion.agregar_cancion("Canción 2")
lista_reproduccion.agregar_cancion("Canción 3")

iterador = iter(lista_reproduccion)

for cancion in iterador:
    print(cancion)
