# Base de datos
# Matriz usuarios
datos_usuarios = [
    [43091220,46754741,45871266,44788110,45928020,43404608],
    ["JIJERO TOMAS", "FRESCA NICOLÁS","CIRIELLI LUCIANO","RADA GABRIELA","HERBAS ADRIAN", "JIJIJI JOJOJO"],
    ["270","115","458","441","696"],
    ["tomasjijero@jijo.com","nfresca@gmail.com","lcirielli@gmail.com","grada@gmail.com","geraldcarazani@gmail.com","ASDASDA"],
    ["UWUseguros","Particular","UWUseguros","JijazoSalud","JijazoSalud"]
    ]
 
# Convertir matriz usuarios a diccionario
encabezado=["DNI","Nombre","Clave", "Correo_electronico", "Obra_social"]
diccionario_usuarios=dict(zip(encabezado, datos_usuarios))
 
# Matriz médicos
datos_medicos = [
    ["ALVAREZ PETER","FLORES JUAN","PAREDES CARLOS","GARCIA MAXIMO","TORRES DANTE"],
    [22482796,36457774,15445213,34456789,25444123],
    ['alvarezp@gmail.com','floresj@gmail.com','carlosp@gmail.com','maximog@gmail.com','torresd@gmail.com'],
    ["GINECOLOGIA","ODONTOLOGIA","TRAUMATOLOGIA","CARDIOLOGIA","NEUROLOGIA"],
    ]
 
# Convertir matriz médicos a diccionario
encabezado_medicos = ["Nombre", "DNI", "Correo","Especialidad", "Hora"]
diccionarios_medicos = dict(zip(encabezado_medicos, datos_medicos))
 
# Matriz de turnos
turnos = [
    [43091220,46754741,45871266,44788110,45928020], # DNI del paciente
    ["Jijero tomas","Nicolad Fresca","Cirielli Luciano","Rada Gabriela","Herbas Adrian"], #Nombres de los pacientes
    ["GINECOLOGIA","ODONTOLOGIA","TRAUMATOLOGIA","CARDIOLOGIA","NEUROLOGIA"], # Especialidad
    ["ALVAREZ PETER","FLORES JUAN","PAREDES CARLOS","GARCIA MAXIMO","TORRES DANTE"], #Nombres del doc
    ["20/09/2025","06/5/2025","15/08/2025","26/07/2025","30/10/2025"], # Fecha del turno
    ["12:00","13:00","15:00","11:00","18:00"], # Hora
    ]
turnos_disponibles = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],  # ID
    ["01/06/2025", "01/06/2025", "01/06/2025",
     "02/06/2025", "02/06/2025", "02/06/2025",
     "03/06/2025", "03/06/2025", "03/06/2025",
     "04/06/2025", "04/06/2025", "04/06/2025",
     "05/06/2025", "05/06/2025", "05/06/2025"],  # Fecha
    ["08:00", "09:30", "11:00",
     "08:00", "09:30", "11:00",
     "08:00", "09:30", "11:00",
     "08:00", "09:30", "11:00",
     "08:00", "09:30", "11:00"],  # Hora
    ["ALVAREZ PETER", "ALVAREZ PETER", "ALVAREZ PETER",
     "FLORES JUAN", "FLORES JUAN", "FLORES JUAN",
     "PAREDES CARLOS", "PAREDES CARLOS", "PAREDES CARLOS",
     "GARCIA MAXIMO", "GARCIA MAXIMO", "GARCIA MAXIMO",
     "TORRES DANTE", "TORRES DANTE", "TORRES DANTE"],  # Doctor
    ["GINECOLOGIA", "GINECOLOGIA", "GINECOLOGIA",
     "ODONTOLOGIA", "ODONTOLOGIA", "ODONTOLOGIA",
     "TRAUMATOLOGIA", "TRAUMATOLOGIA", "TRAUMATOLOGIA",
     "CARDIOLOGIA", "CARDIOLOGIA", "CARDIOLOGIA",
     "NEUROLOGIA", "NEUROLOGIA", "NEUROLOGIA"],  # Especialidad
    ["disponible"] * 15  # Estado
]
 
 
# Diccionario para mostrar turnos disponibles
encabezado_turnos_disp = ["ID", "Fecha", "Hora", "Doctor", "Especialidad"]
diccionario_turnos_disp = dict(zip(encabezado_turnos_disp, turnos_disponibles))
 
# Convertir matriz turnos a diccionario
encabezado_turnos=["DNI","Nombre","Especialidad","Doctor", "Fecha","Hora"]
diccionario_turnos = dict(zip(encabezado_turnos,turnos))
 
admin = [[43404608],
         ["Tomas Otero"],
         ["912"],
         ["tomasotero499@gmail.com"]]