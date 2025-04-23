from menu_main import *
from menu_cliente import *

def menu():
        bandera = True
        while bandera:
            titulo = "Bienvenido al Menú"
            titulo_decorado = titulo.center(50,"-")
            print(titulo_decorado)
            print("Inicio de Sesión")

            codigo = int(input("Ingresar codigo de usuario: "))
            print("-"*50)

            if codigo == 912:
                menu_main()

                bandera = False
                

            elif codigo == 2:
                agrego = agregar_usuarios(datos_usuarios)

                print(agrego)
            
                
            elif codigo == -1:
                print("Cerrando el menu")
                bandera = False

            elif codigo in datos_usuarios[2]:
                print(f"Código {codigo} encontrado, accediendo al menú.")
                menu_usuario()
                bandera = False
            else:
                 print("Código no encontrado")



menu()