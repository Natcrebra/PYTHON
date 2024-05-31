from numpy import *

v=float_(input('v? ').split())
w=float_(input('w? ').split())
s1=0;n=len(v) #defino los acumuladores

for i in range(n):
	s2=0
	for j in range(i+1):
		s2+=v[i]*w[j]
	s1+=s2
	
print('suma=%g'%s1)#se pone al final del todo pq no se itera, solo imprime.




