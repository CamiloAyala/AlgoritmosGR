import time
#
sumador=0
multiplicador=int(input("Ingrese el primer número (positvo y de max. 5 dígitos): "))
while(multiplicador < 0 or multiplicador >= 100000):
  multiplicador=int(input("Error: Ingrese el primer número nuevamente: "))

multiplicando=int(input("Ingrese el segundo número (positvo y de max. 5 dígitos): "))
while(multiplicando < 0 or multiplicando >= 100000):
  multiplicando=int(input("Error: Ingrese el segundo número nuevamente: "))

inicio=time.time()
print(inicio)
while (multiplicador>0):

  """"
  Si el `multiplicador` toma un valor impar (su LSB es 1) al dividirlo 
  entre 2, entonces al resultado se le suma el valor que tenga en ese 
  momento el `multiplicando`
  """
  if (multiplicador & 1):
    sumador = sumador + multiplicando
    
  """
  Actualizar el valor del `multiplicador` dividiendolo por 2:
  en binario básicamente es 7_10 que es 111_2 al correr los bits a
  a la derecha 1 espacio quitando el LSB entonces 7_10 quedaría 11_2 
  que ahora sería 3_10
  """    
  multiplicador >>= 1

  """
  Actualizar el valor del `multiplicando` multiplicándolo por 2:
  en binario básicamente es 7_10 que es 111_2 al correr los bits a
  a la izquierda 1 espacio agregando un 0 en el LSB entonces 7_10 quedaría 1110_2 
  que ahora sería 14_10
  """     
  multiplicando <<= 1
  
fin=time.time()
print("El resultado es: ",sumador)
print("El tiempo que toma el algoritmo es: %.10f segundos"% (fin-inicio))