class Persona:
    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        self._edad = 0

    # Getters y Setters
    def get_nombre(self):
        if self._nombre == "":
            return "La pernona no tiene un nombre"
        else:
            return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def mostrar_Informacion_Persona(self):
        return [
            f"Nombre: {self._nombre}",
            f"Apellido: {self._apellido}",
            f"Edad: {self._edad}"
        ]
