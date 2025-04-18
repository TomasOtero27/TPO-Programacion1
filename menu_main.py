from base_prueba import *
from datos import *
def menu_main():
    bandera = True
    while bandera:
        print("\nBienvenido al Menú:")
        print("1- Mostrar matriz de usuarios o medicos ")
        print("2- Ordenar una fila específica")
        print("3- Agregar datos paciente o medico")
        print("4- Cerrar menú")
        
        eleccion = input("Ingrese la opción: ")

        if eleccion == "1":
            print("1- para datos usuarios")
            print("2- datos medicos")
            print("3- Para cerrar")
            bandera_matriz = True
            while bandera_matriz :
                eleccion_opcion_1 = int(input("Seleccione opcion: "))
                if eleccion_opcion_1 == 1:
                    print("Mostrando los datos de los clientes")
                    print(datos_usuarios)
                elif eleccion_opcion_1 == 2:
                    print("Mostrando los datos medicos: ")
                    print(datos_medicos) 
                elif eleccion_opcion_1 == 3:
                    print("Cerrando opcion 1")
                    bandera_matriz = False
                else:
                    print("Incorrecto")


        elif eleccion == "2":
            print("1- para ordenar la matriz de usuarios")
            print("2- para ordenar la matriz de medicos")
            print("3- Para cerrar")
            bandera_ordenada= True
            while bandera_ordenada :
                eleccion_ordenada = int(input("Seleccione opcion: ") )
                if eleccion_ordenada == 1:
                    print(datos_usuarios)  
                    fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
                    if 0 <= fila and fila < len(datos_usuarios):  
                        ordenar_lista(fila) 
                        print("Fila ordenada con éxito.")
                        mostrar_matriz(datos_usuarios)  
                    else:
                        print("Número de fila inválido. Intente nuevamente.")

                elif eleccion_ordenada == 2:
                    print(datos_medicos)  
                    fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
                    if 0 <= fila and fila < len(datos_medicos):  
                        ordenar_lista(fila) 
                        print("Fila ordenada con éxito.")
                        mostrar_matriz(datos_medicos)  
                    else:
                        print("Número de fila inválido. Intente nuevamente.")
                elif eleccion_ordenada == 3:
                    print("Cerrando opcion 2")
                    bandera_ordenada = False
                else:
                    print("Numero invalido")

        elif eleccion == "3":
            print("1- para ordenar la matriz de usuarios")
            print("2- para ordenar la matriz de medicos")
            print("3- Para cerrar")
            bandera_agregar = True
            while bandera_agregar:
                eleccion_agregar = int(input("Seleccione opcion: "))
                if eleccion_agregar == 1:
                    agrego = agregar_usuarios(datos_usuarios)
                    print(agrego)
                elif eleccion_agregar == 2:
                    agregar = agregar_medicos(datos_medicos)
                    print(agregar)
                elif eleccion_agregar == 3:
                    print("Cerrando opcion 3")
                    bandera_agregar = False
                else:
                    print("Numero invalido")


        elif eleccion == "4":
            print("Cerrando menú...")
            bandera = False

        else:
            print("\nOpción inválida. Intente nuevamente.")

