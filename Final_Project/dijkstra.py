"""
	El agoritmo recorre de manera global global el grafo
	como si fuera arbol hacia abajo, caclulando las distancia relativa en cada 
	vertice.
  TODO: Agregar comentarios de la función
	De network: 
		grafo.adjacency()
		nx.nodes(grafo)
		grafo.get_edge_data(nodoActual,nodoAdjacente).get('weight')
"""
def Dijkstra(grafo, inicio, destino):	
  # Lista: Guarda el camino realiado desde la ciudad de inicio hasta la ciudad de destino
  # Enlaza un nodo con su nodo anterior en el calculo del camino mas corto
  nodosPrevios = {}
	
	# nx.nodes(G)= [nodo1,nodo2,...,nodoN]
	# Objeto `pesos`:
	#		Es el peso (distancia o tiempo) de inicio a destino, 
	# 	contiene las distancias/tiempos o pesos relativos
	# 	desde el punto de vista del nodo inicial
	# Inicializar un diccionario (nodoX: peso[en infty]) excepto al nodo de origen
	# N=|ciudades|
	# O(N)
	
  print("1")
  pesos = {v: math.inf for v in list(nx.nodes(grafo))}
	# excepto al nodo de origen...
	# O(1)
  pesos[inicio] = 0

	# Cuando se cacula la distancia relativa a un nodo
	# Previene que se tengan en cuenta caminos mas largos
	# FIFO:
	# O(1)
  cola = []
	# O(1)

	#

	# Desde ell punto de vista del arbol,
	# Desde la raiz el primer vecino es el nodo de partida (inicio)
  cola.append(inicio)

	# Mientras hayan vecinos optimos que recorrer
  while len(cola) != 0:
		# Extraer el primero
		# O(1)
    nodoActual = cola.pop(0)
    
    # Itera sobre los nodos adjacentes del nodo Actual
		# dict(grafo.adjacency()) matrix de adjacencia

		# 'Santa Marta': {'Armenia': {'weight': 1252},
		# 							'Barranquilla': {'weight': 114},
		# 							'Bogotá': {'weight': 1128},
		# 							'Bucaramanga': {'weight': 721},
		# 							'Cali': {'weight': 1507},
		# 							'Cartagena': {'weight': 306},
		# 							'Cúcuta': {'weight': 816},
		# 							'Ibagué': {'weight': 1118},
		# 							'Manizales': {'weight': 1149},
		# 							'Medellín': {'weight': 937},
		# 							'Neiva': {'weight': 1335},
		# 							'Pasto': {'weight': 2048},
		# 							'Pereira': {'weight': 1231},

		# Recorrer cada uno de los nodos vecinos del nodo actal
		# 	la convierte en diccionario
		# 	y del diccionario extrae los de llave: {[nodoactual]=[nodoX],[nodoactual]=[nodoY],[nodoactual]=[nodoZ],...}
		# 	dict.get(nodoActual) es O(1) <- hash(nodoActual)
		# 	https://www.quora.com/Why-does-a-hash-table-have-O-1-search
		# 	Como el grafo es Fullconnected, |grafo.adjacency().get(nodoActual)| = |ciudades|
		# 	Por tanto el for es
		# O(N)
    for nodoAdyacente in dict(grafo.adjacency()).get(nodoActual):
			# grafo.get_edge_data nos da el peso de (nodoActual,nodoAdyacente). O los pesos (si son mas de un peso por arista)
			# path es la suma previamente calculada (camino anterior) con el peso de la actual arista
			# path va acumulando el peso para ciudada vecina a medida que se va bifurcando
			# Es el peso hasta el punto de partida (que se va acumulando) +MAS+ El peso desde el punto de partida al punto `nodoAdyacente`
			# O(1)
      path = pesos[nodoActual] + grafo.get_edge_data(nodoActual,nodoAdyacente).get('weight')
      # Evalua si el nuevo camino es menor en peso al actual
      if path < pesos[nodoAdyacente]:
        # Actualiza el nuevo peso junto con el nodo al cual se pasa
        pesos[nodoAdyacente] = path

				# Diccionario: dict['ciudad'] = 'ciudad actual'
				# nodoActual, pop(0) de `cola`
				# Crea el arbol de conexión enlazando nodos, 
				# con una definicion de 'nodoOrigen' -> 'NodoPrevio -> ... -> Raiz(Inicio)
        nodosPrevios[nodoAdyacente] = nodoActual
				# dict
				# 	['Bogota']=B/manga
				# 	['Cali']=B/manga
				# 	['Pereria']=B/manga
				# 	....

        cola.append(nodoAdyacente)
				#
			#Fin for: 
			# 1era iteracion va a agregar a cola todos los vecinos.
			# 2da iteracion

	# Se recorre el arbol de conexión representado en los enlaces de
	# nodosPrevios, para ir teniendo en cuenta los nodos
  node = destino
  path = []
  peso = pesos[node]
  while node != inicio:
    path.append(node)
    node = nodosPrevios[node]
  path.append(node) 
  path.reverse()

  return path, peso