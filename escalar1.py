#producto escalar de dos vectores
n=int(input('n? '))
#v=[]; w=[]; 
v=[0]*n; w=[0]*n
p=0
for i in range(n):
	j=i+1 #para que empiece en 1
	vi=float(input('v(%i)? '%j)) #te indica por qué iteración vas
	wi=float(input('w(%i)? '%j))
	#v=v+[vi]; w=w+[wi]
	#v.append(vi);w.append(wi)
	p+=v[i]*w[i]
print('v·w=%g'%p)
