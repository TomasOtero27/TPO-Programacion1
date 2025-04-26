from datos import *

def mostrar_tabla_medicos(diccionario_medicos):
    print(f"{'Nombres_y_Apellidos':<20}{'DNI':<12}{'Especialidad':<20}{'Sucursal':<15}{'Correo_electronico':<30}") #rebanadas
    print("-" * 72)
    lista_nombre = diccionario_medicos["Nombres_y_Apellidos"]
    lista_dni = diccionario_medicos["DNI"]
    lista_especialidad = diccionario_medicos["Especialidad"]
    lista_sucursal = diccionario_medicos["Sucursal"]
    lista_correo = diccionario_medicos["Correo_electronico"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_nombre[i]):<20}{lista_dni[i]:<12}{str(lista_especialidad[i]):<20}{lista_sucursal[i]:<15}{lista_correo[i]:<30}")
        
def ordenar_lista_medicos(fila):
    datos_medicos[fila].sort()

def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)
def agregar_medicos (datos_medicos):
    bandera = True
    while bandera:
        extender_medicos = int(input("Ingrese DNI: "))
        if extender_medicos == -1:
            print("Cerrando agregar....")
            bandera = False
        elif extender_medicos < 11111111 or extender_medicos > 99999999:
            print("Numero invalido")
        else:
            datos_medicos[1].append(extender_medicos)
            print("DNI agregado")
            nombre = input("Ingrese el nombre y apellido: ")
            datos_medicos[0].append(nombre)
            print("Nombre agregado")
            especialidad = input("Ingrese especialidad: ")
            datos_medicos[2].append(especialidad) 
            print("Especialidad agregada")   
            sede = input("Ingrese la sede: ")
            datos_medicos[3].append(sede)   
            gmail = input("Ingrese su gmail: ")
            datos_medicos[4].append(gmail)

            return datos_medicos

def borrar_datos_medicos(datos_medicos):
    print(datos_medicos[1])
    dni = int(input("Indique el DNI: "))
    if dni in datos_medicos[1]:
        indice = datos_medicos[1].index(dni) #con el index buscamos su ubicacion de la matriz
        
        for sublistas in datos_medicos:        #usando metodo de listas, con for in
            sublistas.pop(indice)                #el pop(indice) borra todos los datos de la ubicacion 
        print(f"Usuario eliminado con éxito: {dni}")   #parametros reales pasados por nombre F{}
    else:
        print("DNI no encontrado.")
    
    return datos_medicos

def remplazar_datos_medicos(datos_medicos):
    dni = int(input("Indique DNI: "))
    if dni in datos_medicos[0]:
        indice = datos_medicos[0].index(dni)
        print("Indique que quiere modificar")
        print(f"1 - Nombre: {datos_medicos[1][indice]}")
        print(f"2 - Contraseña: {datos_medicos[2][indice]}")
        print(f"3 - Gmail: {datos_medicos[3][indice]}")
        print("4 - Para terminar")
        bandera_remplazar = True
        while bandera_remplazar:
            remplazo = int(input("Ingrese la opcion: "))
            if remplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                datos_medicos[1][indice] = nuevo_nombre
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}") 
            elif remplazo == 2:
                nueva_contraseña = int(input("Ingrese la nueva contraseña: "))
                datos_medicos[2][indice] = nueva_contraseña
                print("Contraseña cambiada....")                #USAR PARA QUE SEA TDO ##### POR SUB, VALIDAR CON DELIMITACION
            elif remplazo == 3:
                nuevo_gmail = input("Ingrese el nuevo gmail: ")
                datos_medicos[3][indice]= nuevo_gmail
                print(f"Gmail cambiado: {nuevo_gmail}")
            elif remplazo == 4:
                bandera_remplazar = False
            else:
                print("Numero no ncontrado")
    else:
        print("DNI no encontrado...")
    return datos_medicos