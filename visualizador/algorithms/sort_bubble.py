items = []
n = 0
i = 0   # número de pasadas completas
j = 0   # índice dentro de la pasada

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j
    # Si ya terminó (pasadas >= n-1)
    if i >= n-1:
        return {"done": True}

    a = j
    b = j+1

    # comparar y swap si corresponde
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swapped = True
    else:
        swapped = False

    # avanzar j; si llegamos al final de la pasada, reiniciar j y aumentar i
    j += 1
    if j+1 > n - i - 1:
        j = 0
        i += 1

    return {"a": a, "b": b, "swap": swapped, "done": False}
