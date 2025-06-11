import time
from Menu.menu_main import *
from Menu.menu_cliente import *
import json

def cargar_json_admin():
     with open("datos/admin.json", "r", encoding="UTF-8") as datos:
          admin = json.load(datos)
          return admin
def cargar_json_usuario():
     with open("datos/usuarios.json", "r", encoding="UTF-8") as datos:
          usuarios = json.load(datos)
          return usuarios

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
                    print("0 - Cerrar menú")
                    ingreso = int(input("Ingrese su DNI:"))
               except ValueError:
                    print("Se espera numeros enteros")
               else:
                    admin = cargar_json_admin()
                    usuarios= cargar_json_usuario()
                    if ingreso == 0:
                         print("Volviendo...")
                         time.sleep(1) 
                    else:
                         encontrado = False
                         for usuario in admin:
                              if usuario["dni"] == ingreso:
                                   print("Encontrado")
                                   contraseña_admin = input("Ingrese la contraseña: ")
                                   if str(contraseña_admin) == str(usuario["contraseña"]):
                                        menu_main()
                                   else:
                                        print("Contraseña incorrecta")
                                   encontrado = True
                                   break
                         if not encontrado:
                              for usuario in usuarios:
                                   if usuario["dni"] == ingreso:
                                        print("Encontrado")
                                        contraseña_usuario = input("Ingrese la contraseña: ")
                                        if str(contraseña_usuario) == str(usuario["contraseña"]):
                                             menu_usuario(ingreso)
                                        else:
                                             print("Contraseña incorrecta")
                                        encontrado = True
                                        break
                         if not encontrado:
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