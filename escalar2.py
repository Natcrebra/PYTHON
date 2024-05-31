from numpy import *

while True:
	v=float_(input ('v? ').split())
	w=float_(input ('w? ').split())
	if len(v)==len(w):
		break

print('v·w=%g'%dot(v,w))

		
