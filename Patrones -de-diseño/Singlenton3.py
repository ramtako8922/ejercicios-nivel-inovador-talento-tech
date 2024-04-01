class RegistroUsuarios:
    _instancia = None   # Instancia única de la clase
    _usuarios = {}      # Diccionario para almacenar los usuarios registrados

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            # Si no hay una instancia existente, crea una nueva
            cls._instancia = super(RegistroUsuarios, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def registrar_usuario(self, usuario, contrasena):
        if usuario not in self._usuarios:
            # Si el usuario no está registrado, agrega el usuario y contraseña al diccionario
            self._usuarios[usuario] = contrasena
            return True
        return False

    def verificar_credenciales(self, usuario, contrasena):
        # Verifica las credenciales del usuario
        return self._usuarios.get(usuario) == contrasena

# Uso
registro_usuarios = RegistroUsuarios()
registro_usuarios.registrar_usuario('usuario1', 'contrasena1')
print(registro_usuarios.verificar_credenciales('usuario1', 'contrasena1'))  # Output: True
print(registro_usuarios.verificar_credenciales('usuario2', 'contrasena2'))  # Output: False
