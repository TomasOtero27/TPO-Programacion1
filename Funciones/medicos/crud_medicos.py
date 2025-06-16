from datos.datos import *
import re

#------------------------------------- 
def separador():
    print("-" * 50)

def agregar_medicos (archivo):
    try:
        arch = open(archivo,"a", encoding="UTF-8")
    except OSError as mensaje:
        print(f"Fallo todo {mensaje}")
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
                    continue 
            # Validamos si el DNI ya existe
                with open(archivo, "r", encoding="UTF-8") as f:
                    lineas = f.readlines()
                    for linea in lineas:
                        if str(dni) in linea:
                            print("El DNI ya existe, por favor ingrese otro.")
                            break
                    #continue
                    else:
                        while True:
                            nombre_agregado = input("Ingrese el nombre: ").strip().upper()
                            if not nombre_agregado.isalpha():
                                print("El nombre debe contener solo letras.")
                                continue
                            elif nombre_agregado == "":
                                print("El nombre no puede estar vacío.")
                                continue
                            else:
                                break
                        while True:
                            apellido = input("Ingrese su apellido: ").strip().upper()
                            if apellido == "":
                                print("El apellido no puede estar vacío. Intente nuevamente.")
                            elif not apellido.isalpha():
                                print("El apellido solo puede contener letras. Intente nuevamente.")
                            else:
                                break
                        nombref = nombre_agregado + " " + apellido
                        while True:
                            gmail = input("Ingrese su correo: ")
                            # Validamos el formato del correo como cadena
                            # Empieza con cualquier cosa que no sea '@', contiene '@' y termina con un dominio
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", gmail):
                                print("Correo inválido. Debe contener '@' y finalizar con un dominio. Intente nuevamente.")
                            elif gmail == "":
                                print("El correo no puede estar vacío. Intente nuevamente.")
                            else:
                                break
                        while True:
                            especialidad_agregado = input("Especialidad: ")
                            if especialidad_agregado == "":
                                print("La especialidad no puede estar vacía. Intente nuevamente.")
                            elif not especialidad_agregado.isalpha():
                                print("La especialidad solo puede contener letras. Intente nuevamente.")
                            else:
                                break
                        nombre = nombref.upper()
                        especialidad = especialidad_agregado.upper()
                        arch.write("\n" + str(dni) + ";" + nombre + ";"   + gmail  + ";"  + especialidad)
                        print("Agregado correctamente") 
    finally:
        try:
            arch.close()
        except NameError:
            pass

#-----------------------------------------------------------------------------------------------------
#---------------------------------------- funcion borrar------------------------------------
#-----------------------------------------------------------------------------------------------------
        
def borrar_datos_medicos(archivo):
    try:
        # Abrir y leer el archivo
        with open(archivo, "r", encoding="UTF-8") as f:
            lineas = f.readlines()
            datos_medicos = [linea.strip().split(";") for linea in lineas]
            datos_medicos = [[campo.strip() for campo in fila] for fila in datos_medicos]

        while True:
            dni = input("Ingrese el DNI a modificar (0 para salir): ").strip()
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
        while True:
            try:
                dni = input("Ingrese el DNI a modificar (0 para salir): ").strip()
                if dni == "0":
                    print("Saliendo de la función....")
                    break
                encontrado = False
                for fila in datos_medicos:
                    if fila[0] == dni:
                        encontrado = True
                        while True:
                            separador()
                            print("Indique el dato a modificar")
                            print(f"1 - Nombre: {fila[1]}")
                            print(f"2 - Correo: {fila[2]}")
                            print(f"3 - Especialidad: {fila[3]}")
                            print("0 - Salir")
                            separador()
                            try:
                                opcion = int(input("Ingrese la opción a cambiar: "))
                            except ValueError:
                                print("Se espera un número.")
                                continue
                            if opcion == 1:
                                while True:
                                    nuevo = input("Ingrese el nuevo nombre: ").strip()
                                    if not nuevo.isalpha():
                                        print("El nombre debe contener solo letras.")
                                        continue
                                    elif nuevo == "":
                                        print("El nombre no puede estar vacío.")
                                        continue
                                    else:
                                        apellido = input("Ingrese el apellido: ").strip()
                                        if not apellido.isalpha():
                                            print("El apellido debe contener solo letras.")
                                            continue
                                        elif apellido == "":
                                            print("El apellido no puede estar vacío.")
                                            continue
                                        else:
                                            nuevo = nuevo + " " + apellido
                                            nuevo = nuevo.upper()
                                            fila[1] = nuevo
                                            print("Nombre actualizado.")
                                            break
                            elif opcion == 2:
                                while True:
                                    nuevo = input("Ingrese el nuevo correo: ")
                                    if not re.match(r"[^@]+@[^@]+\.[^@]+", nuevo):
                                        print("Correo inválido. Debe contener '@' y finalizar con un dominio.")
                                        continue
                                    elif nuevo == "":
                                        print("El correo no puede estar vacío.")
                                        continue
                                    else:
                                        fila[2] = nuevo
                                        print("Correo actualizado.")
                            elif opcion == 3:
                                nuevo = input("Ingrese la nueva especialidad: ").strip().title()
                                fila[3] = nuevo
                                print("Especialidad actualizada.")
                            elif opcion == 0:
                                print("Saliendo...")
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
