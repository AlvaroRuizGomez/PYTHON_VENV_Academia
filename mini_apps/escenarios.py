"""
    ESCENARIOS
"""
import os


def escenario_titulo(titulo):
    os.system('cls')
    # * Preguntas para el usuario
    print(titulo)
    print('=' * 50, '\n')


def escenario_titulo_input(titulo, titulo_input):
    os.system('cls')
    # * Preguntas para el usuario
    print(titulo)
    print('=' * 50, '\n')
    print(input(titulo_input))
