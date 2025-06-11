from datos.datos import *
import json

def abrir_archivo(archivo):
    try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
            print("Mostrando los datos de los clientes")
            print(f'{"dni":<10}{"nombres":<20}{"contraseña":<12}{"gmail":<25}{"seguro":<20}{"activo":<20}')
            print("-" * 87)

            for usuario in usuarios:
                try:
                    dni = usuario["dni"]
                    nombre = usuario["nombre"]
                    contraseña = usuario["contraseña"]
                    gmail = usuario["gmail"]
                    seguro = usuario["seguros"]
                    if usuario["activo"] == True:
                        activo ="si"
                    else:
                        activo ="no"

                    print(f'{str(dni):<10}{nombre:<20}{contraseña:<12}{gmail:<25}{seguro:<20}{activo:<20}')
                except ValueError:
                    print("Línea con formato incorrecto")
    except (OSError,FileNotFoundError) as mensaje:
        print("Fallo todo:", mensaje)


#---------------------------------MOSTRAR MIS DATOS---------------------------
def mostrar_datos_usuarios(archivo,ingreso):
    try:
        with open (archivo,'r', encoding="UTF-8") as datos:
            usuarios = json.load(datos)
        dni = [emp["dni"] for emp in usuarios]
        indice = dni.index(ingreso)
        print("Sus datos:")
        print()
        print(f"Su Nombre y apellido: {usuarios[indice]["nombre"]}")
        print(f"Contraseña: {usuarios[indice]["contraseña"]}")
        print(f"Gmail: {usuarios[indice]["gmail"]}")
        print(f"Seguro medico: {usuarios[indice]["seguros"]}")

    except(FileNotFoundError,OSError) as error:
        print(f"fallo todo: {error}")