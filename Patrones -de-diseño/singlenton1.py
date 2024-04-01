class Configuracion:
    _instancia = None   # Variable estática para almacenar la única instancia de la clase
    _configuracion = {} # Diccionario para almacenar la configuración

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            # Si no hay una instancia existente, crea una nueva
            cls._instancia = super(Configuracion, cls).__new__(cls)
        return cls._instancia

    def __init__(self, configuracion=None):
        # Si se proporciona una configuración inicial, actualiza el diccionario de configuración
        if configuracion:
            self._configuracion.update(configuracion)

    def obtener_valor(self, clave):
        # Devuelve el valor correspondiente a una clave en la configuración
        return self._configuracion.get(clave)

    def establecer_valor(self, clave, valor):
        # Establece un valor para una clave en la configuración
        self._configuracion[clave] = valor

# Uso
configuracion = Configuracion({'idioma': 'es', 'tema': 'oscuro'})  # Crea una instancia de Configuracion
print(configuracion.obtener_valor('idioma'))  # Output: es
configuracion.establecer_valor('idioma', 'en')  # Establece el idioma a 'en'
print(configuracion.obtener_valor('idioma'))  # Output: en
