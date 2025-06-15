import re
from datos.datos import *
import json

def enmascarar_contraseña(contraseña):
    contraseña_enmascarada =  re.sub(r'.',"*", contraseña)
    return contraseña_enmascarada

def enmascarar_gmail(gmail):
    gmail_enmascarado = re.sub(r'^[^@]+', "*" * 10, gmail)
    return gmail_enmascarado


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
            print(f"4 - Seguro medico: {usuarios[indice]["seguros"]}")
            print("0 - Para cerrar el menú")
            while True:
                opcion = input("Indique el dato a modificar: ")
                if opcion == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    nuevo_apellido = input("Ingrese nuevo apellido: ")
                    print("Modificado")
                    usuarios[indice]["nombre"]= nuevo_nombre.upper() + " " + nuevo_apellido.upper()
                elif opcion == "2":
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    print("Modificado")
                    usuarios[indice]["contraseña"]= nueva_contraseña
                elif opcion == "3":
                    nuevo_gmail = input("ingrese el nuevo gmail: ")
                    print("Modificado")
                    usuarios[indice]["gmail"]= nuevo_gmail
                elif opcion == "4":
                    while True:
                            print("1- KukardosSeguros")
                            print("2- ConsejoMate")
                            print("3- Particular")
                            try:
                                obras = int(input("Seleccione obra social: "))
                                while obras < 1 or obras > 3:
                                    print("Opción incorrecta")
                                    obras = int(input("Seleccione una opción: "))
                                if obras == 1:
                                    prepaga = "KukardosSeguros"
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
                    print("Modificado")
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
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        while True:
            try:
                dni = int(input("Ingrese el DNI: "))
                if dni == 0:
                    print("Volviendo al menú principal...")
                    return
                elif dni < 11111111 or dni > 99999999:
                    print("DNI inválido. Intente nuevamente.")
                    continue
            except ValueError:
                print("Se esperan números válidos.")
                continue

            # Verificar si el DNI ya existe
            existe = False
            for usuario in usuarios:
                if usuario["dni"] == dni:
                    existe = True
                    break

            if existe:
                print("Usuario con ese DNI ya existe. Intente con otro.")
            else:
                break

        nombre = input("Ingrese su nombre: ").strip().upper()
        apellido = input("Ingrese su apellido: ").strip().upper()
        gmail = input("Ingrese su gmail: ")
        contraseña = input("Ingrese su contraseña: ")
        activo = True

        while True:
            print("1- KukardosSeguros")
            print("2- ConsejoMate")
            print("3- Particular")
            try:
                obras = int(input("Seleccione obra social: "))
                if obras < 1 or obras > 3:
                    print("Opción incorrecta. Intente nuevamente.")
                    continue
                if obras == 1:
                    obra_social = "KukardosSeguros"
                elif obras == 2:
                    obra_social = "ConsejoMate"
                else:
                    obra_social = "Particular"
                break
            except ValueError:
                print("Se espera un número.")

        nuevo_usuario = {
            "dni": dni,
            "contraseña": contraseña,
            "nombre": nombre + " " + apellido,
            "gmail": gmail,
            "seguros": obra_social,
            "activo": activo
        }

        usuarios.append(nuevo_usuario)

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(usuarios, datos, ensure_ascii=False, indent=4)

        print(f"Se agregó el usuario {nombre} {apellido} correctamente.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error al acceder al archivo: {error}")


#--------------------------------------------------- ELIMINAR USUARIOS -------------

def eliminar_usuario(archivo, busqueda):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        dni = [emp["dni"] for emp in usuarios]
        if busqueda in dni:
            indice = dni.index(busqueda)
            usuarios.pop(indice)  # Elimina el empleado por índice

            with open(archivo, 'w', encoding="UTF-8") as datos:
                json.dump(usuarios, datos, ensure_ascii=False, indent=4)
            print(f"Usuario con DNI: {busqueda} eliminado.")
        else:
            print(f"Usuario con DNI: {dni} no encontrado.")

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
    

#---------------------------------------------- "ELIMINAR"---------------------------------
def desactivar_usuario(archivo):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        try:
            dni = int(input("Ingrese el DNI del usuario a desactivar: "))
        except ValueError:
            print("Se espera un número válido.")
            return

        encontrado = False
        for usuario in usuarios:
            if usuario["dni"] == dni:
                if usuario["activo"] == False:
                    print("El usuario ya esta dado de baja.")
                else:
                    usuario["activo"] = False
                    encontrado = True
                break

        if encontrado:
            with open(archivo, 'w', encoding="UTF-8") as datos:
                json.dump(usuarios, datos, ensure_ascii=False, indent=4)
            print(f"El usuario con DNI {dni} fue desactivado correctamente.")
        else:
            print(f"No se encontró un usuario con DNI {dni}.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error al acceder al archivo: {error}")

#---------------------------------------------------------------------
#----------------------------------------ALTA-------------------------
#---------------------------------------------------------------------

def reactivar_usuario(archivo):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        try:
            dni = int(input("Ingrese el DNI del usuario a reactivar: "))
        except ValueError:
            print("Se espera un número válido.")
            return

        encontrado = False
        for usuario in usuarios:
            if usuario["dni"] == dni:
                if usuario["activo"] == True:
                    print("El usuario ya esta dado de alta.")
                else:
                    usuario["activo"] = True
                    encontrado = True
                break

        if encontrado:
            with open(archivo, 'w', encoding="UTF-8") as datos:
                json.dump(usuarios, datos, ensure_ascii=False, indent=4)
            print(f"El usuario con DNI {dni} fue reactivado correctamente.")
        else:
            print(f"No se encontró un usuario con DNI {dni}.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error al acceder al archivo: {error}")
#------------------------------------------------------------------------------------------
#---------------------------------------------- RECURSIVIDAD ---------------------------------
#------------------------------------------------------------------------------------------

def recursividad_activos(archivo, f = 0):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        if f == len(usuarios):
            return 0
        else:
            if usuarios[f]["activo"] == True:
                contador = 1
            else:
                contador = 0
            return contador + recursividad_activos(archivo, f + 1)

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')


def recursividad_seguros_kukardo(archivo, f=0):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        if f == len(usuarios):
            return 0
        else:
            contador = 0
            if usuarios[f]["seguros"] == "KukardosSeguros" and usuarios[f]["activo"] == True:
                contador += 1
            return contador + recursividad_seguros_kukardo(archivo, f + 1)

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')


def recursividad_seguros_consejo(archivo, f=0):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        if f == len(usuarios):
            return 0
        else:
            contador = 0
            if usuarios[f]["seguros"] == "ConsejoMate" and usuarios[f]["activo"] == True:
                contador += 1
            return contador + recursividad_seguros_consejo(archivo, f + 1)

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')

def recursividad_particular(archivo, f=0):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)

        if f == len(usuarios):
            return 0
        else:
            contador = 0
            if usuarios[f]["seguros"] == "Particular" and usuarios[f]["activo"] == True:
                contador += 1
            return contador + recursividad_particular(archivo, f + 1)

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')