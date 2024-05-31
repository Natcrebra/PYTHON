from numpy import *

v=[float(i)for i in input('v? ').split()]
w=[float(i)for i in input('w? ').split()]
s1=0;n=len(v) #defino los acumuladores

for i in range(n):
	s2=0
	for j in range(i+1):
		s2+=w[j]
	s1+=v[i]*s2
	
print('suma=%g'%s1)#se pone al final del todo pq no se itera, solo imprime.




