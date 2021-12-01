# Lab3 Grupo 9: Método de bisección
[Google Docs de enunciado](https://docs.google.com/document/d/17PbQ12ueK_aBHzUAt4S3vwtmE4-OyNAEduATqXiE5cE/edit)

[Google Slides del Método de bisección](https://docs.google.com/presentation/d/1qtsbJFTalOlM7qdlacQk5FTIT5Tq7c23iIX81jkiwac/edit?usp=sharing)

 ```python
def biseccion(f,a,b,tol):                           # O(1)
    if (func(f,a) * func(f,b) >= 0):                # O(1)
        print("Los intervalos no son correctos")    # O(1)
        exit()                                      # O(1)
    N=1                                             # O(1)
    NMAX=1000                                       # O(1)
    while (N<=NMAX):                                # O(M)
        c = (a+b)/2                                 # O(1)
        error=(b - a)/2                             # O(1)
        if (func(f,c) == 0.0 or (error < tol)):     # O(1)
            break                                   # O(1)
        if (func(f,c)*func(f,a) < 0):               # O(1)
            b = c                                   # O(1)
        else:                                       # O(1)
            a = c                                   # O(1)
        N+=1                                        # O(1)
    return c                                        # O(1)
```

