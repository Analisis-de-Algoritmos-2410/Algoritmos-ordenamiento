# Analisis de complejidad de algoritmos de ordenamiento

## Merge sort

Este algoritmo sigue una técnica de Divide & Conquer.

1. Se divide el arreglo en en $2$
2. Se hace una llamada recursiva para ordenar esas mitades
    2.1 El caso base es que el tamaño del arreglo sea $1$, ya que ya está ordenado.
3. Se migran los dos arreglos ordenado escogiendo cual es el menor elemento que va de primeras en cada arreglo (Se puede utilizar la técnica de Two pointers).

El comportamiento asintotico de este algoritmo es $O(n\log n)$ ya que para migrar los array toma $O(n)$, entonces, siguiendo la relacion de recurrencia del algoritmo se puede decir que:

$$T(n) = 2T(n/2) + O(n)$$

Siguiendo el teorema maestro, entonces podemos decir que la complejidad si es $O(n\log n)$

### Lower bound de los algoritmos basados en comparaciones

Un algoritmo basado en comparaciones se llama así cuando ordena los elementos comparando los objetos por pares. **Merge y selection sort** son algoritmos basados en comparaciones.

**Lemma**: Cualquie algoritmo basado en comparación hace $\Omega(n\log n)$ comparaciones en el peor caso para ordenar $n$ objetos.

**Proof**: Cuando se crea el arbol de decision de un algoritmo basado en comparaciones, podemos verificar ciertas cosas.

Lo primero es que el arbol va a tener $l = n!$ hojas, ya que las hojas en el arbol van a ser las permutaciones del array y solo una es la correcta. Lo segundo es que el arbol va a tener una profundidad $d$ que va a ser calculado despues.

En el peor caso, se debe hacer $d$ comparaciones para llegar a la hoja y como los arboles de decisiones son arboles binarios completos, entonces se puede determinar que:

$$2^d = l \implies d = \log_2l$$

Y se puede demostrar que $\log (n!) = \Omega(n\log n)$. Siguiendo la siguiente representacion de $\log(n!)$.

$$
\begin{align}
\log_2(n!) &= \log_2(1 \cdot 2 \cdot \dots \cdot n) \\
&= \log_2 1 + \log_2 2 + \dots + \log_2 n \\
&= \sum_{i=1}^{n}\log_2i
\end{align}
$$

Dado esto, determine solo la segunda mitad, y denote que ahora el resultado va a ser menor o igual a $\log_2(n!)$

$$
\begin{align}
\log_2(n!) &\ge \log_2 \frac{n}{2} + \dots + \log_2 n \\
\log_2(n!) &\ge \frac{n}{2}\log_2 \frac{n}{2} = \Omega(n\log n)\\
\end{align}
$$

## Quick sort

Quick sort es un algoritmo basado en comparaciones. Su comportamiento asintotico es de $\Theta(n\log n)$ pero es en el caso promedio, ya que es randomizado el proceso. Este comportamiento asintotico se da gracias a que se considera un algoritmo de Divide & Conquer, y se puede modelar la manera en la que ejecuta el algoritmo con la relación de recurrencia similar al **merge sort**.

Quick sort tiene la idea que se tiene que elegir un pivot $x$ (Un numero que generalmente es el primero) y hay que reordenar el arreglo según el pivot. Es decir, considere el arreglo $[5, 4, 8, 1, 2]$ en este caso el pivot va a ser $5$, entonces se debe reordenar el arreglo de la siguiente manera:

$$[\underbrace{1, 2, 4}_{\le x}, \underbrace{5}_{x}, \underbrace{8}_{< x}]$$

Entonces una vez reordenado el arreglo ordena de manera recursiva el arreglo $\le x$ y el arreglo resultante de $< x$. El pivot ya está ordenado, entonces no es necesario hacer algún arreglo.

Para el proceso de reordenar el arreglo, se debe tener en cuenta que hay que dibujar las dos regiones $\le x$ y la $< x$, entonces siempre que descubramos un numero $\le x$ se debe hacer un swap con el primer elemento de la región $< x$. Al final se hace un swap del ultimo elemento de la región $\le x$ con el pivot. Dicho de cierta forma, hacer esas dos particiones va a tomar $O(n)$.


Pero, para escoger el pibote hay que ser cuidadosos, ya que si escogemos el elemento minimo del arreglo como pibote siempre, entonces la complejidad va a ser de $\Theta(n^2)$ ya que no existe la primera región.

QuickSort no tiene asegurado que sea $O(n\log n)$, puede ser $O(n^2)$ en los peores casos de partición, podría probarse que con un pivot random podría mejorar la mayoría de los casos, pero en el peor caso, siempre va a ser $O(n^2)$

Sin embargo, hay que tener en cuenta que si todos los elementos son iguales, entonces el algoritmo daría un tiempo de $O(n^2)$. Para evitar esto, lo que se puede hacer es hacer una partición de más, o una region de mas $= x$ donde se almacenen todos los elementos iguales al pivot.

Para poder seguir con el algoritmo, debemos almacenar los indices que indican los boundaries de las regiones para que se pueda referenciar en las demás llamadas recursivas.
