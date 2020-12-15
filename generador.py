import sys
from random import randint

from contenedor import contenedor, contenedor_fuerza_bruta
from item import Item
from secuencias import alineamiento_needleman


def main(_argv):
    if len(sys.argv) == 1:
        print('error')
        return

    if sys.argv[1] == '1':
        if len(sys.argv) != 10:
            print('error')
            return

        w = int(sys.argv[2])
        n = int(sys.argv[3])
        min_peso = int(sys.argv[4])
        max_peso = int(sys.argv[5])
        min_beneficio = int(sys.argv[6])
        max_beneficio = int(sys.argv[7])
        min_cantidad = int(sys.argv[8])
        max_cantidad = int(sys.argv[9])

        items = generador_contenedor(n, min_peso, max_peso, min_beneficio, max_beneficio, min_cantidad, max_cantidad)

        print('Programación Dinámica:' + str(contenedor(items, w)))
        print('Fuerza Bruta:' + str(contenedor_fuerza_bruta(items, w)))

    if sys.argv[1] == '2':
        hileras = generador_secuencias(int(sys.argv[2]), int(sys.argv[3]))
        alineamiento_needleman(hileras[0], hileras[1])


def generador_contenedor(n, min_p, max_p, min_b, max_b, min_c, max_c):
    items = []

    _id = 0
    cont = 0
    while cont < n:

        peso = randint(min_p, max_p)
        beneficio = randint(min_b, max_b)
        cantidad = randint(min_c, max_c)

        for i in range(cantidad):
            items.append(Item(_id + 1, peso, beneficio))
            cont += 1

        _id += 1

    return items


def generador_secuencias(len_hilera1, len_hilera2):
    letras = ['A', 'T', 'G', 'C']
    hilera1 = []
    hilera2 = []

    i = 0
    while i < len_hilera1:
        valor = randint(0, 3)
        hilera1.append(letras[valor])
        i += 1

    i = 0
    while i < len_hilera2:
        valor = randint(0, 3)
        hilera2.append(letras[valor])
        i += 1

    print(''.join(hilera1))
    print(''.join(hilera2))

    return ''.join(hilera1), ''.join(hilera2)


if __name__ == '__main__':
    main(sys.argv[1:])
