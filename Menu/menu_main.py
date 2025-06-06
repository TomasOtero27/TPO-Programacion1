#--------------------------------IMPORT-------------------------
import time
from Funciones.medicos.mostrar_tabla_medicos import *
from Funciones.medicos.crud_medicos import *
from Funciones.usuarios.mostrar_tabla import *
from Funciones.usuarios.crud_usuarios import *
from Funciones.usuarios.turnos import *
from datos.datos import *
#---------------------------------------------------------------------


def menu_main(ingreso):
    while True:
        titulo = "Bienvenido al Menú de administrador"
        titulo_decorado = titulo.center(50,"-")
        print(titulo_decorado)
        print("1 - Mostrar matriz de usuarios o médicos")
        print("2 - Ordenar por fila específica")
        print("3 - Agregar datos de paciente o médico")
        print("4 - Remover datos")
        print("5 - Modificar datos")
        print("6 - Crear o mostrar turnos")
        print("0 - Volver al menu principal")
        
        eleccion = input("Ingrese la opción: ")
        print("-"*50)

        # Mostrar matriz de usuarios o médicos
        if eleccion == "1":
            print("Datos a mostrar:")
            print("1 - Datos usuarios")
            print("2 - Datos médicos")
            print("0 - Cerrar menu")
            while True :
                eleccion_opcion_1 = input("Ingrese la opción: ")
                # Mostrar datos clientes
                if eleccion_opcion_1 == "1":
                    print("Mostrando los datos de los clientes")
                    "mostrar_tabla(diccionario_usuarios)"
                    abrir_archivo("datos/datos_usuario.txt")
                # Mostrar datos médicos
                elif eleccion_opcion_1 == "2":
                    print("Mostrando los datos médicos")
                    #mostrar_tabla_medicos(diccionarios_medicos)
                    abrir_archivo_medicos("datos/datos_medico.txt")    
                # Cerrar menú      
                elif eleccion_opcion_1 == "0":
                    print("Cerrando menú de mostrar diccionarios")
                    time.sleep(1)
                    break
                else:
                    print("Parámetro no encontrado")

        # Ordenar por fila específica
        elif eleccion == "2":
            print("1 - Ordenar la matriz de usuarios")
            print("2 - Ordenar la matriz de médicos")
            print("0 - Cerrar menú")
            while True :
                eleccion_ordenada = input("\nIngrese la opción: ")
                # Ordenar usuarios
                if eleccion_ordenada == 1:
                    print(datos_usuarios)  
                    fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
                    # Validamos la fila
                    if 0 <= fila and fila < len(datos_usuarios):  
                        ordenar_usuarios_por_campo(fila)
                        print("Fila ordenada con éxito.")
                        mostrar_matriz(datos_usuarios)  
                    else:
                        print("Número de fila inválido. Intente nuevamente.")

                # Ordenar médicos
                elif eleccion_ordenada == 2:
                    print(datos_medicos)  
                    fila = int(input("\nIngrese el número de la fila que desea ordenar (0 a 3): "))
                    # Validamos la fila
                    if 0 <= fila and fila < len(datos_medicos):  
                        ordenar_usuarios_por_campo(fila)
                        print("Fila ordenada con éxito.")
                        mostrar_matriz(datos_medicos)  
                    else:
                        print("Número de fila inválido. Intente nuevamente.")
                # Cerrar menú
                elif eleccion_ordenada == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Numero invalido")

        # Agregar datos de paciente o médico
        elif eleccion == "3":
            print("1 - Agregar usuarios")
            print("2 - Agregar médicos")
            print("0 - Cerrar menú")
            while True:
                eleccion_agregar = input("Seleccione una opción: ")
                # Agregar usuario
                if eleccion_agregar == "1":
                    agregar_usuarios("datos/usuarios.json")
                # Agregar médico
                elif eleccion_agregar == "2":
                    agregar_medicos("datos_medico.txt")
                elif eleccion_agregar == "0":
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Numero invalido")

        # Remover datos
        elif eleccion == "4":
            print("1 - Borrar datos de usuarios")
            print("2 - Borrar datos de medicos")
            print("3 - Borrar turnos")
            print("0 - Cerrar menú")
            while True:
                eleccion_borrar = input("Ingrese una opción: ")
                # Borrar usuario
                if eleccion_borrar == "1":
                    borrar_datos_usuarios(datos_usuarios)
                # Borrar médico
                elif eleccion_borrar == "2":
                    borrar_datos_medicos (datos_medicos)
                # Borrar turno
                elif eleccion_borrar == "3":
                    borrar_turnos(turnos)
                # Cerrar menú
                elif eleccion_borrar == "0":
                    print("Cerrando menu...")
                    time.sleep(1)
                    break
                else:
                    print("Parámetro incorrecto")

        # Modificar datos
        elif eleccion == "5":
            print("1 - Modificar datos de usuarios")
            print("2 - Modificar datos de médicos")
            print("0 - Cerrar menú")
            while True:
                eleccion_reemplazar = input("Ingrese una opción: ")
                # Modificar usuario
                if eleccion_reemplazar == "1":
                    try:    
                        busqueda = int(input("Ingrese el DNI a modificar: "))
                    except ValueError:
                        print(f"Se espera numeros... {busqueda}")
                    modificar_datos_usuarios_admin("datos/usuarios.json",busqueda)
                # Modificar médico
                if eleccion_reemplazar == "2":
                    remplazar_datos_medicos(datos_medicos)
                # Cerrar menú
                elif eleccion_reemplazar == "0":
                    print("Cerrando menu...")
                    time.sleep(1)
                    break
                else:
                    print("Parámetro incorrecto")
        
        # Crear o mostrar turnos
        elif eleccion == "6":
            diccionario_turnos = dict(zip(encabezado_turnos, turnos))
            print("1 - Crear turnos")
            print("2 - Mostrar turnos")
            print("3 - Borrar turnos")
            print("0 - Cerrar menú")
            while True:
                eleccion_turnos = int(input("Ingrese la opcion: "))
                # Crear turnos
                if eleccion_turnos == 1:
                    realizar_turnos(turnos,datos_medicos,datos_usuarios,ingreso)
                # Mostrar turnos
                elif eleccion_turnos == 2:
                    diccionario_turnos = dict(zip(encabezado_turnos, turnos))
                    mostrar_tabla_turnos(diccionario_turnos)
                # Borrar turnos
                elif eleccion_turnos == 3:
                    borrar_turnos(turnos)
                # Cerrar menú
                elif eleccion_turnos == 0:
                    print("Cerrando menu...")
                    time.sleep(1)
                    break
                else:
                    print("Numero incorrecto")
        # Cerrar menú
        elif eleccion == "0":
            print("Volviendo al login")
            time.sleep(1)
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

