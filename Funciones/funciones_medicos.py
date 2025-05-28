from datos.datos import *

def mostrar_tabla_medicos(diccionario_medicos):
    print(f"{'Nombre':<20}{'DNI':<12}{'Correo':<30}{'Especialidad':<30}{'Precio':<15}")
    print("-" * 100)
    lista_nombre = diccionario_medicos["Nombre"]
    lista_dni = diccionario_medicos["DNI"]
    lista_correo = diccionario_medicos["Correo"]
    lista_especialidad = diccionario_medicos["Especialidad"]
    lista_precio = diccionario_medicos["Precio"]

    for i in range(len(lista_dni)):
        print(f"{str(lista_nombre[i]):<20}{lista_dni[i]:<12}{lista_correo[i]:<30}{str(lista_especialidad[i]):<30}{lista_precio[i]:<15}")
        
def ordenar_usuarios_por_campo(ordenar):
    medicos = list(zip(*datos_medicos))
    medicos.sort(key=lambda medicos: medicos[ordenar])           #lambda
    for i in range(len(datos_medicos)):
        datos_medicos[i] = [medicos[i] for medicos in medicos]


def mostrar_matriz(matriz):
    print("Matriz actualizada:")
    for fila in matriz:
        print(fila)

def agregar_medicos (archivo):
    try:
        arch = open(archivo,"a", encoding="UTF-8")
        print("0 para terminar")
        dni = input("Ingrese el dni nuevo: ")
        while dni !="0":
            nombre_agregado = input("Nombre y Apellido: ")
            gmail = input("Gmail: ")
            especialidad_agregado = input("Especialidad: ")
            precio = input("Precio")
            nombre = nombre_agregado
            especialidad = especialidad_agregado
            arch.write("\n" + dni + ";" + nombre + ";"   + gmail + "gmail.com" + ";"  + especialidad + ";"  + precio)
            dni = input("Ingrese el dni nuevo: ")
        print("Agregado correctamente")
    except OSError as mensaje:
        print("Fallo todo")
    finally:
        try:
            arch.close()
        except NameError:
            pass
        
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