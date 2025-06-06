from datetime import datetime
import re
from datos.datos import *
import json

def separador():
    print("-"*50)

def realizar_turnos (turnos,datos_medicos,datos_usuarios,ingreso):
    while True:
        print(f"Entrando al Menú turnos con: {ingreso}")
        indice_ingreso = datos_usuarios[0].index(ingreso)
        print(f"Bienvenido al Menu turnos: {indice_ingreso}")

        especialidad_disponible = datos_medicos[3]

        # Mostrar especialidades
        print("Especialidades disponibles:")
        separador()
        for especialidad in especialidad_disponible:
            print(especialidad)
        separador()
        # Input especialidad
        especialidad_turno = input("Ingrese la especialidad: ")
        patron = [especialidad for especialidad in especialidad_disponible if re.search(especialidad_turno, especialidad, re.IGNORECASE)]

        if patron:
            especialidad_turno = patron[0]
            print(f"Especialidad elegida: {especialidad_turno}")

            while True:
                fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")

                if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
                    try:
                        dia = int(fecha[:2])
                        mes = int(fecha[3:5])
                        anio = int(fecha[6:])
                        fecha_valida = datetime(anio, mes, dia) 

                        if fecha_valida >= datetime.today():
                            # Guardar turno
                            turnos[0].append(ingreso)
                            turnos[1].append(indice_ingreso)
                            turnos[2].append(especialidad_turno)

                            indice = datos_medicos[3].index(especialidad_turno)
                            turnos[3].append(datos_medicos[0][indice])  # Doctor
                            turnos[4].append(fecha_valida.strftime("%d/%m/%Y"))
                            turnos[5].append(datos_medicos[4][indice])  # Costo

                            print("Turno registrado con éxito.")
                            print(f"DNI: {turnos[0][-1]}")
                            print(f"Paciente: {datos_usuarios[1][indice_ingreso]}")
                            print(f"Especialidad: {turnos[2][-1]}")
                            print(f"Doctor: {turnos[3][-1]}")
                            print(f"Fecha: {turnos[4][-1]}")
                            print(f"Costo: {turnos[5][-1]}")
                            break
                        else:
                            print("No se pueden elegir fechas anteriores a hoy")
                    except ValueError:
                        print("Error de fecha inexistente")
                else:
                    print("Formato de fecha incorrecto. Ingresar como DD/MM/AAAA")
            break
        else:
            print("Especialidad no encontrada")





def borrar_turnos(turnos,ingreso):
    while True:
        borrar_turnos_dni = int(input("Ingrese su DNI: "))  #se debe ingresar directo y elegir que turno borrar
        # Validar que el DNI se encuentre en la matriz
        if borrar_turnos_dni in turnos[0]:
            # Usamos el index con paso -1 para usar como índice el ultimo dato encontrado
            indice = len(turnos[0]) - 1 - turnos[0][::-1].index(borrar_turnos_dni)
        if ingreso in turnos[0]:
            # Usamos el index con paso -1 para usar como índice el ultimo dato encontrado
            indice = len(turnos[0]) - 1 - turnos[0][::-1].index(ingreso)
            # Eliminamos el indice de la sublista.
            for sublistas in turnos:
                sublistas.pop(indice)
            print("Último turno eliminado con éxito")
            break
        else:
                print("DNI no econtrado")


def mostrar_turnos_cliente(diccionario_turnos,ingreso):
    print(f"{'DNI':<12}{'Nombre':<20}{'Especialidad':<20}{'Doctor':<20}{'Fecha':<15}{'Precio':15}") 
    print("-" * 72)

    for i in range(len(diccionario_turnos["DNI"])):
        if diccionario_turnos["DNI"][i]== ingreso:
            print(f"{str(diccionario_turnos["DNI"][i]):<12}{diccionario_turnos["Nombre"][i]:<20}{diccionario_turnos["Especialidad"][i]:<20}{diccionario_turnos["Doctor"][i]:<20}{str(diccionario_turnos["Fecha"][i]):<15}{diccionario_turnos["Precio"][i]:<}")