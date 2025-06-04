import time
from Menu.menu_main import *
from Menu.menu_cliente import *
import json

def cargar_json():
     with open("datos/admin.json", "r", encoding="UTF-8") as datos:
          admin = json.load(datos)
          return admin

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
                    admin = cargar_json()
                    if ingreso == 0:
                         print("Volviendo...")
                         time.sleep(1) 
                    else:
                        for usuario in admin:
                            if usuario["dni"] == ingreso:
                                print("Encontrado")
                                contraseña_admin = input("Ingrese la contraseña: ")
                                if str(contraseña_admin) == str(usuario["contraseña"]):
                                    menu_main(ingreso)
                                else:
                                    print("Contraseña incorrecta")
                                break
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