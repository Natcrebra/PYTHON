from time import *
from numpy import * 
#programa para medir el tiempo de ejecución de un programa

n=int(input('n? '))

#--------------------VERSION 1------------------------------------------------

x=[];i=0;ini=process_time() 
while i<n:
	x=x+[i*i]
	i+=1
print('(1)%.5f s'%(process_time()-ini))

#-------------------VERSION 2-------------------------------------------------
	
x=[]; i=0; ini=process_time()
while i<n:
	x.append(i*i)
	i+=1
print('(2)%.5f s'%(process_time()-ini))

#-----------------VERSION 3--------------------------------------------------

x=[0]*n;i=0;ini=process_time()
while i<n:
	x[i]=i*i
	i+=1
print('(3)%.5f s'%(process_time()-ini))

#---------------VERSION 4----------------------------------------------------

x=[0]*n;ini=process_time()
for i in range(n):
	x[i]=i*i
print('(4)%.5f s'%(process_time()-ini))

#--------------VERSION 5----------------------------------------------------

ini=process_time()
x=[i*i for i in range(n)] #para vectorizar como lista
print('(5)%.5f s'%(process_time()-ini))

#-------------VERSION 6-----------------------------------------------------

ini=process_time()
x=arange(n)**2
print('(6)%.5f s'%(process_time()-ini))

