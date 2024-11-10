class Departamento:
    def __init__(self):
        self._nombre_departamento = ""
        self._codigo_departamento = ""
        self._ubicacion = ""
        self._presupuesto_anual = ""

    # Getters y Setters
    def get_nombre_departamento(self):
        return self._nombre_departamento

    def set_nombre_departamento(self, nombre_departamento):
        self._nombre_departamento = nombre_departamento

    def get_codigo_departamento(self):
        return self._codigo_departamento

    def set_codigo_departamento(self, codigo_departamento):
        self._codigo_departamento = codigo_departamento

    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def get_presupuesto_anual(self):
        return self._presupuesto_anual

    def set_presupuesto_anual(self, presupuesto_anual):
        self._presupuesto_anual = presupuesto_anual

    # En la clase Departamento
    def mostrar_Informacion_Departamento(self):
        return [
            f"Nombre del Departamento: {self._nombre_departamento}",
            f"Código de Asignacion: {self._codigo_departamento}",
            f"Ubicación: {self._ubicacion}",
            f"Presupuesto Anual: {self._presupuesto_anual}"
        ]
