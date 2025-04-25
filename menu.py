from menu_main import *
from menu_cliente import *

def menu():
        bandera = True
        while bandera:
            titulo = "Bienvenido al Menú"
            titulo_decorado = titulo.center(50,"-")
            print(titulo_decorado)
            print("Inicio de Sesión")
            print("1 - Para ingresar")
            print("2 - para crear usuario")
            print("3 - Para cerrar")
            opcion = int(input("Seleccione opcion: "))
            print("-"*50)

            if opcion == 1:
                ingreso = int(input("Ingrese su DNI:"))
                if ingreso in datos_usuarios[0]:
                     indice = datos_usuarios[0].index(ingreso)
                     contraseña = int(input("Ingrese la contraseña:"))
                     if contraseña == 912:
                          menu_main()
                          bandera = False
                     elif contraseña == datos_usuarios[2][indice]:
                          menu_usuario()
                          bandera = False
                     else:
                          print("Contraseña incorrecta")
                else:
                     print("DNI no encontrado...")
                

            elif opcion == 2:
                agrego = agregar_usuarios(datos_usuarios)

                print(agrego)
            
                
            elif opcion == 3:
                print("Cerrando el menu")
                bandera = False
            else:
                 print("Código no encontrado")



menu()