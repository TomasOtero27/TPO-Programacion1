from datetime import datetime
import re
from datos import *

fecha_ingresada = "25/04/2025"
fecha_usuario = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
fecha_actual = datetime.today()

def separador():
    print("-"*50)

def ordenar_lista_usuarios(fila):
    datos_usuarios[fila].sort()

def enmascarar_contraseña(contraseña):
    contraseña_enmascarada =  re.sub(r'.','*', contraseña)
    return contraseña_enmascarada

def enmascarar_gmail(gmail):
    gmail_enmascarado = re.sub(r'^[^@]+', '*' * 10, gmail)
    return gmail_enmascarado
        
    
def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)

def agregar_usuarios (datos_usuarios):
    bandera = True
    while bandera:
        extender = int(input("Ingrese DNI: "))
        if extender == -1:
            print("Cerrando menú")
            bandera = False
        elif extender < 11111111 or extender > 99999999:#----------Validacion para que realmente sea un DNI
            print("Numero invalido")
        else:
            datos_usuarios[0].append(extender)
            print("DNI agregado")
            nombre = input("Ingrese el nombre y apellido: ")
            datos_usuarios[1].append(nombre)       
            print("Nombre agregado")
            contraseña_agregar=input("Ingrese la contraseña: ")
            datos_usuarios[2].append(contraseña_agregar)
            print("Contraseña agregado")
            gmail = input("Ingrese su gmail: ")
            datos_usuarios[3].append(gmail)
            print()

            return datos_usuarios 


def realizar_turnos (turnos,datos_medicos,ingreso):
    bandera_turnos = True
    while bandera_turnos:
            # Separamos especialidad de su matriz
            especialidad_disponible = datos_medicos[2]
            # Mostrar especalidades
            separador()
            for especialidad in especialidad_disponible:
                print(especialidad)
            # Input especialidad
            separador()
            especialidad_turno = input(f"Ingrese la especialidad: ")
            # Lista por comprensión
            patron = [especialidad for especialidad in especialidad_disponible if re.search(especialidad_turno,especialidad,re.IGNORECASE)]
            if len(patron) > 0:
                especialidad_turno = patron[0]
                print(f"Especialidad elegida: {especialidad_turno}")
                # Fecha
                fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")
                # Validacion de la fecha en formato DD/MM/AAAA
                if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
                    # Slicing
                    dia = int(fecha[:2])
                    mes = int(fecha[3:5])
                    anio = int(fecha[6:])
                    if (1 <= dia <= 31) and (1 <= mes <= 12):
                        fecha_valida = datetime(anio, mes, dia)
                        if fecha_valida >= datetime.today():#------------------ datatime de una bibliote
                            turnos[0].append(ingreso) # DNI Paciente
                            turnos[1].append(especialidad_turno) # Especialidad
                            indice = datos_medicos[2].index(especialidad_turno) 
                            turnos[2].append(datos_medicos[0][indice]) # Nombre médico
                            turnos[3].append(fecha_valida.strftime("%d/%m/%Y")) # Fecha turno
                            turnos[4].append(datos_medicos[3][indice]) # Lugar

                            print(" Turno registrado con éxito.")
                            separador()
                            # Mostrar los datos del último turno
                            dni = turnos[0][-1]
                            especialidad = turnos[1][-1]
                            nombre = turnos[2][-1]
                            fecha = turnos[3][-1]
                            lugar = turnos[4][-1]
                            # Print
                            print(f"DNI: {dni}")
                            print(f"Especialidad: {especialidad}")
                            print(f"Doctor: {nombre}")
                            print(f"Fecha del turno: {fecha}")
                            print(f"Sede del turno: {lugar}")
                            bandera_turnos = False
                        else:
                            print(" No se pueden elegir fechas anteriores a hoy.")
                    else:
                            print(" Fecha inválida.") 
                else:
                        print(" Formato de fecha incorrecto.") 
            else:
                print(" Especialidad no encontrada.")
    return 

#---------------------------------------- Indico el DNI del usuario y borro los datos datos vinculados -------------------------------------------------           

