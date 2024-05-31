from pylab import *
from math import *

n=101;t=range(n)
x=[0]*n;v=[0]*n;a=[0]*n #inicializando listas
b=2.5;w=pi/10;theta=pi/2

for i in t:
	u=w*i+theta;z=sin(u)
	x[i]=b*z
	v[i]=b*w*cos(u)
	a[i]=-b*w**2*z

clf();plot(t,x,'b*:', label='Posición (m)')
plot(t,v, color='red', marker='d', linestyle='--', label='Velocidade (m/s)')
plot(t,a,'g',linewidth=5, label='Aceleración (m/s²)')

#definimos la leyenda:
l=legend(loc='center left', bbox_to_anchor=(1,0.5))
savefig('armonico.png', bbox_extra_artists=(l,),bbox_inches='tight')#para guardar la gráfica en un fichero
show() #para que nos muestre la gráfica

	



