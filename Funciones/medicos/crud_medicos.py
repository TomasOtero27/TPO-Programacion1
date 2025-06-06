from datos.datos import *

#------------------------------------- 

def agregar_medicos (archivo):
    try:
        arch = open(archivo,"a", encoding="UTF-8")
    except OSError as mensaje:
        print("Fallo todo")
    else:
        print("0 para terminar")
        while True:
            try:
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
                #elif dni in dato_medicos.txt:
                    #print("DNI ya se encuentra registrado...")
                    #continue
                else:
                    nombre_agregado = input("Nombre y Apellido: ")
                    gmail = input("Gmail: ")
                    especialidad_agregado = input("Especialidad: ")
                    precio = input("Costo: ")
                    nombre = nombre_agregado.upper()
                    especialidad = especialidad_agregado.upper()
                    arch.write("\n" + str(dni) + ";" + nombre + ";"   + gmail + "@gmail.com" + ";"  + especialidad + ";"  + precio)
                    print("Agregado correctamente") 
    finally:
        try:
            arch.close()
        except NameError:
            pass

#---------------------------------------- funcion borrar pendiente
        
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

#------------------------------------ funcion reemplazar pendiente

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