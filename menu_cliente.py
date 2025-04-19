from base_prueba import *
from datos import *


def menu_usuario():
        bandera = True
        while bandera:
            print("\nBienvenido al Menú")
            print("1- Para realizar un turno")
            print()
            print()
            print("9- Para cerrar")
            eleccion = int(input("Indique: "))
            if eleccion == 1:
                  realizar_turnos(turnos,datos_medicos,datos_usuarios)
            elif eleccion == 9:
                  print ("Cerrando cliente")
                  bandera = False
            else:
                  print("Numero incorrecto")