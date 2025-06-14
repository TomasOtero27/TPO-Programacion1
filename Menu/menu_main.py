#--------------------------------IMPORT-------------------------
import time
from Funciones.medicos.mostrar_tabla_medicos import *
from Funciones.medicos.crud_medicos import *
from Funciones.usuarios.mostrar_tabla import *
from Funciones.usuarios.crud_usuarios import *
from Funciones.usuarios.turnos import *
from Funciones.admin.turnos_admin import *
from Funciones.admin.crud_usuarios_admin import *
from Funciones.admin.respadocrudmedico import *
from datos.datos import *
#---------------------------------------------------------------------
#---------------------------------------------------------------------

def menu_main():
    while True:
        titulo = "Bienvenido al Menú de administrador"
        titulo_decorado = titulo.center(50,"-")
        print(titulo_decorado)
        print("1 - Datos de usuarios")
        print("2 - Datos de médicos")
        print("3 - Turnos")
        print("4 - Seguros médicos")
        print("0 - Cerrar menú")
        print("-"*50)
        
        try:
            eleccion = int(input("Ingrese la opción: "))
        except ValueError:
            print("Se espera un número...")
            continue
        print("-"*50)

        # Mostrar matriz de usuarios o médicos
        if eleccion == 1:
            print("1 - Mostrar usuarios")
            print("2 - Agregar usuarios")
            print("3 - Cambiar datos de usuarios")
            print("4 - Remover usuarios")
            print("0 - Cerrar menu")
            while True:
                print("-"*50)
                try:
                    eleccion_opcion_1 = int(input("Ingrese la opción: "))
                except ValueError:
                    print("Se espera un número...")
                # Mostrar datos usuarios
                if eleccion_opcion_1 == 1:
                    print("Mostrando los datos de los clientes")
                    abrir_archivo("datos/usuarios.json")
                # Agregar usuarios
                elif eleccion_opcion_1 == 2:
                    agregar_usuarios("datos/usuarios.json")
                    abrir_archivo("datos/usuarios.json")
                elif eleccion_opcion_1 == 3:
                    abrir_archivo("datos/usuarios.json")
                    try:    
                        abrir_archivo("datos/usuarios.json")
                        busqueda = int(input("Ingrese el DNI a modificar: "))
                    except ValueError:
                        print(f"Se espera numeros... {busqueda}")
                    modificar_datos_usuarios_admin("datos/usuarios.json",busqueda)
                # Remover usuarios
                elif eleccion_opcion_1 == 4:
                    try:    
                        abrir_archivo("datos/usuarios.json")
                        busqueda = int(input("Ingrese el DNI del usuario para eliminar: "))
                    except ValueError:
                        print(f"Se espera numeros... {busqueda}")
                    eliminar_usuario("datos/usuarios.json",busqueda)
                # Cerrar menú      
                elif eleccion_opcion_1 == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Opción inválida.")

        # Datos de médicos
        elif eleccion == 2:
            print("1 - Mostrar médicos")
            print("2 - Agregar médicos") 
            print("3 - Modificar datos medicos")
            print("4 - Remover médicos")  
            print("0 - Cerrar menú")
            while True :
                print("-"*50)
                try:
                    eleccion_opcion_2 = int(input("Ingrese la opción: "))
                except ValueError:
                    print("Se espera un número...")
                # Mostrar médicos
                if eleccion_opcion_2 == 1:
                    print("Mostrando datos de médicos")
                    abrir_archivo_medicos("datos/medicos.txt") 
                # Agregar médicos
                elif eleccion_opcion_2 == 2:
                    agregar_medicos("datos/medicos.txt")
                # Remover médicos
                elif eleccion_opcion_2 == 3:
                    abrir_archivo_medicos("datos/medicos.txt")
                    remplazar_datos_medicos("datos/medicos.txt")
                elif eleccion_opcion_2 == 4:
                    print("Remover médicos") #TERMINAR
                # Cerrar menú
                elif eleccion_opcion_2 == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Opción inválida")
        # Menú de turnos
        elif eleccion == 3:
            print("1 - Mostrar turnos")
            print("2 - Agregar turnos")
            print("3 - Borrar turnos")
            print("0 - Cerrar menú")
            while True:
                print("-"*50)
                try:
                    eleccion_opcion_3 = int(input("Seleccione una opción: "))
                except ValueError:
                    print("Se espera un número...")
                # Mostrar turnos
                if eleccion_opcion_3 == 1:
                    mostrar_turnos_ordenados("datos/turnos.json")
                # Agregar turnos
                elif eleccion_opcion_3 == 2:
                    print("Cargando funcion para agregar turnos")
                    time.sleep(3)
                    abrir_archivo("datos/usuarios.json")
                    time.sleep(2)
                    realizar_turnos("datos/turnos.json","datos/turnos_disponibles.json","datos/usuarios.json")
                # Borrar turnos
                elif eleccion_opcion_3 == 3:
                    print("Cargando funcion para borrar turnos")
                    abrir_archivo("datos/usuarios.json")
                    borrar_turnos_admin("datos/turnos.json","datos/turnos_disponibles.json","datos/usuarios.json")
                elif eleccion_opcion_3 == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Opción inválida")
        # Menú de seguros médicos
        elif eleccion == 4:
            print("1 - Mostrar cantidad de usuarios activos")
            print("2 - Mostrar la cantidad de seguros medicos")
            print("0 - Cerrar menú")
            try:
                eleccion_opcion_4 = int(input("Ingrese la opcion: "))
            except ValueError:
                print("Se espera un número...")
                continue
            if eleccion_opcion_4 == 1:
                activos = recursividad_activos("datos/usuarios.json")
                print(f"Usuarios activos: {activos}")
            elif eleccion_opcion_4 == 2:
                activos = recursividad_seguros("datos/usuarios.json")
                print(f"Usuarios con seguro kukardo: {activos}")
            elif eleccion_opcion_4 == 0:
                print("Volviendo...")
                time.sleep(2)
                break
            else:
                print("Número incorrecto.")
        # Cerrar menú
        elif eleccion == 0:
            print("Volviendo al menú principal")
            time.sleep(3)
            break
        else:
            print("Opción no encontrada")