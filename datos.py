datos_usuarios = [
    [43091220,46754741,45871266,44788110,45928020],
    ["Jijero Tomas", "FRESCA NICOLÁS","CIRIELLI LUCIANO","RADA GABRIELA","HERBAS ADRIAN"],
    ["912","115","458","441","696"],
    ["tomasjijero@jijo.com","nfresca@gmail.com","lcirielli@gmail.com","grada@gmail.com","geraldcarazani@gmail.com"]
    ]

encabezado=["DNI","Nombre","Clave", "Correo_electronico"]

diccionario_usuarios=dict(zip(encabezado, datos_usuarios))

datos_medicos = [
    ["ALVAREZ PETER","FLORES JUAN","PAREDES CARLOS","GARCIA MAXIMO","TORRES DANTE"],
    [22482796,36457774,15445213,34456789,25444123],
    ["GINECOLOGÍA","ODONTOLOGIA","PEDIATRA","CLINICO","ODONTOLOGIA"],
    ['MONSERRAT','MONSERRAT','PALERMO','PALERMO','PALERMO'],
    ['alvarezp@gmail.com','floresj@gmail.com','carlosp@gmail.com','maximog@gmail.com','torresd@gmail.com']
    ]
encabezado_medicos = ["Nombres_y_Apellidos", "DNI", "Especialidad", "Sucursal", "Correo_electronico"]

diccionarios_medicos = dict(zip(encabezado_medicos, datos_medicos))

turnos = [
    [43091220,46754741,45871266,44788110,45928020], #DNI del paciente
    ["GINECOLOGÍA","ODONTOLOGIA","PEDIATRA","CLINICO","ODONTOLOGIA"], #Especialidad
    ["ALVAREZ PETER","FLORES JUAN","PAREDES CARLOS","GARCIA MAXIMO","TORRES DANTE"], #Nombre del doc
    ["20/09/2025","06/5/2025","15/08/2025","26/07/2025","30/10/2025"], #Fecha del turno
    ]

encabezado_turnos=["DNI","Especialidad","Doctor", "Fecha"]
diccionario_turnos = dict(zip(encabezado_turnos,turnos))
