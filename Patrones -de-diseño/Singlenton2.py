class AdministradorConexiones:
    _instancia = None   # Instancia única de la clase
    _conexion = None     # Objeto de conexión a la base de datos

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            # Si no hay una instancia existente, crea una nueva
            cls._instancia = super(AdministradorConexiones, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def conectar(self, usuario, contrasena):
        if not self._conexion:
            # Si no hay una conexión existente, crea una nueva conexión
            self._conexion = self._crear_conexion(usuario, contrasena)
        return self._conexion

    def _crear_conexion(self, usuario, contrasena):
        # Lógica para crear una conexión a la base de datos
        pass

# Uso
admin_conexiones = AdministradorConexiones()
conexion1 = admin_conexiones.conectar('usuario1', 'contrasena1')
conexion2 = admin_conexiones.conectar('usuario2', 'contrasena2')
conexion3 = admin_conexiones.conectar('usuario3', 'contrasena3')
print(conexion1 is conexion3)  # Output: True (misma conexión)
