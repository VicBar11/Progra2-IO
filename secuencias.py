def verificar_match(hilera1, hilera2, i, j):
    if hilera1[i] == hilera2[j]:
        return 1
    return -1


def alineamiento_aux(string1, string2, penalizacion):
    filas = len(string1) + 1
    columnas = len(string2) + 1

    matriz = []
    punteros_matriz = []

    for i in range(filas):
        # llenar la matriz
        # con ceros
        matriz.append([0] * columnas)
        punteros_matriz.append([0] * columnas)

        # llenar primera columna
        matriz[i][0] = i * penalizacion

    for j in range(columnas):
        # llenar primera fila
        matriz[0][j] = j * penalizacion

    i = 1
    while i < filas:
        j = 1
        while j < columnas:

            # función match/missmatch
            fn = verificar_match(string1, string2, i - 1, j - 1)

            # match / missmatch / gap-penalty
            caso1 = matriz[i - 1][j - 1] + fn
            caso2 = matriz[i][j - 1] + penalizacion
            caso3 = matriz[i - 1][j] + penalizacion

            _max = max(caso1, caso2, caso3)

            # máximo entre los 3 casos (principio de optimalidad)
            matriz[i][j] = _max

            # marca camino en la matriz puntero
            if caso1 == _max:
                punteros_matriz[i][j] = 1
            elif caso2 == _max:
                punteros_matriz[i][j] = 2
            else:
                punteros_matriz[i][j] = 3

            j += 1
        i += 1

    for i in range(filas):
        print('|', end='')
        for j in range(columnas):
            ptr = punteros_matriz[i][j]
            print('%4d' % (ptr), end='|')
        print('')

    print('')

    for i in range(filas):
        print('|', end='')
        for j in range(columnas):
            item = matriz[i][j]
            print('%4d' % (item), end='|')
        print()

    return matriz, punteros_matriz


def alineamiento_needleman(hilera1, hilera2):
    matriz, punteros = alineamiento_aux(hilera1, hilera2, -2)

    len_s1 = len(hilera1)
    len_s2 = len(hilera2)

    sec1_res = []
    sec2_res = []

    while True:

        ptr = punteros[len_s1][len_s2]

        if punteros[len_s1][len_s2] == 1:  # diagonal
            sec2_res.append(hilera2[len_s2 - 1])  # mete la letra en la hilera 2
            sec1_res.append(hilera1[len_s1 - 1])  # mete la letra en la hilera 1
            len_s1 -= 1
            len_s2 -= 1

        elif punteros[len_s1][len_s2] == 2:  # izquierda
            sec2_res.append(hilera2[len_s2 - 1])  # mete la letra en la hilera 2
            sec1_res.append('_')  # mete gap en la hilera 1
            len_s2 -= 1

        elif punteros[len_s1][len_s2] == 3:  # arriba
            sec2_res.append('_')  # mete gap en la hilera 2
            sec1_res.append(hilera1[len_s1 - 1])  # mete la letra en la hilera 1
            len_s1 -= 1
        else:
            break

    while len_s1 > 0:
        sec2_res.append('_')  # mete gap en la hilera 2
        sec1_res.append(hilera1[len_s1 - 1])  # mete la letra en la hilera 1
        len_s1 -= 1

    while len_s2 > 0:
        sec2_res.append(hilera2[len_s2 - 1])  # mete la letra en la hilera 2
        sec1_res.append('_')  # mete gap en la hilera 1
        len_s2 -= 1

    print(''.join(sec1_res[::-1]))
    print(''.join(sec2_res[::-1]))

    return matriz[len(hilera1)][len(hilera2)]


def evaluar_secuencias(hilera1, hilera2):
    score = 0
    for i in range(len(hilera1)):
        if hilera1[i] == hilera2[i]:
            score += 1
        elif hilera1[i] == '_' or hilera2[i] == '_':
            score -= 2
        elif hilera1[i] != hilera2[i]:
            score -= 1
    return score


def alineamiento_bruto_aux(hilera1, hilera2, hilera_resultante1, hilera_resultante2):

    if hilera1 == '' and hilera2 == '':
        return (hilera_resultante1, hilera_resultante2), evaluar_secuencias(hilera_resultante1, hilera_resultante2)

    if hilera1 == '' and hilera2 != '':

        while hilera2 != '':
            hilera_resultante1 += '_'
            hilera_resultante2 += hilera2[0]
            hilera2 = hilera2[1:]

        return (hilera_resultante1, hilera_resultante2), evaluar_secuencias(hilera_resultante1, hilera_resultante2)

    if hilera2 == '' and hilera1 != '':

        while hilera1 != '':
            hilera_resultante1 += hilera1[0]
            hilera_resultante2 += '_'
            hilera1 = hilera1[1:]

        return (hilera_resultante1, hilera_resultante2), evaluar_secuencias(hilera_resultante1, hilera_resultante2)

    else:
        caso1 = alineamiento_bruto_aux(hilera1[1:], hilera2[1:], hilera_resultante1 + hilera1[0],
                                       hilera_resultante2 + hilera2[0])
        caso2 = alineamiento_bruto_aux(hilera1[1:], hilera2, hilera_resultante1 + hilera1[0], hilera_resultante2 + '_')
        caso3 = alineamiento_bruto_aux(hilera1, hilera2[1:], hilera_resultante1 + '_', hilera_resultante2 + hilera2[0])

        maximo = max(caso1[1], caso2[1], caso3[1])

        if maximo == caso1[1]:
            return caso1
        if maximo == caso2[1]:
            return caso2
        else:
            return caso3


def alineamiento_bruto(hilera1, hilera2):
    return alineamiento_bruto_aux(hilera1, hilera2, '', '')

# alineamiento_bruto('ATTGTGATCC', 'TTGCATCGGC', '', '')
