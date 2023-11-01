import csv
import datetime
from validate_email_address import validate_email

archivo_pacientes = "pacientes.csv"

# Función para agregar un nuevo paciente al archivo pacientes.CSV
import csv
import datetime
from validate_email_address import validate_email

archivo_pacientes = "pacientes.csv"

# Función para agregar un nuevo paciente al archivo pacientes.CSV
def agregar_paciente():
    try:
        identificacion = input("Número de DNI del paciente: ")

        # Verificar si el paciente ya existe
        if paciente_existe(identificacion):
            print("El paciente con este número de identificación ya está registrado.")
            return

        with open(archivo_pacientes, mode='a', newline='') as file:
            writer = csv.writer(file)
            nombre = input("Nombre del paciente: ")
            
            fecha_nacimiento = None
            while fecha_nacimiento is None:
                fecha_nacimiento_input = input("Fecha de nacimiento (YYYY-MM-DD): ")
                try:
                    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_input, "%Y-%m-%d")
                    if fecha_nacimiento.year < 1900:
                        print("El año de nacimiento es demasiado antiguo. Por favor, ingrese una fecha válida.")
                        fecha_nacimiento = None
                except ValueError:
                    print("La fecha de nacimiento debe estar en el formato YYYY-MM-DD.")
                    fecha_nacimiento = None

            genero = input("Género: ")
            direccion = input("Dirección: ")
            telefono = input("Número de teléfono: ")

            email = input("Correo electrónico: ")
            while not validate_email(email):
                print("El formato del correo electrónico no es válido.")
                email = input("Correo electrónico: ")

            informacion_medica = input("Información médica relevante (alergias, condiciones, medicamentos): ")

            writer.writerow([nombre, fecha_nacimiento.strftime("%Y-%m-%d"), genero, direccion, telefono, email, identificacion, informacion_medica])

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
            identificacion_buscada = input("Ingrese el DNI del paciente a buscar: ")
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

# Función para verificar el número de identificación del paciente
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

