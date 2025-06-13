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
                activo = True
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
                    "nombre": nombre + " " + apellido,
                    "gmail": gmail,
                    "seguros": obra_social,
                    "activo": activo
                    }
                usuarios.append(nuevo_usuario)

                with open(archivo,'w',encoding="UTF-8") as datos:
                    json.dump(usuarios,datos,ensure_ascii=False,indent=4)
                print(f"Se agrego {nombre + " " +  apellido}")          
    except(FileNotFoundError,OSError) as error:
        print(f"fallo todo: {error}")

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
    

#---------------------------------------------- "eliminar"---------------------------------


#------------------------------------------------------------------------------------------
#---------------------------------------------- RECURSIVIDAD ---------------------------------
#------------------------------------------------------------------------------------------

def recursividad_activos(archivo):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        
        contador = 0
        for usuario in usuarios:
            if usuario.get("activo"):
                contador += 1
        return contador

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        return 0


def recursividad_particular(archivo):
    try:
        with open(archivo, 'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        
        contador = 0
        for usuario in usuarios:
            if usuario.get("Partiular"):
                contador += 1
        return contador

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')
        return 0
    
    #VERIFICAR, NO APARENTA SER RECURSIVA
