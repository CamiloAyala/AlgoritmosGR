import time

n=int(input("Ingrese un número menor o igual a 100: "))
while n > 100:
  n=int(input("Ingrese un número válido: "))
  
inicio=time.time()
actual = 0
siguiente = 1

for k in range(n):
    # guardamos la suma
    """
    Aquí `siguiente` es i_{n-2} porque esta desactualizado. Consecuentemente `actual`
    es i_{n-1}. Guardamos en memoria la suma i_{n-2} + i_{n-1} que seria i_{n} ...
    """
    suma = actual + siguiente  # (i_{n-2} + i_{n-1})
    """
    Ahora corremos i_{n-1} a i_{n-2}
    """
    actual = siguiente #
    """
    y i_{n-1} ahora tiene el valor de i_{n}, es decir, el valor de (i_{n-2} + i_{n-1})
    """
    siguiente = suma # n+1 = (n-1 + n)
    
fin=time.time()
print("El resultado es: ",actual)
print("El tiempo que toma el algoritmo es: %.10f segundos"% (fin-inicio))
