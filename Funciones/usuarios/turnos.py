from datetime import datetime
import re
from datos.datos import *
import json

def mostrar_turnos_por_especialidad(turnos_disp, especialidad):
    print(f"\nTurnos disponibles para {especialidad.upper()}:")
    print(f"{'ID':<5}{'Fecha':<15}{'Hora':<10}{'Doctor':<20}")
    print("-" * 50)
    for i in range(len(turnos_disp[0])):
        if turnos_disp[4][i].upper() == especialidad.upper():
            print(f"{turnos_disp[0][i]:<5}{turnos_disp[1][i]:<15}{turnos_disp[2][i]:<10}{turnos_disp[3][i]:<20}")
 

def realizar_turnos_usuarios(archivo_turnos, archivo_turnos_disponibles, archivo_usuarios, ingreso):

    # Cargar datos
    with open(archivo_usuarios, 'r', encoding='utf-8') as f:
        usuarios = json.load(f)
    with open(archivo_turnos_disponibles, 'r', encoding='utf-8') as f:
        turnos_disponibles = json.load(f)
    with open(archivo_turnos, 'r', encoding='utf-8') as f:
        turnos = json.load(f)

    # Buscar usuario
    usuario = ""
    for u in usuarios:
        if u["dni"] == ingreso:
            usuario = u
            break

    if usuario == "":
        print("Usuario no encontrado")
        return

    print(f"Bienvenido/a {usuario['nombre']}")

    # Mostrar especialidades disponibles
    especialidades = []
    for turno in turnos_disponibles:
        if turno["estado"] == "disponible" and turno["especialidad"] not in especialidades:
            especialidades.append(turno["especialidad"])

    print("\nEspecialidades disponibles:")
    for esp in especialidades:
        print(f"- {esp}")

    especialidad = input("Ingrese la especialidad deseada: ").strip().upper()

    # Filtrar turnos disponibles por especialidad
    turnos_filtrados = []
    for turno in turnos_disponibles:
        if turno["estado"] == "disponible" and turno["especialidad"].upper() == especialidad:
            turnos_filtrados.append(turno)

    if not turnos_filtrados:
        print("No hay turnos disponibles")
        return

    print(f"\nTurnos disponibles para {especialidad}:")
    for turno in turnos_filtrados:
        print(f"ID: {turno['id']}, Día: {turno['dia']}, Hora: {turno['hora']}, Médico: {turno['medico']}")

    try:
        id_turno = int(input("Seleccione el ID del turno a asignar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Verificar que el ID sea válido
    turno_seleccionado = ""
    for turno in turnos_filtrados:
        if turno["id"] == id_turno:
            turno_seleccionado = turno
            break

    if turno_seleccionado == "":
        print("ID no válido.")
        return

    # Marcar turno como ocupado en turnos_disponibles
    for turno in turnos_disponibles:
        if turno["id"] == id_turno:
            turno["estado"] = "ocupado"
            break

    # Crear nuevo turno y agregarlo
    nuevo_turno = {
        "dni": usuario["dni"],
        "contraseña": usuario["contraseña"],
        "nombre": usuario["nombre"],
        "especialidad": turno_seleccionado["especialidad"],
        "medico": turno_seleccionado["medico"],
        "dia": turno_seleccionado["dia"],
        "fecha": turno_seleccionado["hora"]
    }

    turnos.append(nuevo_turno)

    # Guardar cambios
    with open(archivo_turnos_disponibles, 'w', encoding='utf-8') as f:
        json.dump(turnos_disponibles, f, ensure_ascii=False, indent=4)
    with open(archivo_turnos, 'w', encoding='utf-8') as f:
        json.dump(turnos, f, ensure_ascii=False, indent=4)

    print("\n✅ Turno registrado con éxito:")
    print(f"🧾 DNI: {usuario['dni']}")
    print(f"👤 Paciente: {usuario['nombre']}")
    print(f"🩺 Especialidad: {turno_seleccionado['especialidad']}")
    print(f"👨‍⚕️ Doctor: {turno_seleccionado['medico']}")
    print(f"📅 Fecha: {turno_seleccionado['dia']}")
    print(f"⏰ Hora: {turno_seleccionado['hora']}")

#----------------------------BORRAR DATOS COMO ADMIN------------------------------------------
 
def borrar_turnos_admin(turnos, ingreso, turnos_disponibles):
    borrar_turnos_dni = int(input("Ingrese su DNI: "))
 
    # Validar que el DNI esté en la lista de turnos
    if borrar_turnos_dni not in turnos[0]:
        print("DNI no encontrado en la lista de turnos.")
        
 
    # Mostrar todos los turnos registrados por ese DNI
    print(f"\n Turnos registrados para el DNI {borrar_turnos_dni}:")
    turnos_usuario = []
    for i in range(len(turnos[0])):
        if turnos[0][i] == borrar_turnos_dni:
            print(f"{len(turnos_usuario)} - Fecha: {turnos[4][i]}, Especialidad: {turnos[2][i]}, Doctor: {turnos[3][i]}")
            turnos_usuario.append(i)
 
    # Validar si tiene turnos
    if not turnos_usuario:
        print("No se encontraron turnos para ese DNI.")
        return
 
    # Elegir qué turno borrar
    try:
        eleccion = int(input("Ingrese el número del turno que desea eliminar: "))
        if eleccion < 0 or eleccion >= len(turnos_usuario):
            print("Selección inválida.")
            return
 
        indice = turnos_usuario[eleccion]
        doctor = turnos[3][indice]
        fecha = turnos[4][indice]
        especialidad = turnos[2][indice]
 
        # Buscar la hora en los turnos disponibles para identificar el turno a restaurar
        id_turno_recuperado = None
        for i in range(len(turnos_disponibles[0])):
            if (turnos_disponibles[3][i] == doctor and
                turnos_disponibles[1][i] == fecha and
                turnos_disponibles[4][i] == especialidad):
                id_turno_recuperado = i
                break
 
        # Restaurar el estado del turno a "disponible"
        if id_turno_recuperado is not None:
            turnos_disponibles[5][id_turno_recuperado] = "disponible"
 
        # Eliminar los datos del turno del paciente
        for sublista in turnos:
            sublista.pop(indice)
 
        print("✅ Turno eliminado y marcado como disponible.")
    except ValueError:
        print("Debe ingresar un número válido.")


#------------------------------------BORRAR TURNOS COMO USUARIO---------------------------------
 
def borrar_turnos(turnos, ingreso, turnos_disponibles):
    while True:
        borrar_turnos_dni = input("Ingrese su DNI: ").strip()
 
        # Validar que el DNI esté en la lista
        if borrar_turnos_dni in turnos[0]:
            # Buscar el índice del último turno registrado con ese DNI
            indice = len(turnos[0]) - 1 - turnos[0][::-1].index(borrar_turnos_dni)
 
            # Obtener datos del turno a eliminar
            doctor = turnos[3][indice]
            fecha = turnos[4][indice]
            especialidad = turnos[2][indice]
 
            # Obtener hora del turno a eliminar buscando en turnos_disponibles
            hora = None
            for i in range(len(turnos_disponibles[0])):
                if (turnos_disponibles[3][i] == doctor and
                    turnos_disponibles[1][i] == fecha and
                    turnos_disponibles[4][i] == especialidad and
                    turnos_disponibles[5][i] == "ocupado"):  # Asegura que solo restaure lo que estaba ocupado
                    hora = turnos_disponibles[2][i]
                    break
 
            # Ahora buscar el índice exacto con doctor + fecha + hora
            id_turno_recuperado = None
            for i in range(len(turnos_disponibles[0])):
                if (turnos_disponibles[3][i] == doctor and
                    turnos_disponibles[1][i] == fecha and
                    turnos_disponibles[2][i] == hora and
                    turnos_disponibles[4][i] == especialidad):
                    id_turno_recuperado = i
                    break
 
            # Restaurar estado del turno como disponible
            if id_turno_recuperado is not None:
                turnos_disponibles[5][id_turno_recuperado] = "disponible"
 
            # Eliminar los datos del turno del paciente
            for sublista in turnos:
                sublista.pop(indice)
 
            print("Último turno eliminado con éxito y marcado como disponible.")
            break
 
        else:
            print("DNI no encontrado.")