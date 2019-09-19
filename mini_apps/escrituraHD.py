""" 
    Python escritura en disco
    --------------------------

    Puede leer y escribir archivos con la funcion (open)
    Los archivos pueden ser de texto o binario

    Manejadores:
    * r = read
    * w = write
    * a = apped
    * r+ = read and write
    Se deben cerrar los archivos con el metodo (close)
    Una de las mejores maneras de manejar archivos es con (with)
"""


nombre = input('Tu nombre: ')

# * Escritura
with open('file.txt', 'w') as f:
    for i in range(5):
        f.write(f'{nombre}\n')
    f.close()

# f = open('file.txt', 'w')
# f.write('ULTIMO')
# f.close()

# Lectura
# with open('file,txt', 'r') as f:
#    for linea in f:
#    print(linea)
#    f.close()