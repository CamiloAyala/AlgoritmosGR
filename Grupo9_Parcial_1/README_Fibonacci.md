# Fibonacci
[README](README.md)

    actual = 0                                              -> O(1)
    siguiente = 1                                           -> O(1)
    for k in range(n):                                      -> O(n)
        suma = actual + siguiente                           -> O(1)
        actual = siguiente                                  -> O(1)
        siguiente = suma                                    -> O(1)

Es evidente que la complejidad de la suma no resulta ser tan grande 
como para ser considerado O(n).

El calculo del Big-O es el siguiente:

     O(1) + O(1) + O(n)*(O(1) + O(1) + O(1))
     2*O(1) + O(n) * (3*O(1))

Despreciando los costos insignificativos tenemos como resultado que el
algoritmo tiene un costo de O(n)