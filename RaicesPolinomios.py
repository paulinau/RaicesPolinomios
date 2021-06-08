#Ugalde Carreño Paulina 19141209
#coding: utf-8
from Horner import *
from Bairstow import *
from math import pow, inf
import sys

#Pedimos el grado del polinomio y este debe ser mayor a 0
grado = 0
while grado<=0:
    grado = int(input("Grado del polinomio (>0): "))

#Array donde se guardaran los coeficientes de nuestro polinomio
coeficientes = []

# Ingresamos los coeficientes del polinomio comenzando con el termino de mayor grado y terminando 
print("Ingresa los coeficientes comenzando por el termino de mayor grado y terminando con el termino independiente ")
for i in range(grado+1):
    coeficiente = float(input("Ingresa el coeficiente: "))
    coeficientes.append(coeficiente)
coeficientes.reverse()

#Pedimos las cifras significativas
csig = int(input("Cifras significativas: "))

#Primera y segunda derivada de nuestro polinomio
primeraDerivada = deriva(coeficientes) 
segundaDerivada = deriva(primeraDerivada)     

#Valores que necesita el algoritmo de Bairstow
r = coeficientes[0]/coeficientes[-1]
s = r
r1 = primeraDerivada[0]/primeraDerivada[-1]
if(grado==1):
    r2=1
else:
    r2 = segundaDerivada[0]/segundaDerivada[-1]
s1 = r1
s2 = r2
tolerancia = 0.5*pow(10, 2-csig)

#Listas donde vamos a guardar las raices
raiz = []
raiz_derivada1 = []
raiz_derivada2 = []

# Metodo con el cual se obtienen las raices reales y complejas
Bairstow(coeficientes, r, s, grado, raiz, tolerancia)
Bairstow(primeraDerivada, r1, s1, grado-1, raiz_derivada1, tolerancia)
Bairstow(segundaDerivada, r2, s2, grado-2, raiz_derivada2, tolerancia)

#las raices con +0j son normales y nos quedamos solo con la parte real
for i in range (len(raiz)): 
    if(complex(raiz[i]).imag==0):
        raiz[i]=raiz[i].real
for i in range (len(raiz_derivada1)): 
    if(complex(raiz_derivada1[i]).imag==0):
        raiz_derivada1[i]=raiz_derivada1[i].real
for i in range (len(raiz_derivada2)): 
    if(complex(raiz_derivada2[i]).imag==0):
        raiz_derivada2[i]=raiz_derivada2[i].real

#Separar raices complejas de las reales
#si está vacía, no tiene max, min, ni tampoco crece o decrece
raiz_derivada1 = [x for x in raiz_derivada1 if type(x) is not complex]
raiz_derivada2 = [x for x in raiz_derivada2 if type(x) is not complex]

# Máximos y mínimos
maximos = []              
minimos = []

# Definimos una constante, esta tendrá la función siguiente:
# si contamos con una raíz 2, se evalua el polinomio en 1.9 y en 2.01
c = 1/pow(10, csig)

if(len(raiz_derivada1)!=0):
    for x in raiz_derivada1:
        # Para evaluar la funcion, usamos el algoritmo de horner
        izquierda = horner(grado-1, primeraDerivada, (x-c))
        derecha = horner(grado-1, primeraDerivada, (x+c))

        if (izquierda < 0 and derecha > 0): 
            minimos.append((x, horner(grado, coeficientes, x)))

        elif (izquierda > 0 and derecha < 0): 
            maximos.append((x, horner(grado, coeficientes, x)))
else: #Si raiz_derivada1 esta vacio, no hay maximos ni minimos
    maximos.append("No hay máximos")
    minimos.append("No hay minimos")

# Puntos de inflexion
puntos_inflexion = []
if(len(raiz_derivada2)!=0):
    if(grado > 2):
        for x in raiz_derivada2:
            puntos_inflexion.append((x, horner(grado, coeficientes, x)))
    else:
        puntos_inflexion.append("polinomios de grado <= 2 no tienen puntos de inflexion ni concavidad")
