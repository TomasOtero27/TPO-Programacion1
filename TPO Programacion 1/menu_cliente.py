from base_prueba import *
from menu import *

def menu_C():
    bandera = True
    while bandera:
        print("\nBienvenido al Menú:")
        print("Agregar usuario, -1 para terminar")
        eleccion = int(input("usted es cliente?: "))
        if eleccion == 1:
            agrego = agregar_paciente(datos_pacientes)

            print(agrego)
     
        elif eleccion == -1:
            bandera = False


menu_C()# Ejecutar menú