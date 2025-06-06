import re
from datos.datos import *
import json

def enmascarar_contraseña(contraseña):
    contraseña_enmascarada =  re.sub(r'.',"*", contraseña)
    return contraseña_enmascarada

def enmascarar_gmail(gmail):
    gmail_enmascarado = re.sub(r'^[^@]+', "*" * 10, gmail)
    return gmail_enmascarado

#------------------------------------------ Terminar borrar datos

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

#-------------------------------- MODIFICAR DATOS------------------------------


def modificar_datos_usuarios(archivo,ingreso):
   try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        dni = [emp["dni"] for emp in usuarios]
        indice = dni.index(ingreso)
        print("Indique el dato a modificar")
        print(f"1 - Su Nombre y apellido: {usuarios[indice]["nombre"]}")
        print(f"2 - Contraseña: {enmascarar_contraseña(usuarios[indice]["contraseña"])}")
        print(f"3 - Gmail: {enmascarar_gmail(usuarios[indice]["gmail"])}")
        print(f"4- Seguro medico: {usuarios[indice]["seguros"]}")
        print("0 - Para cerrar el menú")
        while True:
            opcion = input("Indique el dato a modificar: ")
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_apellido = input("Ingrese nuevo apellido: ")
                usuarios[indice]["nombre"]= nuevo_nombre.upper() + " " + nuevo_apellido.upper()
            elif opcion == "2":
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                usuarios[indice]["contraseña"]= nueva_contraseña
            elif opcion == "3":
                nuevo_gmail = input("ingrese el nuevo gmail: ")
                usuarios[indice]["gmail"]= nuevo_gmail
            elif opcion == "4":
                while True:
                        print("1- KukardoSeguros")
                        print("2- ConsejoMate")
                        print("3- Particular")
                        try:
                            obras = int(input("Seleccione obra social: "))
                            while obras < 1 or obras > 3:
                                print("Opción incorrecta")
                                obras = int(input("Seleccione una opción: "))
                            if obras == 1:
                                prepaga = "KukardoSeguros"
                                break
                            elif obras == 2:
                                prepaga = "ConsejoMate"
                                break
                            elif obras == 3:
                                prepaga = "Particular"
                                break
                            else:
                                print(f"Numero incorrecto: {obras}")
                        except ValueError:
                            print("Se espera numeros")
                nueva_prepaga = prepaga
                usuarios[indice]["seguros"]= nueva_prepaga
            elif opcion == "0":
                break
            else:
                print(f"Incorrecto: {opcion}")
        with open(archivo,'w',encoding="UTF-8") as datos:
            json.dump(usuarios,datos,ensure_ascii=False,indent=4)
            print("Datos actualizados con éxito.")

   except(FileNotFoundError,OSError) as error:
        print(f"fallo todo: {error}")

#------------------------------------------------------------------------------------------

#----------------------------------SOLO FUNCIONES PARA ADMIN-------------------------------

def modificar_datos_usuarios_admin(archivo, busqueda):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        dni = [emp["dni"] for emp in usuarios]
        if busqueda in dni:
            # Obtener índice del empleado y modificar
            indice = dni.index(busqueda)
            print("Indique el dato a modificar")
            print(f"1 - Su Nombre y apellido: {usuarios[indice]["nombre"]}")
            print(f"2 - Contraseña: {enmascarar_contraseña(usuarios[indice]["contraseña"])}")
            print(f"3 - Gmail: {enmascarar_gmail(usuarios[indice]["gmail"])}")
            print(f"4- Seguro medico: {usuarios[indice]["seguros"]}")
            print("0 - Para cerrar el menú")
            while True:
                opcion = input("Indique el dato a modificar: ")
                if opcion == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    nuevo_apellido = input("Ingrese nuevo apellido: ")
                    usuarios[indice]["nombre"]= nuevo_nombre.upper() + " " + nuevo_apellido.upper()
                elif opcion == "2":
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    usuarios[indice]["contraseña"]= nueva_contraseña
                elif opcion == "3":
                    nuevo_gmail = input("ingrese el nuevo gmail: ")
                    usuarios[indice]["gmail"]= nuevo_gmail
                elif opcion == "4":
                    while True:
                            print("1- KukardoSeguros")
                            print("2- ConsejoMate")
                            print("3- Particular")
                            try:
                                obras = int(input("Seleccione obra social: "))
                                while obras < 1 or obras > 3:
                                    print("Opción incorrecta")
                                    obras = int(input("Seleccione una opción: "))
                                if obras == 1:
                                    prepaga = "KukardoSeguros"
                                    break
                                elif obras == 2:
                                    prepaga = "ConsejoMate"
                                    break
                                elif obras == 3:
                                    prepaga = "Particular"
                                    break
                                else:
                                    print(f"Numero incorrecto: {obras}")
                            except ValueError:
                                print("Se espera numeros")
                    nueva_prepaga = prepaga
                    usuarios[indice]["seguros"]= nueva_prepaga
                elif opcion == "0":
                    break
                else:
                    print(f"Incorrecto: {opcion}")
            with open(archivo, 'w', encoding="UTF-8") as datos:
                json.dump(usuarios, datos, ensure_ascii=False, indent=4)

            print("Modificado")
        else:
            print(f"Usuario con DNI {busqueda} no encontrado.")

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')

#--------------------------------------------------- AGREGAR USUARIOS -------------

def agregar_usuarios(archivo):
    try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        if usuarios:
                while True:
                    try:
                        dni = int(input("Ingrese el DNI: "))
                        break
                    except ValueError:
                        print("Se espera numeros")
                nombre=input("Ingrese su nombre: ").strip().upper()
                apellido=input("Ingrese su apellido: ").strip().upper()
                gmail=input("Ingrese su gmail: ")
                contraseña=input("Ingrese su contraseña: ")
                while True:
                        print("1- KukardoSeguros")
                        print("2- PolentaPrestoPronta")
                        print("3- Particular")
                        try:
                            obras = int(input("Seleccione obra social: "))
                            while obras < 1 or obras > 3:
                                print("Opción incorrecta")
                                obras = int(input("Seleccione una opción: "))
                            if obras == 1:
                                prepaga = "KukardoSeguros"
                                break
                            elif obras == 2:
                                prepaga = "ConsejoMate"
                                break
                            elif obras == 3:
                                prepaga = "Particular"
                                break
                        except ValueError:
                            print("Se espera numeros")
                obra_social = prepaga

                nuevo_usuario= {
                    "dni": dni,
                    "contraseña": contraseña,
                    "Nombre": nombre + " " + apellido,
                    "Gmail": gmail,
                    "Seguros": obra_social
                    }
                usuarios.append(nuevo_usuario)

                with open(archivo,'w',encoding="UTF-8") as datos:
                    json.dump(usuarios,datos,ensure_ascii=False,indent=4)
                print(f"Se agrego {nombre + " " +  apellido}")          
    except(FileNotFoundError,OSError) as error:
        print(f"fallo todo: {error}")

#--------------------------------------------------- ELIMINAR USUARIOS -------------

def eliminar_por_legajo(archivo, legajo):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            empleados = json.load(datos)

        legajos = [emp["legajo"] for emp in empleados]
        if legajo in legajos:
            indice = legajos.index(legajo)
            empleados.pop(indice)  # Elimina el empleado por índice

            with open(archivo, 'w', encoding="UTF-8") as datos:
                json.dump(empleados, datos, ensure_ascii=False, indent=4)
            print(f"Empleado con legajo {legajo} eliminado.")
        else:
            print(f"Empleado con legajo {legajo} no encontrado.")

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
