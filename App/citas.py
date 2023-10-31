import csv
import datetime
from pacientes import archivo_pacientes

archivo_citas = "citas.csv"

# Diccionario de especialidades
especialidades = {
    1: "Médico Clínico",
    2: "Traumatología",
    3: "Gastroenterología",
    # Agregar especialidades
}

# Función para generar los turnos para una fecha específica
def generar_turnos(fecha):
    turnos = []
    for hora in range(8, 20):
        for minuto in range(0, 60, 30):
            turnos.append(f"{fecha} {hora:02d}:{minuto:02d}")
    return turnos

# Función para verificar si un turno está disponible
def turno_disponible(fecha, turno, especialidad):
    with open(archivo_citas, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == fecha and row[3] == turno and row[2] == especialidad:
                return False
    return True

# Función para programar una cita con un paciente
def programar_cita():
    try:
        identificacion_paciente = input("Número de identificación del paciente para programar la cita: ")

        # Verificar si el paciente existe
        if not paciente_existe(identificacion_paciente):
            print("El paciente no existe. Por favor, registre al paciente primero.")
            return

        # Mostrar las especialidades y obtener la elección del usuario
        print("Especialidades:")
        for numero, especialidad in especialidades.items():
            print(f"{numero}. {especialidad}")
        numero_especialidad = int(input("Seleccione la especialidad: "))
        especialidad = especialidades.get(numero_especialidad)

        if especialidad is None:
            print("Especialidad no válida. Por favor, elija una especialidad válida.")
            return

        # Pedir al usuario que ingrese una fecha
        fecha_cita = input("Fecha de la cita (YYYY-MM-DD): ")

         # Validar la fecha
        try:
            datetime.datetime.strptime(fecha_cita, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha de ingresada debe estar en el formato YYYY-MM-DD.")

        # Generar los turnos disponibles para la fecha seleccionada
        turnos = generar_turnos(fecha_cita)

        # Filtrar los turnos que ya han sido tomados para la misma especialidad
        turnos = [turno for turno in turnos if turno_disponible(fecha_cita, turno, especialidad)]

        if not turnos:
            print("No hay turnos disponibles para esta fecha y especialidad.")
            return

        # Mostrar los turnos disponibles y obtener la elección del usuario
        print("Turnos disponibles:")
        for i, turno in enumerate(turnos, start=1):
            print(f"{i}. {turno}")
        numero_turno = int(input("Seleccione el turno: "))

        if 1 <= numero_turno <= len(turnos):
            turno = turnos[numero_turno - 1]  # Obtener el turno seleccionado

            with open(archivo_citas, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([identificacion_paciente, fecha_cita, especialidad, turno])

            print("Cita programada con éxito.")
        else:
            print("Selección de turno inválida. Por favor, elija un turno válido.")
    except Exception as e:
        print(f"Error al programar la cita: {str(e)}")

# Función para verificar si el paciente existe
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
