from datos import *

def mostrar_tabla_medicos(diccionario_medicos):
    print(f"{'Nombre':<20}{'DNI':<12}{'Especialidad':<20}{'Sucursal':<15}{'Correo':<30}")
    print("-" * 72)
    lista_nombre = diccionario_medicos["Nombre"]
    lista_dni = diccionario_medicos["DNI"]
    lista_especialidad = diccionario_medicos["Especialidad"]
    lista_sucursal = diccionario_medicos["Sucursal"]
    lista_correo = diccionario_medicos["Correo"]

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
        if extender_medicos < 11111111 or extender_medicos > 99999999:
            print("Numero invalido")
        else:
            datos_medicos[1].append(extender_medicos)
            print("DNI agregado")
            nombre = input("Ingrese el nombre y apellido: ")
            datos_medicos[0].append(nombre.title())
            print("Nombre agregado")
            especialidad = input("Ingrese especialidad: ")
            datos_medicos[2].append(especialidad.title()) 
            print("Especialidad agregada")   
            sede = input("Ingrese la sede: ")
            datos_medicos[3].append(sede.title())   
            gmail = input("Ingrese su gmail: ")
            datos_medicos[4].append(gmail)
            print("Médico creado con éxito")
            bandera = False

def borrar_datos_medicos(datos_medicos):
    for datos in datos_medicos[1]:
        print(datos, end=" ")
    dni = int(input("\nIndique el DNI: "))
    if dni in datos_medicos[1]:
        indice = datos_medicos[1].index(dni) #con el index buscamos su ubicacion de la matriz
        
        for sublistas in datos_medicos:        #usando metodo de listas, con for in
            sublistas.pop(indice)                #el pop(indice) borra todos los datos de la ubicacion 
        print(f"Médico eliminado con éxito: {dni}")   #parametros reales pasados por nombre F{}
    else:
        print("DNI no encontrado.")

def remplazar_datos_medicos(datos_medicos):
    dni = int(input("Indique DNI: "))
    if dni in datos_medicos[1]:
        indice = datos_medicos[1].index(dni)
        print("Indique el dato a modificar")
        print(f"1 - Nombre: {datos_medicos[0][indice]}")
        print(f"2 - Especialidad: {datos_medicos[2][indice]}")
        print(f"3 - Sede: {datos_medicos[3][indice]}")
        print(f"4 - Correo: {datos_medicos[4][indice]}")
        print("0 - Cerrar menú")
        bandera_remplazar = True
        while bandera_remplazar:
            reemplazo = int(input("Ingrese la opción a cambiar: "))
            if reemplazo == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                datos_medicos[0][indice] = nuevo_nombre.title()
                print(f"Nuevo nombre agregado: {nuevo_nombre.title()}") 
            elif reemplazo == 2:
                nueva_especialidad =input("Ingrese la nueva especialidad: ")
                datos_medicos[2][indice] = nueva_especialidad.title()
                print(f"Especialidad cambiada: {nueva_especialidad.title()}")   
            elif reemplazo == 3:
                nueva_sede = input("Ingrese la nueva sede: ")
                datos_medicos[3][indice] = nueva_sede
            elif reemplazo == 4:
                nuevo_gmail = input("Ingrese el nuevo gmail: ")
                datos_medicos[4][indice]= nuevo_gmail
                print(f"Correo cambiado: {nuevo_gmail}")
            elif reemplazo == 0:
                bandera_remplazar = False
            else:
                print("Parámetro no encontrado")
    else:
        print("DNI no encontrado")