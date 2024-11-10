from classDepartamento import Departamento

class Area(Departamento):
    def __init__(self):
        Departamento.__init__(self)
        self._nombre_area = ""
        self._num_empleados = ""

    def get_nombre_area(self):
        return self._nombre_area

    def set_nombre_area(self, nombre):
        self._nombre_area = nombre

    def get_num_empleados(self):
        return self._num_empleados

    def set_num_empleados(self, num_empleados):
        self._num_empleados = num_empleados


    # En la clase Area
    def mostrar_Informacion_Area(self):
        parent_info = super().mostrar_Informacion_Departamento()
        return [
            *parent_info,
            f"Nombre del Área: {self._nombre_area}",
            f"Número de Empleados a Cargo: {self._num_empleados}"
        ]
