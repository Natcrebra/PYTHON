from numpy import *
from numpy.random import *
from numpy.linalg import *


while True:
	n=int(input('n?(par,10<n<20? '))
	if n>=10 and n<=20 and n%2==0:
		break
#---------------------------------------------------------------------------
x= 100*random(n)
v=x[range(0,n,2)]
w=x[range(1,n,2)]
print('v= ',v, 'w= ',w)
#------------------------------------------------------------------------------
m=int(n/2); a=zeros([m,m])
for i in range(m):
	for j in range(m):
		if i>j:
			a[i,j]=v[i]*w[j]
		elif i==j:
			a[i,j]=v[i]/(w[j]+1)
		else:
			a[i,j]=sum(v[:j+1])*sum(w[:i+1])
#--------------------------------------------------------------------------------
print('a: ',a)
print('media: ', mean(a))
print('det: ',det(a))
