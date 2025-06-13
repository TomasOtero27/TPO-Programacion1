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
                    nombre = nombre_agregado.upper()
                    especialidad = especialidad_agregado.upper()
                    arch.write("\n" + str(dni) + ";" + nombre + ";"   + gmail + "@gmail.com" + ";"  + especialidad + ";")
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

def remplazar_datos_medicos(archivo):
    try:
        # Leer archivo
        with open(archivo, "r", encoding="UTF-8") as abrir:
            lineas = abrir.readlines()
            datos_medicos = [linea.strip().split(";") for linea in lineas]
            datos_medicos = [[campo.strip() for campo in fila] for fila in datos_medicos]

        print("0 para terminar")
        while True:
            try:
                dni = input("Ingrese su DNI: ").strip()
                if dni == "0":
                    print("Volviendo...")
                    break
                encontrado = False
                for fila in datos_medicos:
                    if fila[0] == dni:
                        encontrado = True
                        print("Indique el dato a modificar")
                        print(f"1 - Nombre: {fila[1]}")
                        print(f"2 - Correo: {fila[2]}")
                        print(f"3 - Especialidad: {fila[3]}")
                        print("0 - Salir")

                        while True:
                            opcion = input("Ingrese la opción a cambiar: ").strip()
                            if opcion == "1":
                                nuevo = input("Ingrese el nuevo nombre: ").strip().title()
                                fila[1] = nuevo
                                print("Nombre actualizado.")
                            elif opcion == "2":
                                nuevo = input("Ingrese el nuevo correo: ").strip()
                                fila[2] = nuevo
                                print("Correo actualizado.")
                            elif opcion == "3":
                                nuevo = input("Ingrese la nueva especialidad: ").strip().title()
                                fila[3] = nuevo
                                print("Especialidad actualizada.")
                            elif opcion == "0":
                                break
                            else:
                                print("Opción inválida.")
                        break
                if not encontrado:
                    print("DNI no encontrado.")

            except ValueError:
                print("Se espera un número de DNI válido.")

        # Guardar archivo actualizado
        with open(archivo, "w", encoding="UTF-8") as guardado:
            for fila in datos_medicos:
                guardado.write("; ".join(fila) + "\n")

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")
