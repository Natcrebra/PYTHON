#progreso de ejecución de un programa
n=5000000
for i in range(n):
	print('%5.1f%%'%(100*i/n),end='\r')
	
