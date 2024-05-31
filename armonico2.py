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

clf();subplots_adjust(hspace=0.5)
subplot(311)
plot(t,x,'b*:', label='Posición (m)')
xlabel('Tempo(s)');ylabel('Posición (m)')
subplot(312)
plot(t,v, color='red', marker='d', linestyle='--', label='Velocidade (m/s)')
xlabel('Tempo(s)'); ylabel('Velocidade (m/s)')
subplot(313)
plot(t,a,'g',linewidth=5, label='Aceleración (m/s²)')
xlabel('Tempo(s)');ylabel('Aceleración (m/s²)')

savefig('armonico2.png')#para guardar la gráfica en un fichero


	



