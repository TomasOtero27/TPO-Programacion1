import random
from datos import *

def ordenar_lista(fila):
    datos_usuarios[fila].sort()
    return datos_usuarios[fila]


def ordenar_lista(fila):
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
        #elif extender < 11111111 and extender > 99999999:
            #print("Numero invalido")
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