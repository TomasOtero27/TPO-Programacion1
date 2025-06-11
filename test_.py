from Funciones.usuarios.crud_usuarios import *

def testeo_enmascararcontraseñas():
    assert enmascarar_contraseña("912") == "***"
    assert enmascarar_contraseña("") == ""

def test_enmascarar_gmail():
    assert enmascarar_gmail("moristeenmadrid@gmail.com") == "**********@gmail.com"
    assert enmascarar_gmail("riverplate@gmail.com") == "**********@gmail.com"