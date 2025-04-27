from datetime import datetime
import re
from datos import *

fecha_ingresada = "25/04/2025"
fecha_usuario = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
fecha_actual = datetime.today()

def separador():
    print("-"*50)

def ordenar_lista_usuarios(fila):
    datos_usuarios[fila].sort()

def enmascarar_contraseña(contraseña):
    contraseña_enmascarada =  re.sub(r'.',"*", contraseña)
    return contraseña_enmascarada

def enmascarar_gmail(gmail):
    gmail_enmascarado = re.sub(r'^[^@]+', "*" * 10, gmail)
    return gmail_enmascarado
        
    
def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)

def agregar_usuarios (datos_usuarios):
    bandera = True
    while bandera:
        dni = int(input("Ingrese DNI: "))
        # Validamos el largo del DNI
        if dni < 11111111 or dni > 99999999:
            print("Numero invalido")
        else:
            # Agregamos DNI
            datos_usuarios[0].append(dni)
            print("DNI agregado")
            # Agregamos Nombre
            nombre = input("Ingrese el nombre y apellido: ")
            datos_usuarios[1].append(nombre.title())       
            print("Nombre agregado")
            # Agregamos Contraseña
            contraseña_agregar=input("Ingrese la contraseña: ")
            datos_usuarios[2].append(contraseña_agregar)
            print("Contraseña agregada")
            # Agregamos Correo
            correo = input("Ingrese su correo: ")
            datos_usuarios[3].append(correo)

            print("Usuario creado con éxito")
            bandera = False



def realizar_turnos (turnos,datos_medicos,datos_usuarios):
    bandera_turnos = True
    while bandera_turnos:
            dni = int(input("Ingrese su DNI: "))
            if dni in datos_usuarios[0]:
            # Separamos especialidad de su matriz
                especialidad_disponible = datos_medicos[2]
            # Mostrar especalidades
                separador()
                for especialidad in especialidad_disponible:
                    print(especialidad)
            # Input especialidad
                separador()
                especialidad_turno = input(f"Ingrese la especialidad: ")
            # Lista por comprensión
                patron = [especialidad for especialidad in especialidad_disponible if re.search(especialidad_turno,especialidad,re.IGNORECASE)]
                if len(patron) > 0:
                    especialidad_turno = patron[0]
                    print(f"Especialidad elegida: {especialidad_turno}")
                # Fecha
                    fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")
                # Validacion de la fecha en formato DD/MM/AAAA
                    if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
                    # Slicing
                        dia = int(fecha[:2])
                        mes = int(fecha[3:5])
                        anio = int(fecha[6:])
                        if (1 <= dia <= 31) and (1 <= mes <= 12):
                            fecha_valida = datetime(anio, mes, dia)
                            if fecha_valida >= datetime.today():
                                turnos[0].append(dni) # DNI Paciente
                                turnos[1].append(especialidad_turno) # Especialidad
                                indice = datos_medicos[2].index(especialidad_turno) 
                                turnos[2].append(datos_medicos[0][indice]) # Nombre médico
                                turnos[3].append(fecha_valida.strftime("%d/%m/%Y")) # Fecha turno
                                turnos[4].append(datos_medicos[3][indice]) # Lugar

                                print(" Turno registrado con éxito.")
                                separador()
                                # Mostrar último turno
                                print(f"DNI: {turnos[0][-1]}")
                                print(f"Especialidad: {turnos[1][-1]}")
                                print(f"Doctor: {turnos[2][-1]}")
                                print(f"Fecha del turno: {turnos[3][-1]}")
                                print(f"Sede del turno: {turnos[4][-1]}")
                                bandera_turnos = False
                            else:
                                print(" No se pueden elegir fechas anteriores a hoy.")
                        else:
                                print(" Fecha inválida.") 
                    else:
                            print(" Formato de fecha incorrecto.") 
                else:
                    print(" Especialidad no encontrada.")
            else:
                print("DNI no encontrado")        




def borrar_datos_usuarios(datos_usuarios):
    # Mostrar DNIs cargados
    for datos in datos_usuarios[0]:
        print(datos, end=" ")
    # Solicitamos DNI a eliminar
    dni = int(input("\nIndique el DNI a eliminar: "))
    # Validamos que exista dentro de la matriz y buscamos su posición con index
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni) 
        # Recorremos las sublistas de la matriz y eliminamos el indice con pop       
        for sublistas in datos_usuarios:      
            sublistas.pop(indice)          
        print(f"Usuario eliminado con éxito: {dni}")
    else:
        print("DNI no encontrado.")
    
    return datos_usuarios
        
