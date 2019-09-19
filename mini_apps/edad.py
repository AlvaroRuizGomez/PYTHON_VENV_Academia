"""
    EDAD
"""


def opinarEdad(edad):
    if edad < 20:
        raise NameError('No se permiten edades negativas')   
    if edad < 40:
        return 'eres joven'
    elif edad < 70:
        return 'eres maduro'
    elif edad < 120:
        return 'Cuidate'

try:
    print(opinarEdad(-4))

except NameError as err:
    print(err)


print('Mas cosas')

print('Mas cosas')

print('Mas cosas')
