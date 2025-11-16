
items = []
n = 0
gaps = []    # La secuencia de saltos (Shell, Knuth, etc.)
gap_index = 0 # Índice en la secuencia de gaps
i = 0        # Índice principal (para el bucle externo)
j = 0        # Índice de comparación/swap

def init(vals):
    """
    Inicializa el estado del algoritmo.
    Utiliza la secuencia de gaps de Shell (n/2, n/4, ...)
    """
    global items, n, gaps, gap_index, i, j
    items = list(vals)
    n = len(items)
    
    # 1. Generar la secuencia de gaps (Clásico de Shell)
    gaps.clear()
    h = n // 2
    while h > 0:
        gaps.append(h)
        h //= 2
    
    # 2. Reiniciar punteros
    gap_index = 0
    i = 0 
    j = 0 

def step():
    """
    Ejecuta UN micro-paso del algoritmo Shell Sort (comparación o swap).
    """
    global items, n, gaps, gap_index, i, j
    
    # Si no quedan más gaps por procesar, el algoritmo terminó
    if gap_index >= len(gaps):
        return {"done": True}
    
    gap = gaps[gap_index]
    
    # El Shell Sort usa una "Insertion Sort" con un salto (gap)
    
    # 1. Avanzar i al primer elemento a insertar (i = gap)
    if i < gap:
        # Iniciamos la fase de Insertion Sort con el gap actual
        i = gap
        j = i 
    
    # 2. Chequeo de fin de la pasada (todos los elementos insertados con este gap)
    if i >= n:
        # Terminó la pasada para este gap.
        gap_index += 1 # Avanzamos al siguiente gap
        i = 0          # Reiniciamos i para el nuevo gap
        j = 0
        return {"a": -1, "b": -1, "swap": False, "done": False} # Paso de control
        
    # 3. Lógica de comparación/swap (como en Insertion Sort, pero con salto)
    
    # Comienzo del desplazamiento hacia atrás (j es la posición actual, j - gap es la anterior)
    if j < gap or items[j - gap] <= items[j]:
        # Ya se encontró la posición correcta (o es el primer elemento), avanzamos 'i'
        i += 1
        j = i
        # Devolvemos un highlight simple sin swap
        return {"a": i - 1, "b": i, "swap": False, "done": False}

    else:
        # Es necesario hacer el intercambio (swap)
        a = j - gap
        b = j
        
        # Realizamos el intercambio en la lista global 'items'
        items[a], items[b] = items[b], items[a]
        
        # Retrocedemos la posición j
        j -= gap
        
        # Devolvemos el resultado (swap = True)
        return {"a": a, "b": b, "swap": True, "done": False}