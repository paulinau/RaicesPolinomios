#Ugalde Carreño Paulina 19141209
import cmath as cmath
import math 
import sys

# Funcion de horner para evaluar el polinomio
def horner(grado, coeficientes, x):
    polinomio = coeficientes[grado]
    k = grado - 1
    while (k >= 0):
        polinomio = coeficientes[k] + (polinomio*x)
        k = k - 1
        # Al término de este ciclo WHILE, la variable polinomio tiene el valor del P(x)
    return polinomio

# Funcion de derivacion que deriva el polinomio
def deriva(coeficientes):
    derivada = []
    k = 1
    if((len(coeficientes)) == 1):
        derivada.append(0)
    else:
        while(len(coeficientes)>k): 
            derivada.append(coeficientes[k]*k)
            k=k+1

    return derivada 