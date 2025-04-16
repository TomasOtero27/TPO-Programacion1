from base_prueba import *
def menu_main():
    bandera = True
    while bandera:
        print("\nBienvenido al Menú:")
        print("1- Mostrar matriz de pacientes")
        print("2- Ordenar una fila específica")
        print("3- Agregar datos paciente")
        print("4- Argregar datos medicos")
        print("5- Cerrar menú")
        
        eleccion = input("Ingrese la opción: ")

        if eleccion == "1":
            print(datos_pacientes)

        elif eleccion == "2":
            print(datos_pacientes)  
            fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
            
            if 0 <= fila and fila < len(datos_pacientes):  
                ordenar_lista() 
                print("Fila ordenada con éxito.")
                mostrar_matriz(datos_pacientes)  
            else:
                print("Número de fila inválido. Intente nuevamente.")

        elif eleccion == "3":
            agrego = agregar_paciente(datos_pacientes)

            print(agrego)

 
        elif eleccion == "5":
            print("Cerrando menú...")
            bandera = False

        else:
            print("\nOpción inválida. Intente nuevamente.")

