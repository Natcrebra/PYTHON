from numpy import *

v=[float(i)for i in input('v? ').split()]
w=[float(i)for i in input('w? ').split()]
s1,s2=0,0;n=len(v) #defino los acumuladores

for i,j in zip(v,w):

	s2+=j;s1+=i*s2
	
print('suma=%g'%s1)#se pone al final del todo pq no se itera, solo imprime.




