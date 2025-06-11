#--------------------------------IMPORT-------------------------
import time
import json
from Funciones.medicos.mostrar_tabla_medicos import *
from Funciones.medicos.crud_medicos import *
from Funciones.usuarios.mostrar_tabla import *
from Funciones.usuarios.crud_usuarios import *
from Funciones.usuarios.turnos import *
from Funciones.admin.turnos_admin import *
from datos.datos import *
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# Json y txt
def cargar_json_usuarios():
    with open("datos/usuarios.json", "r", encoding="UTF-8") as archivo:
        usuarios = json.load(archivo)
        return usuarios
    
def cargar_txt_medicos():
    with open("datos/medicos.txt", "r", encoding="UTF-8") as archivo:
        medicos = archivo.readlines()
        return [medico.strip() for medico in medicos]
    
def cargar_json_turnos():
    with open("datos/turnos.json", "r", encoding="UTF-8") as archivo:
        turnos = json.load(archivo)
        return turnos
    
def menu_main():
    while True:
        titulo = "Bienvenido al Menú de administrador"
        titulo_decorado = titulo.center(50,"-")
        print(titulo_decorado)
        print("1 - Datos de usuarios")
        print("2 - Datos de médicos")
        print("3 - Turnos")
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
            print("3 - Remover usuarios")
            print("0 - Cerrar menu")
            while True:
                print("-"*50)
                try:
                    usuarios = cargar_json_usuarios()
                except FileNotFoundError:
                    print("El archivo de usuarios no existe.")
                    break
                try:
                    eleccion_opcion_1 = int(input("Ingrese la opción: "))
                except ValueError:
                    print("Se espera un número...")
                # Mostrar datos usuarios
                if eleccion_opcion_1 == 1:
                    print("Mostrando datos de usuarios")
                # Agregar usuarios
                elif eleccion_opcion_1 == 2:
                    print("Agregar usuarios")
                # Remover usuarios
                elif eleccion_opcion_1 == 3:
                    print("Remover usuarios")
                # Cerrar menú      
                elif eleccion_opcion_1 == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Opción inválida.")

        # Datos de médicos
        elif eleccion == 2:
            try:   
                medicos = cargar_txt_medicos()
            except FileNotFoundError:
                print("El archivo de médicos no existe.")
                break
            print("1 - Mostrar médicos")
            print("2 - Agregar médicos") 
            print("3 - Remover médicos")  
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
                # Agregar médicos
                elif eleccion_opcion_2 == 2:
                    print("Agregar médicos")
                # Remover médicos
                elif eleccion_opcion_2 == 3:
                    print("Remover médicos")
                # Cerrar menú
                elif eleccion_opcion_2 == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Opción inválida")
        # Menú de turnos
        elif eleccion == 3:
            try:
                turnos = cargar_json_turnos()
            except FileNotFoundError:
                print("El archivo de turnos no existe.")
                break
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
                    print("Mostrando turnos")
                # Agregar turnos
                elif eleccion_opcion_3 == 2:
                    print("Agregar turnos")
                # Borrar turnos
                elif eleccion_opcion_3 == 3:
                    print("Borrar turnos")
                elif eleccion_opcion_3 == 0:
                    print("Cerrando menú")
                    time.sleep(1)
                    break
                else:
                    print("Opción inválida")
            # Cerrar menú
        elif eleccion == 0:
            print("Volviendo al menú principal")
            time.sleep(1)
            break
        else:
            print("Opción no encontrada")