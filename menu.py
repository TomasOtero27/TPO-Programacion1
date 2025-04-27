# Funciones menú
from Menu.menu_main import *
from Menu.menu_cliente import *

# Menú de inicio del programa
def menu():
     bandera = True
     while bandera:
          titulo = "Bienvenido al Menú"
          titulo_decorado = titulo.center(50,"-")
          print(titulo_decorado)
          print("Inicio de Sesión")
          print("1 - Ingresar")
          print("2 - Crear usuario")
          print("0 - Cerrar menú")
          opcion = int(input("Seleccione una opción: "))
          print("-"*50)

          # Validacion de opciones
          if opcion == 1:   # Ingreso al programa
               ingreso = int(input("Ingrese su DNI:"))
               if ingreso in datos_usuarios[0]:
                    indice = datos_usuarios[0].index(ingreso)
                    contraseña = input("Ingrese la contraseña: ")
                    if contraseña == "912": # Contraseña administrador
                         menu_main()
                         bandera = False
                    elif contraseña == datos_usuarios[2][indice]: # Contraseña usuario
                         menu_usuario(ingreso)
                         bandera = False
                    else:
                         print("Contraseña incorrecta")
               else:
                    print("DNI no encontrado")
                
          # Agregar usuarios nuevos
          elif opcion == 2:
               agregar_usuarios(datos_usuarios)
            
          # Cerrar menú
          elif opcion == 0:
               print("Cerrando el menu")
               bandera = False
          else:
               print("Código no encontrado")

# Main
menu()