def remplazar_datos_usuarios(datos_usuarios):
    dni = int(input("Indique su DNI: "))
    separador()
    # Validamos que el DNI se encuentre en la matriz
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni)
        # Mostramos los datos, algunos enmasacarados, a cambiar
        print("Indique el dato a modificar")
        print(f"1 - Nombre: {datos_usuarios[1][indice]}")
        print(f"2 - Contraseña: {enmascarar_contraseña(datos_usuarios[2][indice])}")
        print(f"3 - Gmail: {enmascarar_gmail(datos_usuarios[3][indice])}")
        print("0 - Para cerrar el menú")
        bandera_reemplazar = True
        while bandera_reemplazar:
            reemplazo = int(input("Ingrese la opción a cambiar: "))
            # Cambio de nombre
            if reemplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                # Usamos title para ingresar el nombre con mayúsculas automáticas
                datos_usuarios[1][indice] = nuevo_nombre.title()
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}")
            # Cambio de contraseña
            elif reemplazo == 2:
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                datos_usuarios[2][indice] = nueva_contraseña
                print("Contraseña cambiada con éxito")
            # Cambio de correo
            elif reemplazo == 3:
                nuevo_correo = input("Ingrese el nuevo correo: ")
                datos_usuarios[3][indice]= nuevo_correo
                print(f"Nuevo correo: {nuevo_correo}")
            # Cerrar menú
            elif reemplazo == 0:
                bandera_reemplazar = False
            else:
                print("Número no ncontrado")
    else:
        print("DNI no encontrado") 

def borrar_turnos(turnos):
    bandera_borrar_turnos = True
    while bandera_borrar_turnos:
        borrar_turnos_dni = int(input("Ingrese su DNI: "))
        # Validar que el DNI se encuentre en la matriz
        if borrar_turnos_dni in turnos[0]:
            # Usamos el index con paso -1 para usar como índice el ultimo dato encontrado
            indice = len(turnos[0]) - 1 - turnos[0][::-1].index(borrar_turnos_dni)
            # Eliminamos el indice de la sublista.
            for sublistas in turnos:
                sublistas.pop(indice)
            print("Último turno eliminado con éxito")
            bandera_borrar_turnos = False
        else:
                print("DNI no econtrado")

# Funciones para printear tablas

def mostrar_tabla(diccionario):
    print(f"{'DNI':<12}{'Nombre':<20}{'Clave':<10}{'Correo_electronico':<30}") #rebanadas
    print("-" * 72)
    
    lista_dni = diccionario["DNI"]
    lista_nombre = diccionario["Nombre"]
    lista_clave = diccionario["Clave"]
    lista_correo = diccionario["Correo_electronico"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_dni[i]):<12}{lista_nombre[i]:<20}{str(lista_clave[i]):<10}{lista_correo[i]:<30}")
    return print()

def mostrar_tabla_turnos(diccionario):
    print(f"{'DNI':<12}{'Especialidad':<20}{'Doctor':<20}{'Fecha':<15}{'Sede':15}") 
    print("-" * 72)

    lista_dni = diccionario["DNI"]
    lista_especialidad = diccionario["Especialidad"]
    lista_nombre = diccionario["Doctor"]
    lista_fecha = diccionario["Fecha"]
    lista_sede = diccionario["Sede"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_dni[i]):<12}{lista_especialidad[i]:<20}{lista_nombre[i]:20}{str(lista_fecha[i]):<15}{lista_sede[i]:15}")

def mostrar_turnos_cliente(diccionario_turnos):
    dni = int(input("Ingrese su DNI: "))
    print(f"{'DNI':<12}{'Especialidad':<20}{'Doctor':<20}{'Fecha':<15}{'Sede':15}") 
    print("-" * 72)

    for i in range(len(diccionario_turnos["DNI"])):
        if diccionario_turnos["DNI"][i]== dni:
            print(f"{str(diccionario_turnos["DNI"][i]):<12}{diccionario_turnos["Especialidad"][i]:<20}{diccionario_turnos["Doctor"][i]:<20}{str(diccionario_turnos["Fecha"][i]):<15}{diccionario_turnos["Sede"][i]:<}")