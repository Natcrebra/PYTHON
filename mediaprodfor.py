n=int(input('n? '))
media=0; prod=1
for i in range(n):
	x=float(input('x? '))
	media+=x
	prod*=x
print('media=%g prod=%g'%(media/n,prod))

