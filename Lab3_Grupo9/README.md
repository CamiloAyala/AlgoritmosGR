# Lab3 Grupo 9: Método de bisección
[Google Docs de enunciado](https://docs.google.com/document/d/17PbQ12ueK_aBHzUAt4S3vwtmE4-OyNAEduATqXiE5cE/edit)

[Google Slides del Método de bisección](https://docs.google.com/presentation/d/1qtsbJFTalOlM7qdlacQk5FTIT5Tq7c23iIX81jkiwac/edit?usp=sharing)

 ```python
def biseccion(f,a,b,tol):                           # O(1)
    if (func(f,a) * func(f,b) >= 0):                # O(1)
        print("Los intervalos no son correctos")    # O(1)
        exit()                                      # O(1)
    error=(b - a)/2                                 # O(1)
    while (error > tol):                            # O(log_2((b-a)/tol))
        c = (a+b)/2                                 # O(1)
        error=(b-a)/2                               # O(1)
        if (func(f,c) == 0.0):                      # O(1)^1
            break                                   # O(1)
        if (func(f,c)*func(f,a) < 0):               # O(1)^1
            b = c                                   # O(1)
        else:                                       # O(1)^1
            a = c                                   # O(1)
    return c                                        # O(1)
```
## ¿Cuándo se rompe el ciclo?  
El intervalo incial [a,b] se empieza a acotar exactamente por la mitad
independientemente que a o b sean los que cambien por c.

    error > tol
    (b-a)/2 > tol

## ¿Cuando el error es menor o igual a tol?
Cuando se ha divido (b-a)/2, (b-a)/2, (b-a)/2, ...(b-a)/2, x veces tal que `(b-a)/2 <= tol`

Entonces tenemos:   

![(b-a)/2^{x}<=tol](https://render.githubusercontent.com/render/math?math=\color{white}\large\%5Cleft(b-a%5Cright)%2F2%5E%7Bx%7D%20<%3Dtol)  

![2^{x}/(b-a)<=1/tol](https://render.githubusercontent.com/render/math?math=\color{white}\large\2%5E%7Bx%7D%2F%28b-a%29%20%3C%3D%201%2Ftol)  

![2^{x}/(b-a)=1/tol](https://render.githubusercontent.com/render/math?math=\color{white}\large\2%5E%7Bx%7D%2F%28b-a%29%3D1%2Ftol)  

![2^{x}=(b-a)/tol](https://render.githubusercontent.com/render/math?math=\color{white}\large\2%5E%7Bx%7D%3D%28b-a%29%2Ftol)  

![log_2(2^{x})=log_2((b-a)/tol)](https://render.githubusercontent.com/render/math?math=\color{white}\large\log_2%282%5E%7Bx%7D%29%3Dlog_2%28%28b-a%29%2Ftol%29)  

![x*log_2(2)=log_2((b-a)/tol)](https://render.githubusercontent.com/render/math?math=\color{white}\large\x%2Alog_2%282%29%3Dlog_2%28%28b-a%29%2Ftol%29)  

![x=log_2((b-a)/tol)](https://render.githubusercontent.com/render/math?math=\color{white}\large\x%3Dlog_2%28%28b-a%29%2Ftol%29)
```
(b-a)/2^{x}<=tol
2^{x}/(b-a)<=1/tol
2^{x}/(b-a)=1/tol
2^{x}=(b-a)/tol
log_2(2^{x})=log_2((b-a)/tol)
x*log_2(2)=log_2((b-a)/tol)
x=log_2((b-a)/tol)
```
## Desarollo
El calculo del Big-O es el siguiente:

    O(1)+O(1)+O(1)+O(1)+O(1)+O(log_2((b-a)/tol))*(O(1)+O(1)+O(1)+O(1)+O(1)+O(1)+O(1)+O(1)+O(1))  
    5*O(1)+O(log_2((b-a)/tol))*(9*O(1))

Omitiendo los costos insignificativos tenemos que el método de la bisección tiene una complejidad de:

    O(log_2((b-a)/tol))

## Conclusión
Entonces la complejidad de nuestro algoritmo esta acotado en el pero caso por 

![O(log_2((b-a)/tol))](https://render.githubusercontent.com/render/math?math=\color{white}\large\O%28log_2%28%28b-a%29%2Ftol%29%29)

donde `[a,b]` es el intervalo de búsqueda y `tol` es la tolerancia en error absoluto