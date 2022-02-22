
import math


def funcion_exponencial(x):

    suma = 0
    n = 10

    for n in range(0, n):
        suma += math.pow(x, n)/math.factorial(n)

    return suma


print("Resultado de la funcion_exponencial: ", funcion_exponencial)
print("Resultado con la funcion math.exp: ", math.exp(5))
