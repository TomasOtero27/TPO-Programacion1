from Funciones.usuarios.mostrar_tabla import *
from Funciones.usuarios.crud_usuarios import *
from Funciones.usuarios.turnos import *
from datos.datos import *

# Menú de usuario
def menu_usuario(ingreso):
        while True:
            titulo = "Bienvenido al Menú de Cliente"
            titulo_decorado = titulo.center(50,"-")
            print(titulo_decorado)
            print("1 - Turnos")
            print("2 - Mis Datos")
            print("0 - Salir")
            eleccion = input("Seleccione una opción: ")
            # Validación de opciónes
            if eleccion == "1": 
                # Menú turnos
                while True:
                  titulo = "Bienvenido al menú de turnos"
                  titulo_decorado = titulo.center(50,"-")
                  print(titulo_decorado)
                  print("1 - Solicitar turno")
                  print("2 - Mostrar mis turnos")
                  print("0 - Salir")
                  try:
                        opcion = int(input("Seleccione una opción: "))
                  except ValueError:                             
                        print("Solo números enteros")
                        continue
                  
                  if opcion == 1:
                        # Solicitar turno TERMINAR
                        realizar_turnos_usuarios("datos/turnos.json","datos/turnos_disponibles.json","datos/usuarios.json",ingreso)
                        break 
                  elif opcion == 2:
                        # Mostrar y eliminar turnos
                        mostrar_turnos_cliente(diccionario_turnos,ingreso)
                        print("1 - Eliminar turno")
                        print("0 - Salir")
                        try: 
                              opcion = int(input("Seleccione una opción: "))
                        except ValueError:                             
                              print("Solo números enteros")
                              continue
                        if opcion == 1:
                               borrar_turnos(turnos, ingreso, turnos_disponibles)
                        elif opcion == 0:
                              break
                        else:
                              print("Opción inválida")
            elif eleccion == "2":
                        print("1- Mostrar mis datos")
                        print("2- Modificar mis datos")
                        opcion_datos = input("Indique la opcion deseada: ")
                        if opcion_datos == "1":
                              mostrar_datos_usuarios("datos/usuarios.json",ingreso)
                        elif opcion_datos == "2":
                              modificar_datos_usuarios("datos/usuarios.json",ingreso)

            elif opcion == "0":
                        break
            else:
                        print("Opción inválida")