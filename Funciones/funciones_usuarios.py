from datetime import datetime
import re
from datos.datos import *

fecha_ingresada = "25/04/2025"
fecha_usuario = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
fecha_actual = datetime.today()

def separador():
    print("-"*50)

def ordenar_usuarios_por_campo(ordenar):
    usuarios = list(zip(*datos_usuarios))
    usuarios.sort(key=lambda usuario: usuario[ordenar])           #lambda
    for i in range(len(datos_usuarios)):
        datos_usuarios[i] = [usuario[i] for usuario in usuarios]


def enmascarar_contraseña(contraseña):
    contraseña_enmascarada =  re.sub(r'.',"*", contraseña)
    return contraseña_enmascarada

def enmascarar_gmail(gmail):
    gmail_enmascarado = re.sub(r'^[^@]+', "*" * 10, gmail)
    return gmail_enmascarado

def abrir_archivo(archivo):
    try:
        contenido = open(archivo, "r", encoding="UTF-8")
        for linea in contenido:
            print(linea.strip())
            print(f'{"dni": 10}{"nombres": 20}{"contraseña":10}{"gmail": 20}{"seguro": 20}')
        while linea:
            dni, nombres, contraseña, gmail, seguro = linea.split(";")
            if dni > 1:
                print(f'{dni: 10}{nombres: 20}{contraseña:10}{gmail: 20}{seguro: 20}')
            linea = contenido.readline().strip()
    except FileNotFoundError:
        print("Archivo no encontrado")
    except OSError as mensaje:
        print("Fallo todo")
    finally:
        try:
            contenido.close()
        except:
            print("Fallo")
    
def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)

def agregar_usuarios (datos_usuarios):
    while True:
        try:
            print("0 para volver")
            dni = int(input("Ingrese su DNI: "))
        except ValueError:
            print("Se espera numeros enteros")
            continue # Reinicia el bucle
        else:
            if dni == 0:
                print("Volviendo...")
                break
            # Validamos el largo del DNI
            elif (dni < 1000000 or dni > 99999999):
                print("DNI inválido")
            elif dni in datos_usuarios[0]:
                print("Este DNI ya se encuentra registrado")
                continue
            else:
                # Agregamos DNI
                datos_usuarios[0].append(dni)
                print("DNI agregado")
                # Agregamos Nombre
                nombre = input("Ingrese el nombre y apellido: ")
                datos_usuarios[1].append(nombre.upper())       
                print("Nombre agregado")
                # Agregamos Contraseña
                contraseña_agregar=input("Ingrese la contraseña: ")
                datos_usuarios[2].append(contraseña_agregar)
                print("Contraseña agregada")
                # Agregamos Correo
                correo = input("Ingrese su correo: ")
                datos_usuarios[3].append(correo)
                # Agreagamos Obra Social
                while True:
                    print("Seleccione su obra social.")
                    print("1 - UwUseguros")
                    print("2 - JijazoSalud")
                    print("3 - Particular")

                    try:
                        obras = int(input("Seleccione una opción: "))
                        while obras < 1 or obras > 3:
                            print("Opción incorrecta")
                            obras = int(input("Seleccione una opción: "))
                        if obras == 1:
                            datos_usuarios[4].append("UwUseguros")
                            break
                        elif obras == 2:
                            datos_usuarios[4].append("JijazoSalud")
                            break
                        elif obras == 3:
                            datos_usuarios[4].append("Particular")
                            break
                        else:
                            print("Opción inválida")
                    except ValueError:
                        print("Se esperaba números enteros entre 1 y 3")
                print("Usuario creado con éxito")
                break
                



def realizar_turnos (turnos,datos_medicos,datos_usuarios,ingreso):
    while True:
        print(f"Entrando al Menú turnos con: {ingreso}")
        indice_ingreso = datos_usuarios[0].index(ingreso)
        print(f"Bienvenido al Menu turnos: {indice_ingreso}")

        especialidad_disponible = datos_medicos[3]

        # Mostrar especialidades
        print("Especialidades disponibles:")
        separador()
        for especialidad in especialidad_disponible:
            print(especialidad)
        separador()
        # Input especialidad
        especialidad_turno = input("Ingrese la especialidad: ")
        patron = [especialidad for especialidad in especialidad_disponible if re.search(especialidad_turno, especialidad, re.IGNORECASE)]

        if patron:
            especialidad_turno = patron[0]
            print(f"Especialidad elegida: {especialidad_turno}")

            while True:
                fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")

                if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
                    try:
                        dia = int(fecha[:2])
                        mes = int(fecha[3:5])
                        anio = int(fecha[6:])
                        fecha_valida = datetime(anio, mes, dia) 

                        if fecha_valida >= datetime.today():
                            # Guardar turno
                            turnos[0].append(ingreso)
                            turnos[1].append(indice_ingreso)
                            turnos[2].append(especialidad_turno)

                            indice = datos_medicos[3].index(especialidad_turno)
                            turnos[3].append(datos_medicos[0][indice])  # Doctor
                            turnos[4].append(fecha_valida.strftime("%d/%m/%Y"))
                            turnos[5].append(datos_medicos[4][indice])  # Costo

                            print("Turno registrado con éxito.")
                            print(f"DNI: {turnos[0][-1]}")
                            print(f"Paciente: {datos_usuarios[1][indice_ingreso]}")
                            print(f"Especialidad: {turnos[2][-1]}")
                            print(f"Doctor: {turnos[3][-1]}")
                            print(f"Fecha: {turnos[4][-1]}")
                            print(f"Costo: {turnos[5][-1]}")
                            break
                        else:
                            print("No se pueden elegir fechas anteriores a hoy")
                    except ValueError:
                        print("Error de fecha inexistente")
                else:
                    print("Formato de fecha incorrecto. Ingresar como DD/MM/AAAA")
            break
        else:
            print("Especialidad no encontrada")

       



