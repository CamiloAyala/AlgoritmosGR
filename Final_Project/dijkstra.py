"""
  TODO: Agregar comentarios de la función
"""

def Dijkstra(grafo, inicio, destino):
  # Guarda el camino realiado desde la ciudad de inicio hasta la ciudad de destino
  nodosPrevios = {}

  distancias = {v: math.inf for v in list(nx.nodes(grafo))}
  distancias[inicio] = 0
  peso = 0

  cola = []
  cola.append(inicio)

  while len(cola) != 0:
    nodoActual = cola.pop(0)
    
    # Itera sobre los nodos adjacentes del nodo Actual
    for nodoAdjacente in dict(grafo.adjacency()).get(nodoActual):

      path = distancias[nodoActual] + grafo.get_edge_data(nodoActual,nodoAdjacente).get('weight')
      # Evalua si el nuevo camino es menor en peso al actual
      if path < distancias[nodoAdjacente]:
        # Actualiza el nuevo peso junto con el nodo al cual se pasa
        distancias[nodoAdjacente] = path
        nodosPrevios[nodoAdjacente] = nodoActual

        cola.append(nodoAdjacente)

  node = destino
  path = []
  peso = distancias[node]
  while node != inicio:
    path.append(node)
    node = nodosPrevios[node]
  path.append(node) 
  path.reverse()

  return path, peso