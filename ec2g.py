from math import *

a=float(input('a? '))
b=float(input('b? '))
c=float(input('c? '))
if a==0:
	if b==0:
		if c==0:
			print('x=IR') #IR: toda la recta real
		else:
			print('x=ø')
		
	else:
		print('x=%g'%(-c/b))
else:
	d=b**2-4*a*c ; a2=2*a
	if d<0:
		re=-b/(2*a); im=sqrt(-d)/a2
		print('x1=%g+I·%g'%(re,im))
		print('x2=%g-I·%g'%(re,im))
	elif d==0:
		print('x1=x2=%g'%(-b/a2))
	else:
		rd=sqrt(d)
		x1=(-b+rd)/a2;print('x1=%g'%x1)
		x2=(-b-rd)/a2;print('x2=%g'%x2)





