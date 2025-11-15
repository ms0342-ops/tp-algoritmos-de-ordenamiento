
items = []
n = 0

# Punteros/estado que usa Bubble Sort
i = 0   # cantidad de pasadas completas
j = 0   # índice dentro de la pasada actual

def init(vals):
    """
    Inicializa el estado del algoritmo.
    Recibe la lista original y prepara los punteros.
    """
    global items, n, i, j
    items = list(vals)
    n = len(items)

    # Bubble arranca así:
    i = 0
    j = 0


def step():
    """
    Ejecuta UN micro-paso del algoritmo Bubble Sort.
    Devuelve:
        {"a": a, "b": b, "swap": bool, "done": False}
    o si terminó:
        {"done": True}
    """
    global items, n, i, j

    # Si ya hicimos todas las pasadas, terminamos
    if i >= n - 1:
        return {"done": True}

    # Comparar posiciones j y j+1
    a = j
    b = j + 1

    # swap si corresponde
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swapped = True
    else:
        swapped = False

    # avanzar j
    j += 1

    # si llegamos al final de la pasada:
    if j + 1 > n - i - 1:
        j = 0     # reiniciamos j
        i += 1    # siguiente pasada

    return {"a": a, "b": b, "swap": swapped, "done": False}
