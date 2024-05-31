from sys import *
for i in argv:
	print('%s'%i)
#otra forma de hacerlo con los indices:
n=len(argv)
for i in range(n):
	print('argumento %i: %s'%(i, argv[i]))
n=int(argv[2])
x=float(argv[3])
print('n+x=%g'%(n+x))
