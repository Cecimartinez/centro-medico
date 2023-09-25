import csv

archivo_pacientes = "pacientes.csv"

#agregar un nuevo paciente al archivo pacientes.CSV
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

# buscar pacientes por nombre
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

def programar_cita():
    pass

#PROGRAMA PRINCIPAL
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
