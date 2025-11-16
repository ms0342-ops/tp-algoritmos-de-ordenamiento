# 📊**Visualización de algoritmos de ordenamiento**

Este proyecto es una **herramienta de visualización interactiva** diseñada para demostrar y analizar el rendimiento de varios algoritmos de ordenamiento. La implementación permite al usuario ejecutar algoritmos paso a paso sobre un arreglo de barras, ajustando la cantidad de elementos y la velocidad de la animación.

## 🚀Estructura y componentes

| Archivo/carpeta | Proposito    | Tecnologia                |
| :-------- | :------- | :------------------------- |
 | `index.html` | Interfaz de usuario, animacion y controlador principal | HTML, CSS, JavaScript | 
| `algoritms`/ | Contiene la logica de ordenamiento por micro-pasos    | Python                      |
| `README.md`| Documentacion del proyecto e implementacion | Markdown|


## Algoritmos implementados + Metricas implementadas

- **Bubble Sort (sort_bubble.py):** Intercambia pares adyacentes hasta que el mayor "burbujea" al final.

- **Insertion Sort(sort_insertion.py):** Inserta el elemento actual en su posicion correcta dentro del sub-arreglo ordenado.

- **Selection Sort(sort_selection.py):** Busca el elemento minimo y lo coloca al inicio de cada pasada.

- **Quick Sort(sort_quick.py):** Divide el arreglo alrededor de un pivote y luego ordena recursivamente las dos mitades.

- **Shell Sort(sort_shell.py):** Mejora de Insertion Sort, utilizando saltos (gaps) para mover elementos distantes.

- **Metrica de tiempo**

- **Metrica de historial de rendimiento**

# 📝Notas de implementación 
 

```
Todos los algoritmos cumplen el contrato de realizar una operación atómica 
(una comparacion o intercambio) por cada llamada a la función step( ). 
Esto se logra mediante el uso de variables globales dentro de cada modulo Python 
(sort_bubble.py -sort_insertion.py,etc.)para almacenar el estado de los bucles (i y j) 
y los rangos de operacion  (low, high)
```


## ▶Instrucciones de uso

Para ejecutar el visualizador, abre el archivo index.html en tu navegador web.

- **Ajustes iniciales:** modifica el control deslizante de cantidad para definir el tamaño de arreglo

- **Inicializacion:** pulsa el boton mezclar para generar una nueva secuencia aleatoria de barras. Elige un algoritmo del menu desplegable.
 

  **Control de ejecución:**
    - 
- **Reproducir:** inicia la animacion continua.
- **Pausar:** detiene la animacion en el paso actual
- **Paso:** ejecuta un solo micro-paso dek algoritmo, ideal para el analisis de la logica.


## **Introducción a la Programacion (COM-11)**

## 👩🏻‍💻Equipo de desarrollo

- **Alumna:** Sánchez, Rocio Micaela.

## 👨‍🏫 Docentes

- Omar, Argañaras.

- Velazquez, Luca.
