from menu_main import *


def menu():
        bandera = True
        while bandera:
            print("\nBienvenido al Menú:")
            print("registro")

            eleccion = int(input("Ingresar codigo: "))

            if eleccion == 912:
                menu_main()

                bandera = False
                

            elif eleccion == 2:
                agrego = agregar_usuarios(datos_usuarios)

                print(agrego)
                bandera = False
            
                
            elif eleccion == -1:
                print("Cerrando el menu")
                bandera = False

            else:
                 print("Codigo invalido.")    


menu()