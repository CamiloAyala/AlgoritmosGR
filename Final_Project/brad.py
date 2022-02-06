import heapq


def calculate_distances(graph, starting_vertex):
    # pesos l22
    pesos = {vertex: float('infinity') for vertex in graph}
    pesos[starting_vertex] = 0 #L25
    
    # (pesos,cola)     
    pesosMasCola = [(0, starting_vertex)]
    while len(pesosMasCola) > 0:
        #pesos, nodoActual
        pesosNodoActual, nodoActual = heapq.heappop(pesosMasCola)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if pesosNodoActual > pesos[nodoActual]:
            continue
        
        # Recorrerer los vecinos del nodo actual
        # graph[nodoActual].items(): matrix de ADjh para nodo actual
        for nodoAdyacente, weight in graph[nodoActual].items(): #74
            distanciaHastaNodoAdyacente = pesosNodoActual + weight #76

            # Only consider this new path if it's better than any path we've
            # already found.
            # ¿EStte camino es mas corto que el camino antes calculado
            # a este mismo NodoAdj?
            # PReviene retornos
            if distanciaHastaNodoAdyacente < pesos[nodoAdyacente]: #78
                pesos[nodoAdyacente] = distanciaHastaNodoAdyacente
                heapq.heappush(pesosMasCola, (distanciaHastaNodoAdyacente, nodoAdyacente)) #L78 +L90 

    return pesos


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
