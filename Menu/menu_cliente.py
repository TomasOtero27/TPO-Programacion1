from Funciones import *
from datos import *

# Menú de usuario
def menu_usuario(ingreso):
        while True:
            titulo = "Bienvenido al Menú de Cliente"
            titulo_decorado = titulo.center(50,"-")
            print(titulo_decorado)
            print("1 - Pedir un turno")
            print("2 - Cambiar tus datos")
            print("3 - Cancelar último turno")
            print("4 - Mostrar mis turnos")
            print("0 - Cerrar menú")
            eleccion = input("Seleccione una opción: ")
            # Validación de opciónes
            if eleccion == "1": 
                  # Agregar turno
                  realizar_turnos(turnos,datos_medicos,datos_usuarios,ingreso) 
            elif eleccion == "2":
                  # Cambiar datos
                  cambio = remplazar_datos_usuarios(datos_usuarios,ingreso)
                  print(cambio)
            elif eleccion == "3":
                  # Eliminar turno
                  borrar_turnos(turnos,ingreso)
            elif eleccion == "4":
                  mostrar_turnos_cliente(diccionario_turnos,ingreso)
            elif eleccion == "0":
                  # Cerrar menú
                  print ("Cerrando menú")
                  break
            else:
                  print("Opción incorrecta")