def borrar_datos_usuarios(datos_usuarios):
    print(datos_usuarios[0])
    dni = int(input("Indique el DNI: "))
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni) #con el index buscamos su ubicacion de la matriz
        
        for sublistas in datos_usuarios:        #usando metodo de listas, con for in
            sublistas.pop(indice)                #el pop(indice) borra todos los datos de la ubicacion 
        print(f"Usuario eliminado con éxito: {dni}")
    else:
        print("DNI no encontrado.")
    
    return datos_usuarios
    
    #---------------------------------------- Busco y remplazo los datos del usuario segun su DNI ------------------------------------------------           
    
def remplazar_datos_usuarios(datos_usuarios):
    dni = int(input("Indique DNI: "))
    if dni in datos_usuarios[0]:
        indice = datos_usuarios[0].index(dni)
        print("Indique que quiere modificar")
        print(f"1 - Nombre: {datos_usuarios[1][indice]}")
        print(f"2 - Contraseña: {enmascarar_contraseña(datos_usuarios[2][indice])}")
        print(f"3 - Gmail: {enmascarar_gmail(datos_usuarios[3][indice])}")
        print("4 - Para terminar")
        bandera_remplazar = True
        while bandera_remplazar:
            remplazo = int(input("Ingrese la opcion: "))
            if remplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                datos_usuarios[1][indice] = nuevo_nombre.title()
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}") #title para que ponga mayuscula las palabras
            elif remplazo == 2:
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                datos_usuarios[2][indice] = nueva_contraseña
                print("Contraseña cambiada....")                #USAR PARA QUE SEA TDO ##### POR SUB, VALIDAR CON DELIMITACION
            elif remplazo == 3:
                nuevo_gmail = input("Ingrese el nuevo gmail: ")
                datos_usuarios[3][indice]= nuevo_gmail
                print(f"Gmail cambiado: {nuevo_gmail}")
            elif remplazo == 4:
                bandera_remplazar = False
            else:
                print("Numero no ncontrado")
    else:
        print("DNI no encontrado...")
    return 

def borrar_turnos(turnos):
    print("Ingrese 2 para terminar")
    borrar_turnos_dni= int(input("Ingrese su dni: "))
    if borrar_turnos_dni in turnos[0]:
        indice = turnos[0].index(borrar_turnos_dni)
        for sublistas in turnos:
            sublistas.pop(indice)
        print("Turno eliminado con exito")
    else:
        print("DNI no econtrado")



def mostrar_tabla(diccionario):
    print(f"{'DNI':<12}{'Nombre':<20}{'Clave':<10}{'Correo_electronico':<30}") #rebanadas
    print("-" * 72)
    
    lista_dni = diccionario["DNI"]
    lista_nombre = diccionario["Nombre"]
    lista_clave = diccionario["Clave"]
    lista_correo = diccionario["Correo_electronico"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_dni[i]):<12}{lista_nombre[i]:<20}{str(lista_clave[i]):<10}{lista_correo[i]:<30}")
    return print()

def mostrar_tabla_turnos(diccionario):
    print(f"{'DNI':<12}{'Especialidad':<20}{'Doctor':<10}{'Fecha':<30}") #rebanadas
    print("-" * 72)

    lista_dni = diccionario["DNI"]
    lista_especialidad = diccionario["Especialidad"]
    lista_nombre = diccionario["Doctor"]
    lista_fecha = diccionario["Fecha"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_dni[i]):<12}{lista_especialidad[i]:<20}{lista_nombre[i]:<20}{str(lista_fecha[i]):<30}")

def mostrar_turnos_cliente(diccionario_turnos):
    dni = int(input("Ingrese el dni: "))
    print(f"{'DNI':<12}{'Especialidad':<20}{'Doctor':<10}{'Fecha':<30}") #rebanadas
    print("-" * 72)

    for i in range(len(diccionario_turnos["DNI"])):
        if diccionario_turnos["DNI"][i]== dni:
            print(f"{str(diccionario_turnos['DNI'][i]):<12}{diccionario_turnos['Especialidad'][i]:<20}{diccionario_turnos['Doctor'][i]:<20}{str(diccionario_turnos['Fecha'][i]):<30}")