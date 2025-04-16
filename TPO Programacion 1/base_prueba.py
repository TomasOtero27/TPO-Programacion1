import random
from datos import *

'''def burbuja(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:  
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  '''
                
def ordenar_lista():    
    datos_pacientes[0].sort()
    datos_pacientes[1].sort()
    datos_pacientes[2].sort()
    datos_pacientes[3].sort()
    
    
def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)

def agregar_paciente (datos_pacientes):
    bandera = True
    while bandera:
        extender = int(input("Ingrese DNI: "))
        if extender == -1:
            print("Cerrando agregar....")
            bandera = False
        #elif extender < 11111111 and extender > 99999999:
            #print("Numero invalido")
        else:
            datos_pacientes[0].append(extender)
            print("DNI agregado")
            nombre = input("Ingrese el nombre y apellido: ")
            datos_pacientes[1].append(nombre)       
            print("Nombre agregado")
            datos_pacientes[2].append(random.randint(100,999))
            print("Codigo agregado")
            gmail = input("Ingrese su gmail: ")
            datos_pacientes[3].append(gmail)

            return datos_pacientes 








            