import time
from Menu.menu_main import *
from Menu.menu_cliente import *

def separador():
    print("-"*50)

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
          opcion = input("Ingrese la opción: ")
          # Ingreso al programa
          if opcion == "1": 
               separador()  
               try:
                    print("0 para volver")
                    ingreso = int(input("Ingrese su DNI:"))
               except ValueError:
                    print("Se espera numeros enteros")
               else:
                    if ingreso == 0:
                         print("Volviendo...")
                         time.sleep(1) 
                    elif ingreso in admin[0]:
                         indice = admin[0].index(ingreso)
                         contraseña_admin = input("Ingrese la contraseña: ")
                         if contraseña_admin== admin[2][indice]: # Contraseña administrador
                              menu_main(ingreso)
                         else:
                              print("Contraseña incorrecta")
                    elif ingreso in datos_usuarios[0]:
                         indice = datos_usuarios[0].index(ingreso)
                         contraseña_usuario = input("Ingrese la contraseña: ")
                         if contraseña_usuario == datos_usuarios[2][indice]: # Contraseña usuario
                              menu_usuario(ingreso)
                         else:
                              print("Contraseña incorrecta")
                    else:
                         print("DNI no encontrado")
          # Agregar usuarios nuevos
          elif opcion == "2":
               separador()
               agregar_usuarios(datos_usuarios)
          # Cerrar menú
          elif opcion == "0":
               print("Cerrando el menu")
               time.sleep(1)
               break
          else:
               print("Opción no encontrada")

# Main
menu()