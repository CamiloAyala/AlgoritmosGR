from queue import PriorityQueue
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


