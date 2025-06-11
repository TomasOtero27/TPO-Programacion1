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
 #----------------------------------------TURNOS COMO USUARIO--------------------------------------

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



#------------------------------------BORRAR TURNOS COMO USUARIO---------------------------------
 
def borrar_turnos(archivo_turnos, archivo_turnos_disponibles, archivo_usuarios,ingreso):
    import json

    # Cargar archivos
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
        print("Usuario no encontrado.")
        return

    # Buscar turnos del usuario
    turnos_usuario = []
    for i in range(len(turnos)):
        if turnos[i]["dni"] == ingreso:
            turnos_usuario.append(i)

    if not turnos_usuario:
        print("No se encontraron turnos para ese DNI.")
        return

    print(f"\nTurnos registrados para {usuario['nombre']}:")
    for pos in range(len(turnos_usuario)):
        idx = turnos_usuario[pos]
        turno = turnos[idx]
        print(f"{pos}. Fecha: {turno['dia']} - Hora: {turno['fecha']} - Especialidad: {turno['especialidad']} - Médico: {turno['medico']}")

    try:
        seleccion = int(input("Seleccione el número del turno a eliminar: "))
        if seleccion < 0 or seleccion >= len(turnos_usuario):
            print("Selección inválida.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    indice_turno = turnos_usuario[seleccion]
    turno_a_borrar = turnos[indice_turno]

    # Restaurar el estado en turnos_disponibles usando comparación con tuplas
    for turno_disp in turnos_disponibles:
        if (
            (turno_disp["especialidad"], turno_disp["medico"], turno_disp["dia"], turno_disp["hora"]) ==
            (turno_a_borrar["especialidad"], turno_a_borrar["medico"], turno_a_borrar["dia"], turno_a_borrar["fecha"])
        ):
            turno_disp["estado"] = "disponible"
            break

    # Borrar el turno
    turnos.pop(indice_turno)

    # Guardar cambios
    with open(archivo_turnos, 'w', encoding='utf-8') as f:
        json.dump(turnos, f, ensure_ascii=False, indent=4)
    with open(archivo_turnos_disponibles, 'w', encoding='utf-8') as f:
        json.dump(turnos_disponibles, f, ensure_ascii=False, indent=4)

    print("✅ Turno eliminado y horario marcado como disponible.")
