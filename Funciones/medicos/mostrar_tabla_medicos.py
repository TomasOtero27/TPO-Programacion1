def abrir_archivo_medicos(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as contenido:
            print(f'{"dni":<10}{"nombres":<20}{"Gmail":<25}{"Especialidad":<25}')
            print("-" * 87)

            for linea in contenido:
                linea = linea.strip()
                if not linea:   #si linea esta vacia (datos_usuario.txt) parar
                    continue #si encuentra una linea vacia pasa directo al bucle
                try:
                    dni, nombres, gmail, especialidad= linea.split(";")
                    print(f'{dni.strip():<10}{nombres.strip():<20}{gmail.strip():<25}{especialidad.strip():<25}')
                except ValueError:
                    print("Línea con formato incorrecto:", linea)
            print("-" * 87)
            
    except FileNotFoundError:
        print("Archivo no encontrado")
    except OSError as mensaje:
        print("Fallo todo:", mensaje)