else:
    puntos_inflexion.append("no hay puntos de inflexion")

#Creciente y decreciente
crece = []
decrece = []
#ordenamos la lista
raiz_derivada1.sort()

#la función no crece ni decrece cuando el grado=1 (index out of range)
if(grado==1):
    crece.append("La función no crece ni decrece cuando grado = 1")
    decrece.append("La función no crece ni decrece cuando grado = 1")
else:
    if(len(raiz_derivada1)!=0):
        for i in range(1, len(raiz_derivada1)):
            if horner(grado-1, primeraDerivada, raiz_derivada1[i]-c) < 0:
                decrece.append((raiz_derivada1[i-1], raiz_derivada1[i]))
            else:
                crece.append((raiz_derivada1[i-1], raiz_derivada1[i]))

        if horner(grado-1, primeraDerivada, raiz_derivada1[-1]+c) < 0:
            decrece.append((raiz_derivada1[-1], inf))
        else:
            crece.append((raiz_derivada1[-1], inf))

        if horner(grado-1, primeraDerivada, raiz_derivada1[0]-c) < 0:     
            decrece.append((-inf, raiz_derivada1[0]))
        else:
            crece.append((-inf, raiz_derivada1[0])) 
    else:
        crece.append("no crece")
        decrece.append("no decrece")

#Intervalos de concavidad
arriba = []
abajo = []
#ordenamos la lista
raiz_derivada2.sort()

# Es concava hacia abajo cuando la segunda derivada es negativa
# es concava hacia arriba cuando la segunda derivada es positiva
if(len(raiz_derivada2)!=0):
    if(grado>2):
        for i in range(1, len(raiz_derivada2)):
            if horner(grado-2, segundaDerivada, raiz_derivada2[i]-c) < 0:
                abajo.append((raiz_derivada2[i-1], raiz_derivada2[i]))
            else:
                arriba.append((raiz_derivada2[i-1], raiz_derivada2[i]))

        #intervalo de x a infinito
        if horner(grado-2, segundaDerivada, raiz_derivada2[-1] + c) < 0:
            abajo.append((raiz_derivada2[-1], inf))
        else:
            arriba.append((raiz_derivada2[-1], inf))

        #intervalo de -infinito a x
        if horner(grado-2, segundaDerivada, raiz_derivada2[0] - c) < 0:
            abajo.append((-inf, raiz_derivada2[0]))
        else:
            arriba.append((-inf, raiz_derivada2[0]))
    else:
        arriba.append("no hay concavidad hacia arriba en polinomios con grado <=2")
        abajo.append("no hay concavidad hacia abajo en polinomios con grado <=2")
else:
    arriba.append("no hay concavidad hacia arriba")
    abajo.append("no hay concavidad hacia abajo")

#Mostramos en pantalla los resultados obtenidos
print("-------------------------------------------------------------")
print("RAICES REALES E IMAGINARIAS: ")
for i in raiz:
    print(i, end=", ")

print("\nMAXIMOS:")
for x in maximos:
    print(x, end=", ")
    
print("\nMINIMOS:")
for x in minimos:
    print(x, end=", ")

print("\nPUNTOS DE INFLEXION")
for x in puntos_inflexion:
    print(x, end=", ")

print("\nCRECIENTE EN EL INTERVALO: ")
for x in crece:
    print(x, end=", ")

print("\nCRECIENTE EN EL INTERVALO: ")
for x in decrece:
    print(x, end=", ")

print("\nCONCAVA HACIA ARRIBA EN EL INTERVALO: ")
for x in arriba:
    print(x, end=", ")

print("\nCONCAVA HACIA ABAJO EN EL INTERVALO: ")
for x in abajo:
    print(x, end=", ")

print("\n-------------------------------------------------------------")