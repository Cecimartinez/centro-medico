import csv

archivo_pacientes = "pacientes.csv"

# Función para agregar un nuevo paciente al archivo pacientes.CSV
def agregar_paciente():
    try:
        with open(archivo_pacientes, mode='a', newline='') as file:
            writer = csv.writer(file)
            nombre = input("Nombre del paciente: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            genero = input("Género: ")
            direccion = input("Dirección: ")
            telefono = input("Número de teléfono: ")
            email = input("Correo electrónico (opcional): ")
            identificacion = input("Número de identificación (opcional): ")
            informacion_medica = input("Información médica relevante (alergias, condiciones, medicamentos): ")

            # Validar la fecha de nacimiento en el formato correcto
            if not fecha_nacimiento or not fecha_nacimiento.strip() or len(fecha_nacimiento) != 10:
                raise ValueError("La fecha de nacimiento debe estar en el formato YYYY-MM-DD.")

            writer.writerow([nombre, fecha_nacimiento, genero, direccion, telefono, email, identificacion, informacion_medica])

        print("Paciente agregado con éxito.")
    except Exception as e:
        print(f"Error al agregar paciente: {str(e)}")

# Función para buscar pacientes por nombre
def buscar_pacientes_por_nombre():
    try:
        with open(archivo_pacientes, mode='r') as file:
            reader = csv.reader(file)
            nombre_buscado = input("Ingrese el nombre del paciente a buscar: ")
            print("Resultados de la búsqueda:")
            for row in reader:
                if nombre_buscado.lower() in row[0].lower():
                    print(f"Nombre: {row[0]}, Fecha de Nacimiento: {row[1]}, Teléfono: {row[4]}")
    except Exception as e:
        print(f"Error al buscar pacientes: {str(e)}")

# Función para modificar la información de un paciente
def modificar_informacion_paciente():
    try:
        with open(archivo_pacientes, mode='r') as file:
            reader = csv.reader(file)
            nombre_modificar = input("Ingrese el nombre del paciente a modificar: ")
            pacientes = list(reader)

        with open(archivo_pacientes, mode='w', newline='') as file:
            writer = csv.writer(file)
            for paciente in pacientes:
                if nombre_modificar.lower() == paciente[0].lower():
                    nueva_direccion = input(f"Nueva dirección para {paciente[0]}: ")
                    nuevo_telefono = input(f"Nuevo número de teléfono para {paciente[0]}: ")
                    paciente[3] = nueva_direccion
                    paciente[4] = nuevo_telefono
                writer.writerow(paciente)
        print(f"Información de {nombre_modificar} modificada con éxito.")
    except Exception as e:
        print(f"Error al modificar información del paciente: {str(e)}")

def programar_cita():
    try:
        nombre_paciente = input("Nombre del paciente para programar la cita: ")
        fecha_cita = input("Fecha de la cita (YYYY-MM-DD): ")
        hora_cita = input("Hora de la cita: ")
        motivo_cita = input("Motivo de la cita: ")

        with open("citas.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre_paciente, fecha_cita, hora_cita, motivo_cita])
        
        print("Cita programada con éxito.")
    except Exception as e:
        print(f"Error al programar la cita: {str(e)}")


# Función para visualizar la lista de pacientes
def visualizar_lista_pacientes():
    try:
        with open(archivo_pacientes, mode='r') as file:
            reader = csv.reader(file)
            print("Lista de Pacientes:")
            for row in reader:
                print(f"Nombre: {row[0]}, Fecha de Nacimiento: {row[1]}, Teléfono: {row[4]}")
    except Exception as e:
        print(f"Error al visualizar lista de pacientes: {str(e)}")

# PROGRAMA PRINCIPAL
# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar Nuevo Paciente")
    print("2. Programar Cita Médica")
    print("3. Buscar Pacientes por Nombre")
    print("4. Modificar Información de Paciente")
    print("5. Visualizar Lista de Pacientes")
    print("6. Salir")
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        programar_cita()
    elif opcion == "3":
        buscar_pacientes_por_nombre()
    elif opcion == "4":
        modificar_informacion_paciente()
    elif opcion == "5":
        visualizar_lista_pacientes()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
