items = []
n = 0
i = 0       # posición donde pondremos el mínimo
j = 0       # índice que explora la porción i..n-1
min_idx = 0 # índice del mínimo encontrado

def init(vals):
    global items, n, i, j, min_idx
    items = list(vals)
    n = len(items)
    i = 0
    j = 1 if n > 1 else 0
    min_idx = 0

def step():
    global items, n, i, j, min_idx
    # terminado
    if i >= n-1:
        return {"done": True}

    # Si j está en la primera posición de la exploración, inicializo min_idx
    if j == i + 1:
        min_idx = i

    # comparo j con min_idx (si j < n)
    if j < n:
        a = j
        b = min_idx
        # actualizo min_idx si encuentro uno más chico
        if items[j] < items[min_idx]:
            min_idx = j
            # mostramos comparación, sin swap aún
            j += 1
            return {"a": a, "b": b, "swap": False, "done": False}
        else:
            j += 1
            return {"a": a, "b": b, "swap": False, "done": False}

    # si j >= n entonces terminó la exploración: hago swap entre i y min_idx si hace falta
    if min_idx != i:
        items[i], items[min_idx] = items[min_idx], items[i]
        did_swap = True
    else:
        did_swap = False

    # preparo la siguiente pasada
    i += 1
    j = i + 1 if i + 1 < n else i
    return {"a": i-1, "b": min_idx, "swap": did_swap, "done": False}
