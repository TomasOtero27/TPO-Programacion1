from base_prueba import *
from datos import *


def menu_usuario():
        bandera = True
        while bandera:
            print("\nBienvenido al Menú")
            print("1 - Para realizar un turno")
            print("2 - Para cambiar tus datos")
            print("3 - Para cancelar un turno")
            print("9- Para cerrar")
            eleccion = int(input("Indique: "))
            if eleccion == 1:
                  realizar_turnos(turnos,datos_medicos,datos_usuarios)
            elif eleccion == 2:
                  cambio = remplazar_datos_usuarios(datos_usuarios)
                  print(cambio)
            elif eleccion == 9:
                  print ("Cerrando cliente")
                  bandera = False
            else:
                  print("Numero incorrecto")