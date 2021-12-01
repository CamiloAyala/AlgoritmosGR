# Lab3 Grupo 9: Método de bisección


 ```python
def biseccion(f,a,b,tol):
    if (func(f,a) * func(f,b) >= 0):
        print("Los intervalos no son correctos")
        exit()
    N=1
    NMAX=1000
    while (N<=NMAX):
        c = (a+b)/2
        error=(b - a)/2
        if (func(f,c) == 0.0 or (error < tol)):
            break
        if (func(f,c)*func(f,a) < 0):
            b = c
        else:
            a = c
        N+=1
    return c
```
