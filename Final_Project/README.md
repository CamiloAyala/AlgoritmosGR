# Cálculo de complejidad

## Autores:

1. [Gerardo Andres Hormiga González](mailto:gahormigag@unal.edu.co)
2. [Ivan Fernando Caseres Rosas](mailto:icaseres@unal.edu.co)
3. [Camilo Arturo Echeverry Ayala](mailto:cecheverry@unal.edu.co)
4. [Fredy Andres Rosero Cristancho](mailto:faroseroc@unal.edu.co)

## Código
```python
# N = ciudades (nodos)
def Dijkstra(grafo, inicio, destino):	
  nodosPrevios = {} # O(1)
	
  pesosOptimos = {v: math.inf for v in list(nx.nodes(grafo))} # O(N)
  pesosOptimos[inicio] = 0 # O(1)

  vecinosSinVisitar = PriorityQueue() # O(1)
  vecinosSinVisitar.put((pesosOptimos[inicio], inicio)) # O(1)

  while vecinosSinVisitar.qsize() != 0: # O(E * log N)
    _ , nodoActual = vecinosSinVisitar.get() # O(log N)
    
    for nodoAdyacente in dict(grafo.adjacency()).get(nodoActual): # O(E)
			
      caminoAcumulado = pesosOptimos[nodoActual] + grafo.get_edge_data(nodoActual,nodoAdyacente).get ('weight') # O(1)

      if caminoAcumulado < pesosOptimos[nodoAdyacente]: # O(1)
        pesosOptimos[nodoAdyacente] = caminoAcumulado # O(1)
        nodosPrevios[nodoAdyacente] = nodoActual # O(1)
        vecinosSinVisitar.put((caminoAcumulado, nodoAdyacente)) # O(log N)

  nodo = destino # O(1)
  camino = [] # O(1)
  peso = pesosOptimos[nodo] # O(1)
  while nodo != inicio: # O(N-1): i.e.: Arbol como un Linked list lineal
    camino.append(nodo) # O(1) 
    nodo = nodosPrevios[nodo] # O(1)
  camino.append(nodo) # O(1)
  camino.reverse() # O(log N)

  return camino, peso
```
## Calculo del Big O es:
```   
O(1) + O(N) + 3*O(1) + O(N)*(O(log (N) + O(E)*(4*O(1) + O(log N)))) + 3*O(1) + O(N-1)*(2*O(1)) + O(1) + O(log N)

O(N) + O(N)*(O(log (N) + O(E)*(O(log N)))) + O(N-1) + O(log N)

O(N) + O(N)*(O(E + 1) * O(Log N)) + O(N-1) + O(log N)

O(N) + O(N)*(O(E) * O(Log N)) + O(N-1) + O(log N)

E = N porque puede ser fullconnected (worst-case)

O(N) + O(N^2) * O(Log N)) + O(N-1) + O(log N)

El total de vertices posible en un grafo dirigido de n nodos, es n(n-1) aprox -> n^2. Por tanto si E=N^2

O(N) + O(E) * O(Log N)) + O(N-1) + O(log N)

```

Por propiedades, el calculo de la complejidad para esta implementación del algoritmo de Dijkstra es:

```
O(E) * O(Log N))
```