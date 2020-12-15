import sys
from item import Item
from time import time
import matplotlib.pyplot as plt
from generador import generador_contenedor, generador_secuencias
from secuencias import alineamiento_needleman, alineamiento_bruto
from contenedor import contenedor, contenedor_fuerza_bruta


def main(_argv):
    if len(sys.argv) == 1:
        print('error')
        return

    if sys.argv[1] == '-h':
        print('INSTRUCCIONES:')
        print('Para poder utilizar este sistema debe utilizar el siguiente comando:')
        print('python3 solver.py seleccion_problema seleccion_algoritmo nombre_archivo')
        print('OPCIONES:')
        print('Problema 1 -> Contenedor')
        print('Problema 2 -> Secuencias')
        print('Algoritmo 1 -> Fuerza Bruta')
        print('Algoritmo 2 -> Programación Dinámica')

    elif sys.argv[1] == '1':
        if len(sys.argv) != 4:
            print('error')
            return

        datos_cargados = cargar_archivo_contenedor(sys.argv[3])

        if sys.argv[2] == '1':
            print('Resultado Fuerza Bruta:' + str(contenedor_fuerza_bruta(datos_cargados[1], datos_cargados[0])))
        elif sys.argv[2] == '2':
            print('Resultado Programacion Dinámica:' + str(contenedor(datos_cargados[1], datos_cargados[0])))
        else:
            print("Error: utilice el siguiente comando para ver las instrucciones")
            print("python3 solver.py -h")

    elif sys.argv[1] == '2':
        if len(sys.argv) != 4:
            print('error')
            return

        datos_cargados = cargar_archivo_secuencias(sys.argv[3])

        if sys.argv[2] == '1':
            print('Fuerza Bruta Score:' + str(alineamiento_bruto(datos_cargados[0].strip(), datos_cargados[1].strip())))
        elif sys.argv[2] == '2':
            print('Needleman-Wunsch Score:' + str(
                alineamiento_needleman(datos_cargados[0].strip(), datos_cargados[1].strip())))

    elif sys.argv[1] == '3':

        w = 200
        n = 10
        min_peso = 5
        max_peso = 100
        min_beneficio = 12
        max_beneficio = 70
        min_cantidad = 1
        max_cantidad = 5

        items = generador_contenedor(n, min_peso, max_peso, min_beneficio, max_beneficio, min_cantidad, max_cantidad)

        analizar_contenedor(500, items, w)

    elif sys.argv[1] == '4':

        #secuencias = generador_secuencias(5, 5)
        #analizar_secuencias(5, secuencias[0], secuencias[1])
        analizar_secuencias2(13)

    else:
        print('error')


def cargar_archivo_contenedor(filename):
    file = open(filename, 'r')

    peso_max = int(file.readline())
    items = []

    for i, linea in enumerate(file.readlines()):
        valores = linea.split(',')
        for j in range(int(valores[2])):
            items.append(Item(i + 1, int(valores[0]), int(valores[1])))

    return peso_max, items


def cargar_archivo_secuencias(filename):
    file = open(filename, 'r')

    linea1 = file.readline()
    linea2 = file.readline()

    return linea1, linea2


def analizar_contenedor(loops, items, w):
    sizes = list(range(1, loops + 1))

    repeticiones_dinamica = []
    repeticiones_fuerza_bruta = []

    cont = 0

    while cont < loops:
        start_time = time()
        contenedor(items, w)
        elapsed_time = time() - start_time
        repeticiones_dinamica.append(elapsed_time)

        start_time = time()
        print(contenedor_fuerza_bruta(items, w))
        elapsed_time = time() - start_time
        repeticiones_fuerza_bruta.append(elapsed_time)

        cont += 1

    plt.plot(sizes, repeticiones_dinamica, color='blue')
    plt.plot(sizes, repeticiones_fuerza_bruta, color='green')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('Ciclos (i)')
    plt.show()


def analizar_secuencias(loops, hilera1, hilera2):
    sizes = list(range(1, loops + 1))

    repeticiones_dinamica = []
    repeticiones_fuerza_bruta = []

    cont = 0

    while cont < loops:
        start_time = time()
        alineamiento_needleman(hilera1, hilera2)
        elapsed_time = time() - start_time
        repeticiones_dinamica.append(elapsed_time)

        start_time = time()
        alineamiento_bruto(hilera1, hilera2)
        elapsed_time = time() - start_time
        repeticiones_fuerza_bruta.append(elapsed_time)

        cont += 1

    plt.plot(sizes, repeticiones_dinamica, color='yellow')
    plt.plot(sizes, repeticiones_fuerza_bruta, color='grey')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('Ciclos (i)')
    plt.show()

def analizar_secuencias2(loops):

    sizes = list(range(2, loops + 1))

    repeticiones_dinamica = []
    repeticiones_fuerza_bruta = []

    cont = 1

    while cont < loops:

        hileras = generador_secuencias(cont, cont)

        start_time = time()
        alineamiento_needleman(hileras[0], hileras[1])
        elapsed_time = time() - start_time
        repeticiones_dinamica.append(elapsed_time)

        start_time = time()
        alineamiento_bruto(hileras[0], hileras[1])
        elapsed_time = time() - start_time
        repeticiones_fuerza_bruta.append(elapsed_time)

        cont += 1

    plt.plot(sizes, repeticiones_dinamica, color='yellow')
    plt.plot(sizes, repeticiones_fuerza_bruta, color='grey')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('Largo de hilera (i)')
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
