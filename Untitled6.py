#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
print ("e^-x")
a = int(input("Ingrese el límite: "))

def funcion_exponencial(x):
    suma = 0
    for n in range((a+1)):
        suma += math.pow(x,n) / math.factorial(n)
    return suma
    resultado = 1/suma

b = float(input("Ingrese el valor de x: "))
print("========================================================")
r = 1/funcion_exponencial(b)
print("Resultado con la función funcion_exponencial: ", funcion_exponencial(b))


# In[ ]:




