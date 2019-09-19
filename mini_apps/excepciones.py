"""
    EXCEPCIONES
"""


def dividir(num1,num2):
    try:
        return num1/num2

    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return 'Operacion no valida'


divisor01 = float(input('Primer número'))
divisor02 = float(input('Segundo número'))

print(dividir(divisor01, divisor02))
print('Mas cosas')

print('Mas cosas')

print('Mas cosas')
