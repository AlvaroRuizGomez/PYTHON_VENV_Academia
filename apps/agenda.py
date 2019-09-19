"""
    AGENDA 11 PRO
    =======
    Añadir contactos (nombre/telefono/email)
    Actualizar contactos (nombre)
    Buscar contactos (nombre)
    Eliminar contactos (nombre)
    Listar contactos
    Salir
    =====
    v1.0 (almacenará contenido en memoria)
    v2.0 (escritura en disco)
"""


import os


#from colorama import Fore, Style


# * ********************************
# * ********** CLASES
# * ********************************


class Ficha:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


class Agenda():
    # *constructor
    def __init__(self):
        self._contactos = []

    # *métodos
    # añadir contactos
    def nuevo(self, nombre, telefono, email):
        # el nuevo objeto contacto
        contacto = Ficha(nombre, telefono, email)
        # añadir introduccion de datos del usuario a la lista
        self._contactos.append(contacto)
        print("""
                Contacto añadido correctamente
        """)


    # mostrar todos los contactos
    def mostrar_todo(self):
        # self._contactos es privada no se puede llamar desde otra funcion o metodo si es una clase, ni tampoco desde fuera
        for contacto in self._contactos:
            # como imprimir los contactos en pantalla
            self._mostrar(contacto)


    def _mostrar(self, contacto):
        print('---- * -----' * 10)
        print('Nombre: {}'.format(contacto.nombre))
        print('Télefono: {}'.format(contacto.telefono))
        print('Email: {}'.format(contacto.email))
        print('----- * ------' * 10)

    def borrar(self, nombre):
        # enumerate en que posicion esta el elemento en la lista
        for idx, contacto in enumerate(self._contactos):
            if contacto.nombre.lower() == nombre.lower():
                del self._contactos[idx]
                break


    def buscar(self, nombre):
        for contacto in self._contactos:
            if contacto.nombre.lower() == nombre.lower():
                self._mostrar(contacto)
                break
        else:
            self._no_encontrado()


    # Actualizar contacto
    def actualizar(self, nombre, telefono, email):
        for contacto in self._contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto.telefono = telefono
                contacto.email = email
                break
        # este else es para el for
        else:
            self._no_encontrado()
        print("""
                Actualización correcta
        """)

    def _no_encontrado(self)  :
         print('*' * 30)
         print('!No encontrado')
         print('*' * 30)


# * *******************************
# * ********** FUNCIONES
# * *******************************
def run():
    # limpiar terminal
    os.system('cls')
    # crear objeto
    agenda_de_alvaro = Agenda()
    # bucle infinito
    while True:
        # menu para el usuario
        menu = input("""

                ¿Que quieres hacer ahora?

                [a]ñadir contacto
                [ac]tualizar contacto
                [b]uscar contacto
                [e]liminar contacto
                [l]istar contacto
                    [s]alir
        """)

        # Si el usuario elige la a de Añadir contacto
        if menu.lower() =='a':
            # Se le piden los datos necesarios al usuario
            nombre = input('Escribe el nombre de contacto :')
            telefono = input('Escribe el telefono de contacto :')
            email = input('Escribe el email de contacto :')
            # Se llama al metodo añadir contacto
            agenda_de_alvaro.nuevo(nombre, telefono, email)
            
        # Si el usuario elige la l de Actualizar contacto
        elif menu.lower() =='ac':
            # Se le piden los datos necesarios al usuario
            nombre = input('Escribe el nombre de contacto')
            telefono = input('Escribe el telefono de contacto')
            email = input('Escribe el email de contacto')
            # Se llama al metodo añadir contacto
            agenda_de_alvaro.actualizar(nombre, telefono, email)

        # Si el usuario elige la l de Añadir contacto
        elif menu.lower() =='l':
            # Se llama a la funcion _mostrar
            agenda_de_alvaro.mostrar_todo()

        # Si el usuario elige la b de Buscar contacto
        elif menu.lower() =='b':
            nombre = input('Escribe el nombre de contacto')
           # Se llama al metodo de buscar contacto
            agenda_de_alvaro.buscar()

        elif menu.lower() =='e':
            nombre = input('Escribe el nombre de contacto')
           # Se llama al metodo de buscar contacto
            agenda_de_alvaro.borrar()
            
        # Si el usuario elige s
        elif menu.lower() =='s':
            break

    

# * *******************************
# * ********** INICIO DE SCRIPT
# * *******************************
if __name__ == "__main__":
    print('*' * 70)
    print('B I E N V E N I D O  A  LA A G E N D A  DE  A L V A R O')
    # print(f'{Fore.GREEN}B I E N V E N I D O  A  LA A G E N D A  DE  A L V A R O') cuando importe Colorama para pintar con colores este titulo
    print('*' * 50)
    run()