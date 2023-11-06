import pacientes
import citas

while True:
    print("\nMenú Principal:")
    print("1. Agregar Nuevo Paciente")
    print("2. Programar Cita Médica")
    print("3. Buscar Pacientes por DNI")
    print("4. Modificar Información de Paciente")
    print("5. Visualizar Lista de Pacientes")
    print("6. Salir")
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        pacientes.agregar_paciente()
    elif opcion == "2":
        citas.programar_cita()
    elif opcion == "3":
        pacientes.buscar_pacientes_por_identificacion()
    elif opcion == "4":
        pacientes.modificar_informacion_paciente()
    elif opcion == "5":
        pacientes.visualizar_lista_pacientes()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

