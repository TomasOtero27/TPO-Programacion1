from menu_main import *
from menu_cliente import *

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
                menu_C()

                bandera = False
                
            elif eleccion == -1:
                print("Cerrando el menu")
                bandera = False

            else:
                 print("Codigo invalido.")    


menu()