def borrar_datos_usuarios(datos_usuarios):
    # Mostrar DNIs cargados
    for datos in datos_usuarios[0]:
        print(datos, end=" ")
    # Solicitamos DNI a eliminar
    dni = int(input("\nIndique el DNI a eliminar: "))
    # Validamos que exista dentro de la matriz y buscamos su posición con index
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni) 
        # Recorremos las sublistas de la matriz y eliminamos el indice con pop       
        for sublistas in datos_usuarios:      
            sublistas.pop(indice)          
        print(f"Usuario eliminado con éxito: {dni}")
    else:
        print("DNI no encontrado.")
    
    return datos_usuarios
        
def remplazar_datos_usuarios(datos_usuarios,ingreso):
        print (f"Entrando a la funcion reemplazo con: {ingreso}")
        indice_ingreso = datos_usuarios[0].index(ingreso)
        print(f"Bienvenido: {indice_ingreso}")
        indice = datos_usuarios[0].index(ingreso)
        # Mostramos los datos, algunos enmasacarados, a cambiar
        print("Indique el dato a modificar")
        print(f"1 - Nombre: {datos_usuarios[1][indice]}")
        print(f"2 - Contraseña: {enmascarar_contraseña(datos_usuarios[2][indice])}")
        print(f"3 - Gmail: {enmascarar_gmail(datos_usuarios[3][indice])}")
        print("0 - Para cerrar el menú")
        while True:
            reemplazo = int(input("Ingrese la opción a cambiar: "))
            # Cambio de nombre
            if reemplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                # Usamos title para ingresar el nombre con mayúsculas automáticas
                datos_usuarios[1][indice] = nuevo_nombre.title()
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}")
            # Cambio de contraseña
            elif reemplazo == 2:
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                datos_usuarios[2][indice] = nueva_contraseña
                print("Contraseña cambiada con éxito")
            # Cambio de correo
            elif reemplazo == 3:
                nuevo_correo = input("Ingrese el nuevo correo: ")
                datos_usuarios[3][indice]= nuevo_correo
                print(f"Nuevo correo: {nuevo_correo}")
            # Cerrar menú
            elif reemplazo == 0:
                break
            else:
                print("Número no ncontrado") 

def borrar_turnos(turnos,ingreso):
    while True:
        borrar_turnos_dni = int(input("Ingrese su DNI: "))  #se debe ingresar directo y elegir que turno borrar
        # Validar que el DNI se encuentre en la matriz
        if borrar_turnos_dni in turnos[0]:
            # Usamos el index con paso -1 para usar como índice el ultimo dato encontrado
            indice = len(turnos[0]) - 1 - turnos[0][::-1].index(borrar_turnos_dni)
        if ingreso in turnos[0]:
            # Usamos el index con paso -1 para usar como índice el ultimo dato encontrado
            indice = len(turnos[0]) - 1 - turnos[0][::-1].index(ingreso)
            # Eliminamos el indice de la sublista.
            for sublistas in turnos:
                sublistas.pop(indice)
            print("Último turno eliminado con éxito")
            break
        else:
                print("DNI no econtrado")

# Funciones para printear tablas

def mostrar_tabla(diccionario):
    print(f"{'DNI':<12}{'Nombre':<20}{'Clave':<10}{'Correo':<30}{'Obra':<30}") #rebanadas
    print("-" * 90)
    
    lista_dni = diccionario["DNI"]
    lista_nombre = diccionario["Nombre"]
    lista_clave = diccionario["Clave"]
    lista_correo = diccionario["Correo"]
    lista_obra_social = diccionario["Obra"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_dni[i]):<12}{lista_nombre[i]:<20}{str(lista_clave[i]):<10}{lista_correo[i]:<30}{lista_obra_social[i]:<30}")
    return print()

def mostrar_tabla_turnos(diccionario):
    print(f"{'DNI':<12}{'Especialidad':<20}{'Doctor':<20}{'Fecha':<15}{'Precio':15}") 
    print("-" * 72)

    lista_dni = diccionario["DNI"]
    lista_especialidad = diccionario["Especialidad"]
    lista_nombre = diccionario["Doctor"]
    lista_fecha = diccionario["Fecha"]
    lista_precio = diccionario["Precio"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_dni[i]):<12}{lista_especialidad[i]:<20}{lista_nombre[i]:20}{str(lista_fecha[i]):<15}{lista_precio[i]:15}")

def mostrar_turnos_cliente(diccionario_turnos,ingreso):
    print(f"{'DNI':<12}{'Nombre':<20}{'Especialidad':<20}{'Doctor':<20}{'Fecha':<15}{'Precio':15}") 
    print("-" * 72)

    for i in range(len(diccionario_turnos["DNI"])):
        if diccionario_turnos["DNI"][i]== ingreso:
            print(f"{str(diccionario_turnos["DNI"][i]):<12}{diccionario_turnos["Nombre"][i]:<20}{diccionario_turnos["Especialidad"][i]:<20}{diccionario_turnos["Doctor"][i]:<20}{str(diccionario_turnos["Fecha"][i]):<15}{diccionario_turnos["Precio"][i]:<}")