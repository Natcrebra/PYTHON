from pylab import *
from numpy import *

n=101;t=arange(n)
b=2.5;w=pi/10;theta=pi/2
u=w*t+theta;z=sin(u)
x=b*z;v=b*w*cos(u);a=-b*w**2*z

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

savefig('armonico3.png')#para guardar la gráfica en un fichero


	



