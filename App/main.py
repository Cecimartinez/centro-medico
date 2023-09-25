import csv

# Definir el nombre del archivo CSV para pacientes
archivo_pacientes = "pacientes.csv"

# Función para agregar un nuevo paciente al archivo CSV
def agregar_paciente():
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
        writer.writerow([nombre, fecha_nacimiento, genero, direccion, telefono, email, identificacion, informacion_medica])
    print("Paciente agregado con éxito.")

# Función para programar una nueva cita
def programar_cita():
    pass

# Función para buscar pacientes por nombre
def buscar_pacientes_por_nombre():
    with open(archivo_pacientes, mode='r') as file:
        reader = csv.reader(file)
        nombre_buscado = input("Ingrese el nombre del paciente a buscar: ")
        print("Resultados de la búsqueda:")
        for row in reader:
            if nombre_buscado.lower() in row[0].lower():
                print(f"Nombre: {row[0]}, Fecha de Nacimiento: {row[1]}, Teléfono: {row[4]}")

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar Nuevo Paciente")
    print("2. Programar Cita Médica")
    print("3. Buscar Pacientes por Nombre")
    print("4. Salir")
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        programar_cita()
    elif opcion == "3":
        buscar_pacientes_por_nombre()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
