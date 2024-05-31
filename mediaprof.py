
#introducimos el número de elementos/iteraciones
n=int(input('n? '))
i=0; media=0 ; prod=1#i,media,prod=0,0,1 ;otra forma
#el acumulador es la variable media y acabamos de inicializarlo
#primero con sentencia while:
while i<n:
	x=float(input('x? ')) #introducimos el valor de cada elemento
	media=media+x
	prod=prod*x
	print('media=%g prod=%g'%(media, prod))#para ver como van cambiando estas 												variables
	#i=i+1
	i+=1
print('media=%g prod=%g'%(media/n, prod))








