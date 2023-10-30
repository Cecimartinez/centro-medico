import csv

archivo_pacientes = "pacientes.csv"
archivo_citas = "citas.csv"


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
            email = input("Correo electrónico  ")
            identificacion = input("Número de identificación :")
            informacion_medica = input("Información médica relevante (alergias, condiciones, medicamentos): ")

            # Validar la fecha de nacimiento en el formato correcto
            if not fecha_nacimiento.strip() or len(fecha_nacimiento) != 10:
                raise ValueError("La fecha de nacimiento debe estar en el formato YYYY-MM-DD.")

            writer.writerow([nombre, fecha_nacimiento, genero, direccion, telefono, email, identificacion, informacion_medica])

        print("Paciente agregado con éxito.")
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {str(e)}")
    except (PermissionError, OSError) as e:
        print(f"Error de permisos u otro error relacionado con el archivo: {str(e)}")
    except Exception as e:
        print(f"Error al agregar paciente: {str(e)}")

# Función para buscar pacientes por número de identificación
def buscar_pacientes_por_identificacion():
    try:
        with open(archivo_pacientes, mode='r') as file:
            reader = csv.reader(file)
            identificacion_buscada = input("Ingrese el número de identificación del paciente a buscar: ")
            print("Resultados de la búsqueda:")
            for row in reader:
                if identificacion_buscada.lower() == row[6].lower():
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
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {str(e)}")
    except (PermissionError, OSError) as e:
        print(f"Error de permisos u otro error relacionado con el archivo: {str(e)}")
    except Exception as e:
        print(f"Error al modificar información del paciente: {str(e)}")

#Finción para verificar el número de identificación del paciente
def paciente_existe(identificacion_paciente):
    try:
        with open(archivo_pacientes, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if identificacion_paciente == row[6]:
                    return True
            return False
    except Exception as e:
        print(f"Error al verificar si el paciente existe: {str(e)}")

# Función para programar una cita con un paciente
def programar_cita():
    try:
        identificacion_paciente = input("Número de identificación del paciente para programar la cita: ")
        
        # Verificar si el paciente existe
        if not paciente_existe(identificacion_paciente):
            print("El paciente no existe. Por favor, registre al paciente primero.")
            return

        fecha_cita = input("Fecha de la cita (YYYY-MM-DD): ")
        hora_cita = input("Hora de la cita: ")
        motivo_cita = input("Motivo de la cita: ")

        with open(archivo_citas, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([identificacion_paciente, fecha_cita, hora_cita, motivo_cita])

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
    except FileNotFoundError as e:
        print(f"Error al abrir el archivo: {str(e)}")
    except (PermissionError, OSError) as e:
        print(f"Error de permisos u otro error relacionado con el archivo: {str(e)}")
    except Exception as e:
        print(f"Error al visualizar lista de pacientes: {str(e)}")

# PROGRAMA PRINCIPAL
# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar Nuevo Paciente")
    print("2. Programar Cita Médica")
    print("3. Buscar Pacientes por Identificación")
    print("4. Modificar Información de Paciente")
    print("5. Visualizar Lista de Pacientes")
    print("6. Salir")
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        programar_cita()
    elif opcion == "3":
        buscar_pacientes_por_identificacion()
    elif opcion == "4":
        modificar_informacion_paciente()
    elif opcion == "5":
        visualizar_lista_pacientes()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
