import time

num=int(input("Ingrese un número menor o igual a 100: "))
while num >100:
  num=int(input("Ingrese un número válido: "))
  
ini=time.time()
a = 0
b = 1
for k in range(num):
    c = b+a
    a = b
    b = c
fin=time.time()
print("El resultado es: ",a)
print("El tiempo que toma el algoritmo es: %.10f segundos"% (fin-ini))
