# Multiplicación LaRusse
[README](README.md)

    while (multiplicador>0):                        -> O(log_2(multiplicador)+1)
        if (multiplicador & 1):                     -> 1 * O(1)
            sumador = sumador + multiplicando       -> O(1)
        multiplicador >>= 1                         -> O(1)
        multiplicando <<= 1                         -> O(1)
    

¿Cuando se rompe el ciclo?

* Cuando multiplicador es igual o menor que cero

¿Cuando multiplicador es igual o menor que cero?

* cuando se divida multiplicador/2 las suficientes veces hasta que de <1

¿Cuantas veces?

* multiplicador/2, multiplicador/2, multiplicador/2,... multiplicador/2=0.5

es decir tenemos esta ecuación `multiplicador/2^{x}=1/2`

    multiplicador/2^x=1/2
    2^{x}/multiplicador=2
    2^{x}=2*multiplicador
    log_2(2^{x})=log_2(2*multiplicador)
    x*log_2(2)=log_2(2*multiplicador)
    x=log_2(2*multiplicador)
    x=log_2(2)+log_2(multiplicador)
    x=1+log_2(multiplicador)

El calculo del Big-O es el siguiente:

    O(log_2(multiplicador)+1)*(1*O(1) + O(1) + O(1) + O(1))
    O(log_2(multiplicador)+1)*(4*O(1))

Omitiendo los costos insignificativos tenemos que el método de la multiplicación rusa tiene una complejidad de `log_2(multiplicador) + 1`
