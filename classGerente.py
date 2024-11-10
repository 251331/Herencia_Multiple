from classEmpleado import Empleado
from classArea import Area


class Gerente(Empleado, Area):
    def __init__(self):
        # Inicializa los constructores de las clases base (Empleado y Area)
        Empleado.__init__(self)  # Inicializa la parte de Empleado
        Area.__init__(self)  # Inicializa la parte de Area (que incluye Departamento)

        self._sucursal_a_cargo = ""
        self._metas_cumplidas = 0  # Número de metas cumplidas por el gerente
        self._certificaciones = ""  # Lista de certificaciones que tiene el gerente
        self._evaluacion_desempeno = ""  # Calificación de evaluación de desempeño (ej. 1-5)

    def get_sucursal_a_cargo(self):
        return self._sucursal_a_cargo

    def set_sucursal_a_cargo(self, sucursal_a_cargo):
        self._sucursal_a_cargo = sucursal_a_cargo

    def get_metas_cumplidas(self):
        return self._metas_cumplidas

    def set_metas_cumplidas(self, metas_cumplidas):
        self._metas_cumplidas = metas_cumplidas

    def get_certificaciones(self):
        return self._certificaciones

    def set_certificaciones(self, certificaciones):
        self._certificaciones = certificaciones

    def get_evaluacion_desempeno(self):
        return self._evaluacion_desempeno

    def set_evaluacion_desempeno(self, evaluacion_desempeno):
        self._evaluacion_desempeno = evaluacion_desempeno

    # En la clase Gerente
    def mostrar_Informacion_Gerente(self):
        parent1_info = super().mostrar_Informacion_Area()
        parent2_info = super().mostrar_Informacion_Empleado()
        return [
            *parent1_info,
            *parent2_info,
            f"Sucursal a Cargo: {self._sucursal_a_cargo}",
            f"Número de Metas Cumplidas: {self._metas_cumplidas}",
            f"Numero de Certificaciones: {self._certificaciones}",
            f"Evaluación de Desempeño: {self._evaluacion_desempeno}"
        ]
