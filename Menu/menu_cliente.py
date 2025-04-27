from Funciones import *
from datos import *

# Menú de usuario
def menu_usuario(ingreso):
        bandera = True
        while bandera:
            titulo = "Bienvenido al Menú de Cliente"
            titulo_decorado = titulo.center(50,"-")
            print(titulo_decorado)
            print("1 - Pedir un turno")
            print("2 - Cambiar tus datos")
            print("3 - Cancelar último turno")
            print("4 - Mostrar mis turnos")
            print("0 - Cerrar menú")
            eleccion = int(input("Seleccione una opción: "))
            # Validación de opciónes
            if eleccion == 1: 
                  # Agregar turno
                  realizar_turnos(turnos,datos_medicos,datos_usuarios) 
            elif eleccion == 2:
                  # Cambiar datos
                  cambio = remplazar_datos_usuarios(datos_usuarios)
                  print(cambio)
            elif eleccion == 3:
                  # Eliminar turno
                  borrar_turnos(turnos)
            elif eleccion == 4:
                  mostrar_turnos_cliente(diccionario_turnos)
            elif eleccion == 0:
                  # Cerrar menú
                  print ("Cerrando menú")
                  bandera = False
            else:
                  print("Opción incorrecta")