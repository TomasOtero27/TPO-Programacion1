from Funciones import *
from datos import *
def menu_main():
    bandera = True
    while bandera:
        titulo = "Bienvenido al Menú de administrador"
        titulo_decorado = titulo.center(50,"-")
        print(titulo_decorado)
        print("Seleccione una opción.")
        print("1 - Mostrar matriz de usuarios o medicos ")
        print("2 - Ordenar una fila específica")
        print("3 - Agregar datos paciente o medico")
        print("4 - Para remover datos")
        print("5 - Para modificar datos")
        print("6 - Para hacer turnos o mostrar turnos")
        print("7 - Cerrar menú")
        
        eleccion = input("Ingrese la opción: ")
        print("-"*50)


        if eleccion == "1":
            print("Datos a mostrar:")
            print("1 - Datos de los usuarios")
            print("2 - Datos de los medicos")
            print("3 - Cerrar menú")
            bandera_matriz = True
            while bandera_matriz :
                eleccion_opcion_1 = int(input("Ingrese la opción: "))
                if eleccion_opcion_1 == 1:
                    print("Mostrando los datos de los clientes")
                    mostrar_tabla(diccionario_usuarios)
                elif eleccion_opcion_1 == 2:
                    print("Mostrando los datos medicos: ")
                    mostrar_tabla_medicos(diccionarios_medicos)          #tuplas
                elif eleccion_opcion_1 == 3:
                    print("Cerrando opción 1")
                    bandera_matriz = False
                else:
                    print("Parametro no encontrado")


        elif eleccion == "2":
            print("1 - Ordenar la matriz de usuarios")
            print("2 - Ordenar la matriz de medicos")
            print("3 - Cerrar menú")
            bandera_ordenada= True
            while bandera_ordenada :
                eleccion_ordenada = int(input("Ingrese la opción: ") )
                if eleccion_ordenada == 1:
                    print(datos_usuarios)  
                    fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
                    if 0 <= fila and fila < len(datos_usuarios):  
                        ordenar_lista_usuarios(fila) 
                        print("Fila ordenada con éxito.")
                        mostrar_matriz(datos_usuarios)  
                    else:
                        print("Número de fila inválido. Intente nuevamente.")

                elif eleccion_ordenada == 2:
                    print(datos_medicos)  
                    fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
                    if 0 <= fila and fila < len(datos_medicos):  
                        ordenar_lista_medicos(fila) 
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
            print("1- para borrar datos de usuarios")
            print("2- para borrar datos de medicos")
            print("3 Para borrar turnos")
            print("4- Para cerrar")
            bandera_borrar = True
            while bandera_borrar:
                eleccion_borrar = int(input("Ingrese la opcion: "))
                if eleccion_borrar == 1:
                    borrar = borrar_datos_usuarios(datos_usuarios)
                    print(borrar)
                elif eleccion_borrar == 2:
                    borrar_medicos = borrar_datos_medicos (datos_medicos)
                    print (borrar_medicos)
                elif eleccion_borrar == 4:
                    bandera_borrar = False
                else:
                    print("Numero incorrecto")

        elif eleccion == "5":
            print("1- para modificar datos de usuarios")
            print("2- para modificar datos de medicos")
            print("3 Para modificar turnos")
            print("4- Para cerrar")
            bandera_remplazo = True
            while bandera_remplazo:
                eleccion_reemplazar = int(input("Ingrese la opcion: "))
                if eleccion_reemplazar == 1:
                    remplazar_datos_usuarios(datos_usuarios)
                if eleccion_reemplazar == 2:
                    remplazo_medicos = remplazar_datos_medicos(datos_medicos)
                    print(remplazo_medicos)
                elif eleccion_reemplazar == 4:
                    bandera_remplazo = False
                else:
                    print("Numero incorrecto...")
        elif eleccion == "6":
            print("1 - para realizar turnos")
            print("2 - para mostrar turnos")
            print("3 - para terminar")
            bandera_turnos = True
            while bandera_turnos:
                eleccion_turnos = int(input("Ingrese la opcion: "))
                if eleccion_turnos == 1:
                    realizar_turnos(turnos,datos_medicos,datos_usuarios)
                    
                elif eleccion_turnos == 2:
                    mostrar_tabla_turnos(diccionario_turnos)

                elif eleccion_turnos == 3:
                    bandera_turnos = False
                else:
                    print("Numero incorrecto")
        elif eleccion == "7":
            print("Cerrando menú...")
            bandera = False

        else:
            print("\nOpción inválida. Intente nuevamente.")

