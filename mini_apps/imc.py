"""
    App que pida el peso (en lilogramos) y la altura (en metros).
    de una persona y que calcule su indice de masa corporal(imc).
    El imc se calcula con la formula imc = peso / altura
"""
import os
import time


def imc(peso, altura):
    calculo = peso / altura**2
    # calculo = peso / pow(altura, 2)
    # calculo = peso / (altura * altura)
    return round(calculo, 2)


def escenario_titulo(titulo):
    os.system('cls')
    global peso, altura
    # * Preguntas para el usuario
    print('=' * 50, '\n')
    peso = float(input('¿Cúal es su peso?: '))
    altura = float(input('¿Cúal es su altura?: '))

    # * Resultado para el usuario
    print('?' * 50)
    time.sleep(3)

    # *inicio de script
if __name__ == "__main__":
    escenario_titulo("CÁLCULO DE ÍNDICE DE MASA CORPORAL (IMC)")
    print(f' Su imc es {imc(peso, altura)}')
    print('Un imc le puede probocar problemas coronarios')
    print('Entre 20 y 25, es el limite')
