import random
from datos import *

def ordenar_lista_usuarios(fila):
    datos_usuarios[fila].sort()
    


def ordenar_lista_medicos(fila):
    datos_medicos[fila].sort()
        
    
def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)

def agregar_usuarios (datos_usuarios):
    bandera = True
    while bandera:
        extender = int(input("Ingrese DNI: "))
        if extender == -1:
            print("Cerrando menú")
            bandera = False
        elif extender < 11111111 or extender > 99999999:
            print("Numero invalido")
        else:
            datos_usuarios[0].append(extender)
            print("DNI agregado")
            nombre = input("Ingrese el nombre y apellido: ")
            datos_usuarios[1].append(nombre)       
            print("Nombre agregado")
            datos_usuarios[2].append(random.randint(100,999))
            print("Codigo agregado")
            gmail = input("Ingrese su gmail: ")
            datos_usuarios[3].append(gmail)
            print()

            return datos_usuarios 

def agregar_medicos (datos_medicos):
    bandera = True
    while bandera:
        extender_medicos = int(input("Ingrese DNI: "))
        if extender_medicos == -1:
            print("Cerrando agregar....")
            bandera = False
        elif extender_medicos < 11111111 or extender_medicos > 99999999:
            print("Numero invalido")
        else:
            datos_medicos[1].append(extender_medicos)
            print("DNI agregado")
            nombre = input("Ingrese el nombre y apellido: ")
            datos_medicos[0].append(nombre)
            print("Nombre agregado")
            especialidad = input("Ingrese especialidad: ")
            datos_medicos[2].append(especialidad) 
            print("Especialidad agregada")   
            sede = input("Ingrese la sede: ")
            datos_medicos[3].append(sede)   
            gmail = input("Ingrese su gmail: ")
            datos_medicos[4].append(gmail)

            return datos_medicos


def realizar_turnos (turnos,datos_medicos,datos_usuarios):
    bandera_turnos = True
    while bandera_turnos:                       #Modificar nombres para no generar confuciones jijijo
        turno_medico = int(input("Ingrese el DNI: "))
        if turno_medico in datos_usuarios[0]:
            turnos[0].append(turno_medico)
            print(datos_medicos)
            especialidad_turno = input("Ingrese la especialidad")       #Validar
            if especialidad_turno in datos_medicos[2]:
                turnos[1].append(especialidad_turno)
                turnos[2].append(datos_medicos[0])#modificar
                fecha = input("Ingrese la fecha: ")
                turnos[3].append(fecha)
                print(turnos)
            else:
                print("No encontrado")
        elif turno_medico == -1:
            bandera_turnos = False
        else:
            print("DNI no encontrado")
        return turnos
    
def borrar_datos_usuarios(datos_usuarios):
    print(datos_usuarios[0])
    dni = int(input("Indique el DNI: "))
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni) #con el index buscamos su ubicacion de la matriz
        
        for sublistas in datos_usuarios:        #usando metodo de listas, con for in
            sublistas.pop(indice)                #el pop(indice) borra todos los datos de la ubicacion 
        print(f"Usuario eliminado con éxito: {dni}")
    else:
        print("DNI no encontrado.")
    
    return datos_usuarios

def borrar_datos_medicos(datos_medicos):
    print(datos_medicos[1])
    dni = int(input("Indique el DNI: "))
    if dni in datos_medicos[1]:
        indice = datos_medicos[1].index(dni) #con el index buscamos su ubicacion de la matriz
        
        for sublistas in datos_medicos:        #usando metodo de listas, con for in
            sublistas.pop(indice)                #el pop(indice) borra todos los datos de la ubicacion 
        print(f"Usuario eliminado con éxito: {dni}")   #parametros reales pasados por nombre F{}
    else:
        print("DNI no encontrado.")
    
    return datos_usuarios

def remplazar_datos_usuarios(datos_usuarios):
    dni = int(input("Indique DNI: "))
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni)
        print("Indique que quiere modificar")
        print(f"1 - Nombre: {datos_usuarios[1][indice]}")
        print(f"2 - Contraseña: {datos_usuarios[2][indice]}")
        print(f"3 - Gmail: {datos_usuarios[3][indice]}")
        print("4 - Para terminar")
        bandera_remplazar = True
        while bandera_remplazar:
            remplazo = int(input("Ingrese la opcion: "))
            if remplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                datos_usuarios[1][indice] = nuevo_nombre
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}") 
            elif remplazo == 2:
                nueva_contraseña = int(input("Ingrese la nueva contraseña: "))
                datos_usuarios[2][indice] = nueva_contraseña
                print("Contraseña cambiada....")                #USAR PARA QUE SEA TDO ##### POR SUB, VALIDAR CON DELIMITACION
            elif remplazo == 3:
                nuevo_gmail = input("Ingrese el nuevo gmail: ")
                datos_usuarios[3][indice]= nuevo_gmail
                print(f"Gmail cambiado: {nuevo_gmail}")
            elif remplazo == 4:
                bandera_remplazar = False
            else:
                print("Numero no ncontrado")
    else:
        print("DNI no encontrado...")
    return datos_usuarios


def remplazar_datos_medicos(datos_medicos):
    dni = int(input("Indique DNI: "))
    if dni in datos_medicos[0]:
        indice = datos_medicos[0].index(dni)
        print("Indique que quiere modificar")
        print(f"1 - Nombre: {datos_medicos[1][indice]}")
        print(f"2 - Contraseña: {datos_medicos[2][indice]}")
        print(f"3 - Gmail: {datos_medicos[3][indice]}")
        print("4 - Para terminar")
        bandera_remplazar = True
        while bandera_remplazar:
            remplazo = int(input("Ingrese la opcion: "))
            if remplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                datos_medicos[1][indice] = nuevo_nombre
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}") 
            elif remplazo == 2:
                nueva_contraseña = int(input("Ingrese la nueva contraseña: "))
                datos_medicos[2][indice] = nueva_contraseña
                print("Contraseña cambiada....")                #USAR PARA QUE SEA TDO ##### POR SUB, VALIDAR CON DELIMITACION
            elif remplazo == 3:
                nuevo_gmail = input("Ingrese el nuevo gmail: ")
                datos_medicos[3][indice]= nuevo_gmail
                print(f"Gmail cambiado: {nuevo_gmail}")
            elif remplazo == 4:
                bandera_remplazar = False
            else:
                print("Numero no ncontrado")
    else:
        print("DNI no encontrado...")
    return datos_medicos
