"""
Curva: https://www.geogebra.org/calculator/mdkdzxmg
"""
import time

def func(f,x):
    x=x
    return eval(f)
    #return -x** 4 + 30*(x)**3 + 15*(x)**2 + 34*x + 540
    # En la práctica se puede modelar desde las entradas y salidas de un sistema desconocido, 

def biseccion(f,a,b,tol):
    """
    Este método al utilizar un recta AB que necesariamente intersecta el ejeX
    necesita que los puntos que la crean sean de diferente signo, sea A=(a,f(a)) y B=(b,f(b))
    Para tal condición f(a) y f(b) deben tener diferente signo es decir f(a)*f(b)<0
    """
    if (func(f,a) * func(f,b) >= 0):
        print("Los intervalos no son correctos, f(a) * f(b) = {} * {} es positivo".format(func(f,a),func(f,b)))
        exit()

    """
    Necesitamos entonces hacer el intervalo [a,b] lo mas pqueño posible
    cambiando ya sea punto de la izquierda `a` o el de la derecha `b` por un punto mas cercano a la raíz
    """
    error=(b - a)/2
    while (error > tol):
        """
        Ese punto mas cercano es que el que está justo en la mitad del intervalo.
        """
        c = (a+b)/2

        """
        Suponemos que la raiz c esta en [a,b]
        por tanto tenemos que por izquierda tenemos un error de [a,c] y por derecha un error de [c,b]
        entonces el error es la mitad distancia de ese intervalo [a,b]
        [a]------------[c]------------[b]
            {-(b-a)/2}     {+(b-a)/2}
        """
        error=(b - a)/2
        if (func(f,c) == 0.0):
            break

        """
        Sea A=(a,f(a)) y B=(b,f(b))
        Tenemos dos posiblidades: Recortar el intervalo por derecha o recortar el intervalo por izquierda.
        El criterio es tan sencillo como que la linea recta AB coret al ejeX sea

        f(a)
        |
        [a]------[c]------[b]
                        |
                        f(b)                                              

        Si la imagen de a y la imagen de c tienen disinto signo: Recortar el intervalo por derecha: b<=C
        f(a)
        |
        [a]------[c]------[b]
                |         
                f(c)        

        [a]------[b]......[ ]

        Si la imagen de c y la imagen de b tienen disinto signo: recortar el intervalo por izquierda: a<-c
                        f(b)
                        |
        [a]------[c]------[b]
                |              
                f(c)       

        [ ]......[a]------[b]    

        """
        if (func(f,c)*func(f,a) < 0):
            b = c
        else:
            a = c
    return c

inicio=time.time()
# para este caso tomar el intervalo de [0,1000]=[X0,X1]
a=0
b=1000
# Resolución +-0.001
tol=0.001
# Su modelo a evaluar será: -x^4+30x^3+15x^2+34x+540=0 
f="-x** 4 + 30*(x)**3 + 15*(x)**2 + 34*x + 540"
raiz = biseccion(f,a,b,tol)
fin=time.time()
print("El valor de la raíz para {} es: {:.4}".format(f, raiz))
print("El tiempo que toma el algoritmo es: %.10f segundos"% (fin-inicio))

# Seccion 2: Variando los parámetros del modelo:
f="-x** 4 + 30*(x)**3 + 15*(x)**2 + 34*x"
print("El valor de la raíz para {} es: {:.4}".format(f, biseccion(f,1,b,tol)))

