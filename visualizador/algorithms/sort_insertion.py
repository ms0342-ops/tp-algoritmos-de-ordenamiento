items = []
n = 0
i = 1   # elemento que vamos a insertar en la parte ordenada 0..i-1
j = 1   # índice que usamos para comparar hacia atrás

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = 1

def step():
    global items, n, i, j
    if i >= n:
        return {"done": True}

    # Si j > 0 y items[j-1] > items[j], swap adyacente
    if j > 0 and items[j-1] > items[j]:
        a = j-1
        b = j
        items[a], items[b] = items[b], items[a]
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}
    else:
        # si no se puede intercambiar más, avanzamos i (nueva inserción)
        i += 1
        j = i
        return {"a": max(0, j-1), "b": j if j < n else j-1, "swap": False, "done": False}
