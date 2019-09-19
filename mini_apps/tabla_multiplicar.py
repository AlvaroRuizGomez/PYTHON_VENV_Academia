"""
    la tabla de multiplicar de ese numero
"""
from escenarios import escenario_titulo


def tabla_multiplicar(tabla):
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(tabla, "*", i, "=", i * tabla)


if __name__ == "__main__":
    escenario_titulo('TABLA DE MULTIPLICAR')
    # usuario
    tabla = int(input('¿Qué tabla de multiplicar necesita? :'))
    # respuesta
    tabla_multiplicar(tabla)
