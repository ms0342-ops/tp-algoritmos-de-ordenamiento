
# Variables Globales de Estado
items = []
n = 0
# Stack: Almacena las tareas pendientes de QuickSort como tuplas (low, high)
stack = []
# Punteros de la Partición Actual (La que se está trabajando en step())
low = 0
high = 0
# i es el puntero que rastrea la posición para el siguiente elemento menor al pivote
i = 0 
# j es el cursor que explora el sub-array
j = 0
# pivot_val es el valor del pivote (tomado de items[high])
pivot_val = 0
# fase: Controla qué parte del algoritmo QuickSort se ejecuta en este step()
# 'partition': Fase de barrido (j avanza comparando con el pivote)
# 'swap_pivot': Fase donde se coloca el pivote en su posición final
# 'check': Fase de chequeo, donde se finaliza la tarea y se añaden nuevas subtareas a la pila
fase = 'check' 

def init(vals):
    """
    Inicializa el estado del algoritmo Quick Sort.
    """
    global items, n, low, high, i, j, stack, fase
    items = list(vals)
    n = len(items)
    
    # Inicializa la pila con la tarea de ordenar el array completo
    stack = [(0, n - 1)]
    # La fase inicial debe ser 'check' para que el primer step() saque la primera tarea de la pila
    fase = 'check' 
    low = 0
    high = n - 1
    i = -1
    j = 0
    
def step():
    """
    Ejecuta un micro-paso del algoritmo Quick Sort.
    """
    global items, n, low, high, i, j, stack, fase, pivot_val
    
    # 1. Chequeo de Terminación Global
    if not stack and fase == 'check':
        return {"done": True}

    # 2. Gestión de Tareas (Simulación de Recursión)
    # Si la fase actual ha terminado, sacamos la siguiente tarea de la pila
    if fase == 'check':
        # Si la pila está vacía, ya terminamos.
        if not stack:
            return {"done": True} 
            
        # Extrae la próxima tarea de la pila
        low, high = stack.pop() 

        # Si el sub-array tiene 0 o 1 elemento, ya está ordenado. Pasamos a la siguiente tarea.
        if low >= high:
            fase = 'check'
            # Punteros para la visualización del rango activo (opcional)
            return {"a": low, "b": high, "swap": False, "done": False}

        # Inicializa la partición para el rango (low, high)
        fase = 'partition'
        pivot_val = items[high]
        i = low - 1 # i rastrea el índice del último elemento menor (o igual)
        j = low     # j es el cursor de barrido

    # 3. Fase de Particionamiento ('partition')
    # Recorre el array desde low hasta high-1 comparando con el pivote
    if fase == 'partition':
        # Si j ya llegó al final del rango a particionar (high - 1)
        if j >= high:
            fase = 'swap_pivot'
            # No devolvemos nada, pasamos inmediatamente a la fase de swap_pivot
            return step() 
            
        # El puntero 'a' es el elemento actual que se compara (j)
        # El puntero 'b' es el pivote (high)
        a, b = j, high

        if items[j] < pivot_val:
            # El elemento en j es menor que el pivote
            i += 1
            if i != j:
                # Intercambio real en el array y lo reportamos como swap
                items[i], items[j] = items[j], items[i]
                j += 1
                return {"a": a, "b": i, "swap": True, "done": False} 
            else:
                # No hay swap, solo avanza i y j (caso en que i == j)
                j += 1
                return {"a": a, "b": b, "swap": False, "done": False}
        else:
            # El elemento es mayor o igual que el pivote, solo avanza j
            j += 1
            return {"a": a, "b": b, "swap": False, "done": False}

    # 4. Fase de Colocación del Pivote ('swap_pivot')
    # Coloca el pivote (items[high]) en su posición final (i + 1)
    if fase == 'swap_pivot':
        # La posición final del pivote es i + 1
        pivot_pos = i + 1 
        
        # Realizar el intercambio (pivote con items[i+1])
        items[pivot_pos], items[high] = items[high], items[pivot_pos]
        
        # Generar las nuevas subtareas y ponerlas en la pila
        # Tarea izquierda: (low, pivot_pos - 1)
        stack.append((low, pivot_pos - 1))
        # Tarea derecha: (pivot_pos + 1, high)
        stack.append((pivot_pos + 1, high))
        
        # La partición terminó. Volvemos al gestor de tareas ('check')
        fase = 'check'
        
        # Devolvemos el estado de swap del pivote
        return {"a": high, "b": pivot_pos, "swap": True, "done": False}

    # Fallback (no debería pasar)
    return {"done": False}