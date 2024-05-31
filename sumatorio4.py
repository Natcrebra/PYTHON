from numpy import *

v=[float(i)for i in input('v? ').split()]
w=[float(i)for i in input('w? ').split()]
s1=0;n=len(v) #defino los acumuladores

for i in range(n):
	s1+=v[i]*sum(w[:i+1]) #hemos vectorizado el bucle anterior 
	
print('suma=%g'%s1)#se pone al final del todo pq no se itera, solo imprime.




