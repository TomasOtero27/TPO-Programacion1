from Menu.menu_main import *
from Menu.menu_cliente import *

# Menú de inicio del programa
def menu():
     while True:
        titulo = "Bienvenido al Menú"
        titulo_decorado = titulo.center(50,"-")
        print(titulo_decorado)
        print("Inicio de Sesión")
        print("1 - Ingresar")
        print("2 - Crear usuario")
        print("0 - Cerrar menú")
        opcion = input("Ingrese la opcion: ")
        if opcion == "1":   # Ingreso al programa
                    try:
                        print("0 para volver")
                        ingreso = int(input("Ingrese su DNI:"))
                    except ValueError:
                         print("Se espera numeros enteros")
                    else:
                         if ingreso == 0:
                               print("Volviendo....")
                               break
                         elif ingreso in datos_usuarios[0]:
                              indice = datos_usuarios[0].index(ingreso)
                              contraseña = input("Ingrese la contraseña: ")
                              if ingreso == 43091220 and contraseña == "912": # Contraseña administrador
                                   menu_main(ingreso)
                                   break
                              elif contraseña == datos_usuarios[2][indice]: # Contraseña usuario
                                   menu_usuario(ingreso)
                                   break
                              else:
                                   print("Contraseña incorrecta")
                         else:
                              print("DNI no encontrado")
                
          # Agregar usuarios nuevos
        elif opcion == "2":
                    agregar_usuarios(datos_usuarios)
            
          # Cerrar menú
        elif opcion == "0":
          print("Cerrando el menu")
          break
        else:
                    print("Numero no encontrado")

# Main
menu()