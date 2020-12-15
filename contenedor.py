
def contenedor(items, capacidad):

    matriz = []
    n = len(items)

    for x in range(n):
        matriz.append([])
        for y in range(capacidad + 1):
            matriz[x].append(0)

    for i in range(n):
        for j in range(capacidad + 1):
            if items[i].weight < j+1:
                matriz[i][j] = max(matriz[i-1][j], items[i].value + matriz[i-1][j - items[i].weight])
            else:
                matriz[i][j] = matriz[i-1][j]

    res = [item.to_string() for item in contenedor_aux(items, matriz)]

    return [matriz[n-1][capacidad], res]


def contenedor_aux(items, matriz):

    fila = len(matriz) - 1
    columna = len(matriz[0]) - 1

    result = []

    while fila > -1:

        if fila == 0 and items[fila].weight <= columna:
            result.append(items[fila])
            break

        if matriz[fila][columna] != matriz[fila-1][columna]:
            result.append(items[fila])
            columna -= items[fila].weight

        fila -= 1

    return result


def calcular_peso(items):
    return sum(x.weight for x in items)


def calcular_valores(items):
    return sum(x.value for x in items)


def contenedor_fuerza_bruta(items, max_weight):
    res = max(fuerza_bruta_aux(items, max_weight), key=calcular_valores)
    return [sum(item.value for item in res), [item.to_string() for item in res]]


def fuerza_bruta_aux(items, max_weight):
    aux = [p for p in items if p.weight <= max_weight]

    result = []

    for p in aux:
        res = fuerza_bruta_aux([x for x in aux if x != p], max_weight - p.weight)

        if len(res) == 0:

            result.append([p])
        else:
            result.extend([[p] + x for x in res])

    return result
