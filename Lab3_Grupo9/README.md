# Lab3 Grupo 9: Método de bisección
[Google Docs de enunciado](https://docs.google.com/document/d/17PbQ12ueK_aBHzUAt4S3vwtmE4-OyNAEduATqXiE5cE/edit)

[Google Slides del Método de bisección](https://docs.google.com/presentation/d/1qtsbJFTalOlM7qdlacQk5FTIT5Tq7c23iIX81jkiwac/edit?usp=sharing)

 ```python
def biseccion(f,a,b,tol):                           # O(1)
    if (func(f,a) * func(f,b) >= 0):                # O(1)
        print("Los intervalos no son correctos")    # O(1)
        exit()                                      # O(1)
    error=(b - a)/2                                 # O(1)
    while (error > tol):                            # O(M)
        c = (a+b)/2                                 # O(1)
        error=(b-a)/2                               # O(1)
        if (func(f,c) == 0.0):                      # O(1)
            break                                   # O(1)
        if (func(f,c)*func(f,a) < 0):               # O(1)
            b = c                                   # O(1)
        else:                                       # O(1)
            a = c                                   # O(1)
    return c                                        # O(1)
```

¿Cuándo se rompe el ciclo?  
error > tol
(b-a)/2 > tol
El intervalo incial [a,b]
se empieza a acotar exactamente por la mitad
independientemente que a o b sean los que cambien por c.

¿Cuando el error es menor o igual a tol?
Cuando se ha divido (b-a)/2, (b-a)/2, (b-a)/2, ...(b-a)/2 <= tol

Entonces tenemos  

![formula](https://render.githubusercontent.com/render/math?math=\color{white}\large\(b-a)=((b-a)/2) )  

![formula](https://render.githubusercontent.com/render/math?math=\color{white}\large\(b-a)/2^{x}<=tol )

![formula](https://render.githubusercontent.com/render/math?math=\color{white}\large\b-a%2F2^{x}%3C=tol)

(b-a)/2^{x} <=tol
2^{x}/(b-a) <= 1/tol
2^{x}/(b-a)=1/tol
2^{x}=(b-a)/tol
log_2(2^{x})=log_2((b-a)/tol)
x*log_2(2)=log_2((b-a)/tol)
x=log_2((b-a)/tol)


Como en cada iteración se busca el punto medio del intervalo:  

![formula](https://render.githubusercontent.com/render/math?math=\color{white}\large\C_1=(b-a)/2)

```
![formula](https://render.githubusercontent.com/render/math?math=\color{white}\large\(b-a)=(b-a)/2)
(b-a)/2^{x} <=tol
2^{x}/(b-a) <= 1/tol
2^{x}/(b-a)=1/tol
2^{x}=(b-a)/tol
log_2(2^{x})=log_2((b-a)/tol)
x*log_2(2)=log_2((b-a)/tol)
x=log_2((b-a)/tol)
```