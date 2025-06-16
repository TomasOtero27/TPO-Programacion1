import re
from datos.datos import *
import json

def enmascarar_contraseña(contraseña):
    contraseña_enmascarada =  re.sub(r'.',"*", contraseña)
    return contraseña_enmascarada

def enmascarar_gmail(gmail):
    gmail_enmascarado = re.sub(r'^[^@]+', "*" * 10, gmail)
    return gmail_enmascarado

def separador():
    print("-" * 50)

#LAMBDA PARA VALIDAR QUE SOLO SE INGRESEN LETRAS
solo_letras = lambda s: s.isalpha()
#------------------------------------------------------------------------------
#-------------------------------- MODIFICAR DATOS------------------------------
#------------------------------------------------------------------------------

def modificar_datos_usuarios(archivo,ingreso):
    try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        dni = [emp["dni"] for emp in usuarios]
        indice = dni.index(ingreso)
        print("Indique el dato a modificar")
        print(f"1 - Nombre y apellido: {usuarios[indice]["nombre"]}")
        print(f"2 - Contraseña: {enmascarar_contraseña(usuarios[indice]["contraseña"])}")
        print(f"3 - Correo: {enmascarar_gmail(usuarios[indice]["gmail"])}")
        print(f"4 - Seguro medico: {usuarios[indice]["seguros"]}")
        print("0 - Para cerrar el menú")
        while True:
            separador()
            print("0 para terminar")
            try:
                opcion = int(input("Indique el dato a modificar: "))
            except ValueError:
                print("Se espera un número...")
                continue
            if opcion == 1:
                while True:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    if not solo_letras(nuevo_nombre):
                        print("El nombre solo debe contener letras.")
                        continue
                    elif nuevo_nombre == "":
                        print("El nombre no puede estar vacío.")
                        continue
                    else:
                        while True:
                            nuevo_apellido = input("Ingrese nuevo apellido: ")
                            if not solo_letras(nuevo_apellido):
                                print("El apellido solo debe contener letras.")
                                continue
                            elif nuevo_apellido == "":
                                print("El apellido no puede estar vacío.")
                                continue
                            else:
                                usuarios[indice]["nombre"]= nuevo_nombre.upper() + " " + nuevo_apellido.upper()
                                print(f"Nombre actualizado a: {usuarios[indice]["nombre"]}")
                                break
                        break
            elif opcion == 2:
                while True:
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    if len(nueva_contraseña) < 3:
                        print("La contraseña debe tener al menos 3 caracteres.")
                        continue
                    elif nueva_contraseña == "":
                        print("La contraseña no puede estar vacía.")
                        continue
                    else:
                        usuarios[indice]["contraseña"]= nueva_contraseña
                        print(f"Contraseña actualizada a: {enmascarar_contraseña(usuarios[indice]["contraseña"])}")
                        break
            elif opcion == 3:
                while True:
                    nuevo_gmail = input("ingrese el nuevo correo: ")
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", nuevo_gmail):
                        print("El correo electrónico no es válido.")
                        continue
                    elif nuevo_gmail == "":
                        print("El correo no puede estar vacío.")
                        continue
                    else:
                        usuarios[indice]["gmail"]= nuevo_gmail
                        print(f"Gmail actualizado a: {enmascarar_gmail(usuarios[indice]["gmail"])}")
                        break
            elif opcion == 4:
                while True:
                        print("1 - KukardoSeguros")
                        print("2 - ConsejoMate")
                        print("3 - Particular")
                        try:
                            obras = int(input("Seleccione obra social: "))
                        except ValueError:
                            print("Se espera numeros")
                            continue
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
                nueva_prepaga = prepaga
                usuarios[indice]["seguros"]= nueva_prepaga
                print(f"Seguro medico actualizado a: {usuarios[indice]["seguros"]}")
            elif opcion == 0:
                print("Cerrando el menú...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
                continue
        with open(archivo,'w',encoding="UTF-8") as datos:
            json.dump(usuarios,datos,ensure_ascii=False,indent=4)
            print("Datos actualizados con éxito.")
    except(FileNotFoundError,OSError) as error:
        print(f"Fallo todo: {error}")