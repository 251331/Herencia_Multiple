from classEmpleado import Empleado
from classArea import Area

class Director(Empleado, Area):
    def __init__(self):
        # Inicializa el constructor de la clase base (Empleado y Area)
        Empleado.__init__(self)  # Inicializa la parte de Empleado
        Area.__init__(self)      # Inicializa la parte de Area
        self._region = ""
        self._experiencia = ""  # Años de experiencia del director
        self._reuniones_programadas = ""

    # Getter y Setter
    def get_region(self):
        return self._region

    def set_region(self, region):
        self._region = region

    def get_experiencia(self):
        return self._experiencia

    def set_experiencia(self, experiencia):
        self._experiencia = experiencia

    def get_reuniones_programadas(self):
        return self._reuniones_programadas

    def set_reuniones_programadas(self, reuniones_programadas):
        self._reuniones_programadas = reuniones_programadas

    def mostrarInformacionregion(self):
        return f"La region asignada del director es {self._region}"

    def mostrarSueldoDirector(self):
        sueldo = super().get_sueldo()  # Corregir el acceso al sueldo
        return f"el sueldo del Director es {sueldo}"

    def mostrar_Informacion_Director(self):
        parent1_info = super().mostrar_Informacion_Area()
        parent2_info = super().mostrar_Informacion_Empleado()
        return [
            *parent1_info,
            *parent2_info,
            f"Region asignada: {self._region}",
            f"Años de Experiencia: {self._experiencia}",
            f"Días de Reuniones: {self._reuniones_programadas}"
        ]