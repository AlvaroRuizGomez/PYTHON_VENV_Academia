"""
    FORMATEAR NÚMERO DE TELEFONO
    ----------------------------
    usuario: 666112255 y pais
    (+34)666-112-255
    (+34)666 112 255
"""

from escenarios import escenario_titulo


prefijos_del_mundo = {
    'E': '+34',
    'I': '+39',
    'R': '+86'
}


def prefijo(pais):
    if pais == 'E':
        pass
    elif pais == 'I':
        pass
    elif pais == 'R':
        pass
    else:
        print('Pais no encontrado!')
  

def formatear(tel_usuario, pais_tel):
    # *Esto es un Comprehension
    numero = [i for i in tel_usuario]
    # *Insertamos los nuevos carácteres
    numero.insert(0, '(+34)')
    numero.insert(4, '-')
    numero.insert(8, '-')
    # *Cambiamos a cadena
    numero_cadena = ''.join(numero)
    # *Cambiamos los guiones por espacios
    numero_espacios = numero_cadena.replace('-', ' ')


def run():
    escenario_titulo('F O R M A T E A R   N Ú M E R O  T E L É F O N O')
    # usuario
    tel_usuario = input('Introduce el número de teléfono: ')
    pais_tel = input("[E]spaña [I]talia [R]usia : ")
    # logica
    formatear(tel_usuario, pais_tel)
    # resultado
    print('\n', '*' * 25, 'FORMATEADO', '*' * 25, '\n')


if __name__ == "__main__":
    run()