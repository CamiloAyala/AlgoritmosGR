# Taller1
* [Ivan Fernando Caseres Rosas ](mailto:icaseres@unal.edu.co)
* [Camilo Arturo Echeverry Ayala](mailto:cecheverry@unal.edu.co)
* [Gerardo Andres Hormiga González](mailto:gahormigag@unal.edu.co)
* [Fredy Andres Rosero Cristancho](mailto:faroseroc@unal.edu.co)

A continuación definimos el costo de cada instrucción de nuestro código:

    secuence = "['>NC_045512.2 Severe..."  -> O(1)
    target = "CTCCAAACAATTGCAACAATCCATGAGCAG"  -> O(1)
    
    n = len(target)  -> O(1)
    f = len(secuence) - n  -> O(1)

    for i in range(f):  -> O(n)
      substring = secuence[i:i+n]  -> O(1)
      counter = 0  -> O(1)
      
      for idx, char in enumerate(target):  -> O(n) 

        coincidencia_char = char == substring[idx]  -> O(1)
    
        if not coincidencia_char: ->O(1)*1
          counter = 0 -> O(1)
          break -> O(1)

        counter=counter+1  -> O(1)

      if (counter==n):  ->O(1)*1
        print("posición incial:", i)  -> O(1)
        print("posición final:", i+n)  -> O(1)
        break  -> O(1)

El calculo del Big(O) es:

    4*O(1) + O(n)[ 2*O(1) + O(n)[ 5*O(1) ]  + 4*O(1)^1 ]
    4*O(1) + O(n)[ 2*O(1) + 5*O(n) + 4*O(1) ]
    4*O(1) + O(n)[ 6*O(1) + 5*O(n) ]
    4*O(1) + 6*O(1)*O(n) + 5*O(n)*O(n)
   
A continuación despreciamos los costos insignificativos para el peor escenario

    O(1)*O(n) + O(n)*O(n)
    O(n) + O(n^2)
    O(n^2)
    
El algoritmo tiene un costo de `O(n^2)`
