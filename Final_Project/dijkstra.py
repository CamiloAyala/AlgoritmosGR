from queue import PriorityQueue
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
	
  pesosOptimos = {v: math.inf for v in list(nx.nodes(grafo))}
	# excepto al nodo de origen...
	# O(1)
  pesosOptimos[inicio] = 0

	# Cuando se cacula la distancia relativa a un nodo
	# Previene que se tengan en cuenta caminos mas largos
	# O(1)
  vecinosSinVisitar = PriorityQueue()

	# Desde el punto de vista del arbol,
	# Desde la raiz el primer vecino es el nodo de partida (inicio)  
	# O(1)
  vecinosSinVisitar.put((pesosOptimos[inicio], inicio))

	# Mientras hayan vecinos optimos que recorrer
	# Una arista nunca va estar mas de una vez en la cola `vecinosSinVisitar`
	# Si tenemos A,B,C,D,E,F estos estaran a lo mucho distribuidos en el tiempo en la cola
	# 1 {C}
	# 2 {A,B}
	# 3 {D,E}
	# 4 {F}
	
	# ó 
	# 1 {C}
	# 2 {A,B,D,E}
	# 4 {F}	

	# ò Tdoos vecinos inmediatos de C:
	# 1 {C}
	# 2 {A,B,D,E,F}

	# ò Todos en hilera:
	# 1 {C}
	# 2 {A}	
	# 3 {B}	
	# 4 {D}	
	# 5 {E}	
	# 6 {F}	
	# O(N)
  while vecinosSinVisitar.qsize() != 0: # -> O(N)*(O(E) + O(log N))
		# Extraer y eliminar: Como esta basado en un arbol binario tiene que reacomodar la mitad de los elementos
		# O(log N)
    _ , nodoActual = vecinosSinVisitar.get()
    
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
		# O(E)
    for nodoAdyacente in dict(grafo.adjacency()).get(nodoActual):
			# grafo.get_edge_data nos da el peso de (nodoActual,nodoAdyacente). O los pesos (si son mas de un peso por arista)
			# path es la suma previamente calculada (camino anterior) con el peso de la actual arista
			# path va acumulando el peso para ciudada vecina a medida que se va bifurcando
			# Es el peso hasta el punto de partida (que se va acumulando) +MAS+ El peso desde el punto de partida al punto `nodoAdyacente`
			# O(1)
      caminoAcumulado = pesosOptimos[nodoActual] + grafo.get_edge_data(nodoActual,nodoAdyacente).get('weight')
      # Evalua si el nuevo camino es menor en peso al actual
	  	# ES una ruta mejor u optima?
      if caminoAcumulado < pesosOptimos[nodoAdyacente]:
        # Actualiza el nuevo peso junto con el nodo al cual se pasa
        pesosOptimos[nodoAdyacente] = caminoAcumulado

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

        vecinosSinVisitar.put((caminoAcumulado, nodoAdyacente)) # ->O(1)
				#
			#Fin for: 
			# 1era iteracion va a agregar a cola todos los vecinos.
			# 2da iteracion

	# Se recorre el arbol de conexión representado en los enlaces de
	# nodosPrevios, para ir teniendo en cuenta los nodos
  nodo = destino
  camino = []
  peso = pesosOptimos[nodo]
  while nodo != inicio: # -> O(N-1): i.e.: Arbol como un Linked list lineal
    camino.append(nodo)
    nodo = nodosPrevios[nodo]
  camino.append(nodo) 
  camino.reverse()

  return camino, peso


