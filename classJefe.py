from classEmpleado import Empleado
from classArea import Area


class Jefe(Empleado, Area):
    def __init__(self):
        # Inicializa los constructores de las clases base (Empleado y Area)
        Empleado.__init__(self)  # Inicializa la parte de Empleado
        Area.__init__(self)  # Inicializa la parte de Area (que incluye Departamento)

        self._habilidades_liderazgo = ""
        self._reportes_directos = 0
        self._estrategias_desarrolladas = ""
        self._capacitaciones_completadas = 0
        self._proyectos_dirigidos = 0
        self._dias_disponibilidad_equipo = ""
        self._indice_satisfaccion = 0

    def get_habilidades_liderazgo(self):
        return self._habilidades_liderazgo

    def set_habilidades_liderazgo(self, habilidades):
        self._habilidades_liderazgo = habilidades

    def get_reportes_directos(self):
        return self._reportes_directos

    def set_reportes_directos(self, reportes_directos):
        self._reportes_directos = reportes_directos


    def get_estrategias_desarrolladas(self):
        return self._estrategias_desarrolladas

    def set_estrategias_desarrolladas(self, estrategias):
        self._estrategias_desarrolladas = estrategias

    def get_capacitaciones_completadas(self):
        return self._capacitaciones_completadas

    def set_capacitaciones_completadas(self, capacitaciones):
        self._capacitaciones_completadas = capacitaciones

    def get_proyectos_dirigidos(self):
        return self._proyectos_dirigidos

    def set_proyectos_dirigidos(self, proyectos):
        self._proyectos_dirigidos = proyectos

    def get_dias_disponibilidad_equipo(self):
        return self._dias_disponibilidad_equipo

    def set_dias_disponibilidad_equipo(self, dias):
        self._dias_disponibilidad_equipo = dias

    def get_indice_satisfaccion(self):
        return self._indice_satisfaccion

    def set_indice_satisfaccion(self, indice):
        self._indice_satisfaccion = indice

    # En la clase Jefe
    def mostrar_Informacion_Jefe(self):
        parent1_info = super().mostrar_Informacion_Area()
        parent2_info = super().mostrar_Informacion_Empleado()
        return [
            *parent1_info,
            *parent2_info,
            f"Habilidades de Liderazgo: {self._habilidades_liderazgo}",
            f"Reportes Directos: {self._reportes_directos}",
            f"Estrategias Desarrolladas: {self._estrategias_desarrolladas}",
            f"Capacitaciones Completadas: {self._capacitaciones_completadas}",
            f"Proyectos Dirigidos: {self._proyectos_dirigidos}",
            f"Días de Disponibilidad del Equipo: {self._dias_disponibilidad_equipo}",
            f"Índice de Satisfacción: {self._indice_satisfaccion}"
        ]
