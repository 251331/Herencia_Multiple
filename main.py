from classDirector import Director
from classGerente import Gerente
from classJefe import Jefe

def main():
    director = Director()
    director.set_nombre("Reyna Olivia")
    director.set_apellido("Rodriguez Morales")
    director.set_edad(35)
    director.set_cargo("Directora General")
    director.set_numeronomina("ROMA3587")
    director.set_nombre_departamento("Marketing")
    director.set_codigo_departamento("275GRZ_01008")
    director.set_ubicacion("Pachuca, Plaza juarez #75")
    director.set_presupuesto_anual("$10,000,000")
    director.set_nombre_area("Marketing")
    director.set_num_empleados(5000)
    director.set_sueldo("$11,500,000")
    director.set_region("Hidalgo")
    director.set_experiencia("10 años")
    director.set_nivel_estrategico("Nivel Estratégico (Alta Dirección)")
    director.set_reuniones_programadas("Lunes, Miercoles y Viernes")
    director.set_horas_extras_gestionadas(20)

    gerente = Gerente()
    gerente.set_nombre("Octavio Armando")
    gerente.set_apellido("Reyes Alvarez")
    gerente.set_edad(37)
    gerente.set_cargo("Alta Gerencia")
    gerente.set_numeronomina("OARA8865")
    gerente.set_nombre_departamento("Logística")
    gerente.set_codigo_departamento("5773CFV_824353")
    gerente.set_ubicacion("Pachuca, Plaza juarez #75")
    gerente.set_presupuesto_anual("$9,700,000")
    gerente.set_nombre_area("Tecnología de la Información (TI)")
    gerente.set_num_empleados(3500)
    gerente.set_sueldo("$1,800,000")
    gerente.set_sucursal_a_cargo("Apple Stores")
    gerente.set_metas_cumplidas("25")
    gerente.set_certificaciones("PMP (Project Management Professional)")
    gerente.set_evaluacion_desempeno("Exelente")
    gerente.set_horas_extras_gestionadas(55)
    gerente.set_nivel_estrategico("Nivel Táctico (Gerencia Media)")

    jefe = Jefe()
    jefe.set_nombre("Juan")
    jefe.set_apellido("Jurado Torres")
    jefe.set_edad(34)
    jefe.set_cargo("Liderazgo de Línea o Jefes de Primera Línea")
    jefe.set_numeronomina("JUTJ6573")
    jefe.set_nombre_departamento("Investigación y Desarrollo (I+D)")
    jefe.set_codigo_departamento("83856JDFX_3894123")
    jefe.set_ubicacion("Pachuca, Plaza juarez #75")
    jefe.set_presupuesto_anual("$7,300,000")
    jefe.set_nombre_area("Comunicación y Desarrollo Corporativo")
    jefe.set_num_empleados(800)
    jefe.set_sueldo("$750,000")
    jefe.set_habilidades_liderazgo("Exelente")
    jefe.set_reportes_directos("10")
    jefe.set_estrategias_desarrolladas("Expansión de Mercado")
    jefe.set_capacitaciones_completadas(20)
    jefe.set_proyectos_dirigidos(22)
    jefe.set_dias_disponibilidad_equipo("De Lunes a Sabado")
    jefe.set_indice_satisfaccion(10)
    jefe.set_horas_extras_gestionadas(47)
    jefe.set_nivel_estrategico(" Nivel Operativo (Supervisión y Ejecución)")

    # Mostrar información
    print("\nDirector")
    for item in director.mostrar_Informacion_Director():
        print(f"- {item}")

    print("\nGerente:")
    for item in gerente.mostrar_Informacion_Gerente():
        print(f"- {item}")

    print("\nJefe:")
    for item in jefe.mostrar_Informacion_Jefe():
        print(f"- {item}")

if __name__ == "__main__":
    main()