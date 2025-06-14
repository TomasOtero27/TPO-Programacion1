from datos.datos import *
import json
from Funciones.usuarios.crud_usuarios import enmascarar_gmail,enmascarar_contraseña

def abrir_archivo(archivo):
    try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
            print("Mostrando los datos de los clientes")
            print(f'{"dni":<10}{"nombres":<20}{"contraseña":<12}{"gmail":<25}{"seguro":<20}{"activo":<20}')
            print("-" * 87)

            for usuario in usuarios:
                try:
                    dni = usuario["dni"]
                    nombre = usuario["nombre"]
                    contraseña = usuario["contraseña"]
                    gmail = usuario["gmail"]
                    seguro = usuario["seguros"]
                    if usuario["activo"] == True:
                        activo ="si"
                    else:
                        activo ="no"

                    print(f'{str(dni):<10}{nombre:<20}{contraseña:<12}{gmail:<25}{seguro:<20}{activo:<20}')
                except ValueError:
                    print("Línea con formato incorrecto")
    except (OSError,FileNotFoundError) as mensaje:
        print("Fallo todo:", mensaje)


#---------------------------------MOSTRAR MIS DATOS---------------------------
def mostrar_datos_usuarios(archivo,ingreso):
    try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        dni = [emp["dni"] for emp in usuarios]
        indice = dni.index(ingreso)
        print("Sus datos:")
        print()
        print(f"1 - Su Nombre y apellido: {usuarios[indice]["nombre"]}")
        print(f"2 - Contraseña: {enmascarar_contraseña(usuarios[indice]["contraseña"])}")
        print(f"3 - Gmail: {enmascarar_gmail(usuarios[indice]["gmail"])}")
        print(f"4- Seguro medico: {usuarios[indice]["seguros"]}")
        print("0 - Para cerrar el menú")

    except(FileNotFoundError,OSError) as error:
        print(f"Fallo todo: {error}")

#-----------------------------------------------------------------------------
#--------------------------------MIS TURNOS-----------------------------------
#----------------------------------------------------------------------------
def mostrar_turnos(archivo_turnos, archivo_usuarios,ingreso):
    # Cargar archivos
    try:
        with open(archivo_usuarios, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
        with open(archivo_turnos, "r", encoding="utf-8") as f:
            turnos = json.load(f)
    except (FileNotFoundError, OSError) as e:
        print(f"Errror de archvo: {e}")

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
    