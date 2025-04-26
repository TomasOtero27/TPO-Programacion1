from Funciones import *
from datos import *


def menu_usuario():
        bandera = True
        while bandera:
            print("\nBienvenido al Menú")
            print("1 - Para pedir un turno")
            print("2 - Para cambiar tus datos")
            print("3 - Para cancelar un turno")
            print("4 - mostrar mis turnos")
            print("9- Para cerrar")
            eleccion = int(input("Indique: "))
            if eleccion == 1:
                  realizar_turnos(turnos,datos_medicos,datos_usuarios)  #tuplas?
            elif eleccion == 2:
                  cambio = remplazar_datos_usuarios(datos_usuarios)
                  print(cambio)
            elif eleccion == 3:
                  borrar_turnos(turnos)
            elif eleccion == 4:
                  mostrar_turnos_cliente(diccionario_turnos)

            elif eleccion == 9:
                  print ("Cerrando cliente")
                  bandera = False
            else:
                  print("Numero incorrecto")