def abrir_archivo(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as contenido:
            print("Mostrando los datos de los clientes")
            print(f'{"dni":<10}{"nombres":<20}{"contraseña":<12}{"gmail":<25}{"seguro":<20}')
            print("-" * 87)

            for linea in contenido:
                linea = linea.strip()
                if not linea:   #si linea esta vacia (datos_usuario.txt) parar
                    continue #si encuentra una linea vacia pasa al bucle
                try:
                    dni, nombres, contraseña, gmail, seguro = linea.split(";")
                    print(f'{dni.strip():<10}{nombres.strip():<20}{contraseña.strip():<12}{gmail.strip():<25}{seguro.strip():<20}')
                except ValueError:
                    print("Línea con formato incorrecto:", linea)
    except FileNotFoundError:
        print("Archivo no encontrado")
    except OSError as mensaje:
        print("Fallo todo:", mensaje)
