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

#-----------------------------------------------------------------------------------------------------
#---------------------------------------- funcion borrar pendiente------------------------------------
#-----------------------------------------------------------------------------------------------------
        
def borrar_datos_medicos(archivo):
    try:
        # Abrir y leer el archivo
        with open(archivo, "r", encoding="UTF-8") as f:
            lineas = f.readlines()
            datos_medicos = [linea.strip().split(";") for linea in lineas]
            datos_medicos = [[campo.strip() for campo in fila] for fila in datos_medicos]

        while True:
            dni = input("Ingrese su DNI (0 para salir): ").strip()
            if dni == "0":
                print("Saliendo de la función...")
                break

            encontrado = False
            for fila in datos_medicos:
                if fila[0] == dni:
                    encontrado = True
                    indice = datos_medicos.index(fila)
                    datos_medicos.pop(indice)
                    print(f"Médico eliminado con éxito: {dni}")
                    break  # Importante: parar el bucle para no seguir iterando

            if not encontrado:
                print(f"DNI {dni} no encontrado.")

        # Guardar cambios en el archivo
        with open(archivo, "w", encoding="UTF-8") as f:
            for fila in datos_medicos:
                f.write("; ".join(fila) + "\n")

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as error:
        print(f"Error inesperado: {error}")


#------------------------------------------------------------------------------------------------------------
#------------------------------------ funcion reemplazar-----------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def remplazar_datos_medicos(archivo):
    try:
        # Abre el txt
        with open(archivo, "r", encoding="UTF-8") as f:
            lineas = f.readlines()
            datos_medicos = [linea.strip().split(";") for linea in lineas]
            datos_medicos = [[campo.strip() for campo in fila] for fila in datos_medicos]

        print("0 para terminar")
        while True:
            try:
                dni = input("Ingrese su DNI: ").strip()
                if dni == "0":
                    print("Saliendo de la funcion....")
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
                                print("Saliendo..")
                                break
                            else:
                                print("Opción inválida.")
                        break
                if not encontrado:
                    print("DNI no encontrado.")

            except ValueError:
                print("Se espera numeros")

        # Guardar archivo actualizado
        with open(archivo, "w", encoding="UTF-8") as f:
            for fila in datos_medicos:
                f.write("; ".join(fila) + "\n")

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as error:
        print(f"Error inesperado: {error}")
