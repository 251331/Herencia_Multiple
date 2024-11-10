from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        Persona.__init__(self)
        self._cargo = ""
        self._sueldo = 0
        self._numeronomina = ""
        self._horas_extras_gestionadas = 0
        self._nivel_estrategico = ""  # Nivel estratégico (ej. "Senior", "Ejecutivo")

    # Getter y Setter
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def get_numeronomina(self):
        return self._numeronomina

    def set_numeronomina(self, numeronomina):
        self._numeronomina = numeronomina

    def get_horas_extras_gestionadas(self):
        return self._horas_extras_gestionadas

    def set_horas_extras_gestionadas(self, horas_extras_gestionadas):
        self._horas_extras_gestionadas = horas_extras_gestionadas

    def get_nivel_estrategico(self):
        return self._nivel_estrategico

    def set_nivel_estrategico(self, nivel_estrategico):
        self._nivel_estrategico = nivel_estrategico

    # En la clase Empleado
    def mostrar_Informacion_Empleado(self):
        parent_info = super().mostrar_Informacion_Persona()
        return [
            *parent_info,
            f"Cargo: {self._cargo}",
            f"Sueldo: {self._sueldo}",
            f"Número de Nómina: {self._numeronomina}",
            f"Horas Extras Gestionadas: {self._horas_extras_gestionadas}",
            f"Nivel Estrategico: {self._nivel_estrategico}"
        ]
