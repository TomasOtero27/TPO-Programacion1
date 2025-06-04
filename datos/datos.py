# Base de datos
# Diccionario de usuarios
"""datos_usuarios = {
    43091220: {
        'contraseña': "270",
        'Nombre': "JIJERO TOMAS",
        'Gmail': "tomasjijero@jijo.com",
        'Seguros': "KukardosSeguros"
    },
    46754741: {
        'contraseña': "115",
        'Nombre': "FRESCA NICOLÁS",
        'Gmail': "nfresca@gmail.com",
        'Seguros': "Particular"
    },
    45871266: {
        'contraseña': "458",
        'Nombre': "CIRIELLI LUCIANO",
        'Gmail': "lcirielli@gmail.com",
        'Seguros': "KukardosSeguros"
    },
    44788110: {
        'contraseña': "441",
        'Nombre': "RADA GABRIELA",
        'Gmail': "grada@gmail.com",
        'Seguros': "ConsejoMate"
    },
    45928020:{
        'contraseña': "696",
        'Nombre': "HERBAS ADRIAN",
        'Gmail': "geraldcarazani@gmail.com",
        'Seguros': "ConsejoMate"
    }
}
"""

# Matriz médicos
datos_medicos = [
    ["ALVAREZ PETER","FLORES JUAN","PAREDES CARLOS","GARCIA MAXIMO","TORRES DANTE"],
    [22482796,36457774,15445213,34456789,25444123],
    ['alvarezp@gmail.com','floresj@gmail.com','carlosp@gmail.com','maximog@gmail.com','torresd@gmail.com'],
    ["GINECOLOGIA","ODONTOLOGIA","TRAUMATOLOGIA","CARDIOLOGIA","NEUROLOGIA"],
    [10000,20000,30000,40000,50000]
    ]

# Convertir matriz médicos a diccionario
encabezado_medicos = ["Nombre", "DNI", "Correo","Especialidad", "Precio"]
diccionarios_medicos = dict(zip(encabezado_medicos, datos_medicos))

# Matriz de turnos
turnos = [
    [43091220,46754741,45871266,44788110,45928020], # DNI del paciente
    ["JIJERO TOMAS","FRESCA NICOLÁS","CIRIELLI LUCIANO","RADA GABRIELA","HERBAS ADRIAN"], #Nombres de los pacientes
    ["GINECOLOGIA","ODONTOLOGIA","TRAUMATOLOGIA","CARDIOLOGIA","NEUROLOGIA"], # Especialidad
    ["ALVAREZ PETER","FLORES JUAN","PAREDES CARLOS","GARCIA MAXIMO","TORRES DANTE"], #Nombres del doc
    ["20/09/2025","06/5/2025","15/08/2025","26/07/2025","30/10/2025"], # Fecha del turno
    [10000,20000,30000,40000,50000], # Costo
    ]

# Convertir matriz turnos a diccionario
encabezado_turnos=["DNI","Nombre","Especialidad","Doctor", "Fecha","Precio"]
diccionario_turnos = dict(zip(encabezado_turnos,turnos))


admin = {
    43404608: "912", 
    222: "222"
}




"""admin = [[43404608, 222],
         ["Tomas Otero", "admin"],
         ["912", "222"],
         ["tomasotero499@gmail.com", "correo"]]"""


"""
# Convertir matriz usuarios a diccionario
encabezado=["DNI","Nombre","Clave", "Correo", "Obra"]
diccionario_usuarios=dict(zip(encabezado, datos_usuarios))"""

datos_usuarios = [
    [43091220,46754741,45871266,44788110,45928020],
    ["JIJERO TOMAS", "FRESCA NICOLÁS","CIRIELLI LUCIANO","RADA GABRIELA","HERBAS ADRIAN"],
    ["270","115","458","441","696"],
    ["tomasjijero@jijo.com","nfresca@gmail.com","lcirielli@gmail.com","grada@gmail.com","geraldcarazani@gmail.com"],
    ["UWUseguros","Particular","UWUseguros","JijazoSalud","JijazoSalud"]
    ]