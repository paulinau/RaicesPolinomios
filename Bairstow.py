#Ugalde Carreño Paulina 19141209
import cmath as cmath
import math 
import sys

def Bairstow(coeficientes, r, s, grado, raiz, tolerancia):
	if(grado<1):
		return None
	if((grado==1) and (coeficientes[1]!=0)):
		raiz.append((float(coeficientes[0])/float(coeficientes[1]))*(-1))
		return None
	if(grado==2):
		D = (coeficientes[1]**2.0)-(4.0)*(coeficientes[2])*(coeficientes[0])
		if(D<0):
			X1 = (-coeficientes[1] - cmath.sqrt(D))/(2.0*coeficientes[2])
			X2 = (-coeficientes[1] + cmath.sqrt(D))/(2.0*coeficientes[2])
		else:
			X1 = (-coeficientes[1] - math.sqrt(D))/(2.0*coeficientes[2])
			X2 = (-coeficientes[1] + math.sqrt(D))/(2.0*coeficientes[2])
		raiz.append(X1)
		raiz.append(X2)
		return None
	n = len(coeficientes)
	b = [0]*len(coeficientes)
	c = [0]*len(coeficientes)
	b[n-1] = coeficientes[n-1]
	b[n-2] = coeficientes[n-2] + r*b[n-1]
	i = n - 3
	while(i>=0):
		b[i] = coeficientes[i] + r*b[i+1] + s*b[i+2]
		i = i - 1
	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n - 3
	while(i>=0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i - 1
	Din = ((c[2]*c[2])-(c[3]*c[1]))**(-1.0)
	r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
	s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
	if(abs(b[0])> tolerancia or abs(b[1])>tolerancia):
		return Bairstow(coeficientes,r,s,grado,raiz, tolerancia)
	if (grado>=3):
		Dis = ((r)**(2.0))+((4.0)*(1.0)*(s))
		X1 = (r - (cmath.sqrt(Dis)))/(2.0)
		X2 = (r + (cmath.sqrt(Dis)))/(2.0)
		raiz.append(X1)
		raiz.append(X2)
		return Bairstow(b[2:],r,s,grado-2,raiz, tolerancia)