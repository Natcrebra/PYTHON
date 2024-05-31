# IPython log file

x=4 #1 definir las variables
y=5.6
z=3
c=4+5j
d=-3+2j
b=True
m='Exemplo de python'
#calcular x+z, x², yz, resto de la division x/z, (z-x)y²,cd,c/d
x+z
#[Out]# 7
x**2
#[Out]# 16
y*z
#[Out]# 16.799999999999997
x%z
#[Out]# 1
(x-z)y**2
(x-z)*y**2
#[Out]# 31.359999999999996
c*d
#[Out]# (-22-7j)
c/d
#[Out]# (-0.15384615384615394-1.7692307692307692j)
#comproba o tipo de dato de cada variable
type(x)
#[Out]# int
type(y),type(z),type(c),type(d),type(b),type(m)
#[Out]# (float, int, complex, complex, bool, str)
y+x/2
#[Out]# 7.6
y//x
#[Out]# 1.0
#calcula o máximo e mínimo de x, y e z
floor(x)
from math import floor() and ceil()
from math import *
floor(x), ceil(x)
#[Out]# (4, 4)
floor(y), ceil(y)
#[Out]# (5, 6)
floor(z), ceil(z)
#[Out]# (3, 3)
max(x,y,z), min(x,y,z)
#[Out]# (5.6, 3)
math.factorial(x)
from math import factorial
math.factorial(x)
factorial(x)
#[Out]# 24
#Avalía as seguintes expresións: 
sen**2(pi)*cos(4*pi/3)
import math
sin**2(pi)*cos(4*pi/3)
sin**2(math.pi)*cos(4*math.pi/3)
(sin(math.pi))**2*cos(4*math.pi/3)
#[Out]# -7.498798913309295e-33
e**3*log(5)
#[Out]# 32.3264246157732
e**sqrt(2*pi)
#[Out]# 12.263511081611982
sqrt(3*pi/2)
#[Out]# 2.1708037636748028
e**(7*pi/3)
#[Out]# 1525.965888988749
8*(pi**50)
#[Out]# 5.762137555772631e+25
sqrt(40*pi**5+6*pi+e**(7*pi))
#[Out]# 59609.84432527889
x=-8.3, y=-4
x=-8.3; y=-4
abs(-8.3)
#[Out]# 8.3
abs(-4)
#[Out]# 4
#3.Calcula o valor absoluto
#4.Calcula o valor máis próximo, valor por exceso, valor por defecto e parte enteira de 
x=4.2; y=-3.7;z=-3.6+4.2j
round(x), round(y), round(z)
round(x), round(y)
#[Out]# (4, -4)
trunc(x), trunc(y), trunc(z)
trunc(x), trunc(y)
#[Out]# (4, -3)
ceil(x), floor(x), ceil(y), floor(y), ceil(z), floor(z)
ceil(x), floor(x), ceil(y), floor(y)
#[Out]# (5, 4, -3, -4)
#5.Define unha lista cos seguinte elementos e realiza as seguintes operacións:
lista1=[3,4,5,6,2,6,4,1,3,4]
len(lista)
len(lista1)
#[Out]# 10
type(lista1)
#[Out]# list
lista1[3]
#[Out]# 6
lista1[2]
#[Out]# 5
lista1[0],lista1[1],lista1[2],lista1[3]
#[Out]# (3, 4, 5, 6)
lista1[0:3]
#[Out]# [3, 4, 5]
lista1[10:7]
#[Out]# []
lista1[7:10]
#[Out]# [1, 3, 4]
max(lista1)
#[Out]# 6
min(lista1)
#[Out]# 1
sum(lista1)
#[Out]# 38
count(4)
import numpy
lista1.count(4)
#[Out]# 3
insert(5,20)
lista1.insert(5,20)
lista1
#[Out]# [3, 4, 5, 6, 2, 20, 6, 4, 1, 3, 4]
lista1[2:6]
#[Out]# [5, 6, 2, 20]
lista1[1,3,5]
lista1[1:3:5]
#[Out]# [4]
lista1[1:2:5]
#[Out]# [4]
[0:2:4]
lista1[0:2:4]
#[Out]# [3]
lista1.remove[3]
lista1[3].remove()
remove(lista1[3])
lista1.remove(lista1[3])
lista1.remove(lista1[4])
lista1.remove(lista1[5])
lista1.remove(lista1[6])
lista1.insert(1,30), lista1.insert(2,40)
#[Out]# (None, None)
lista1.insert(1,30); lista1.insert(2,40)
lista1.insert(0,15)
lista1.append(50)
lista1.insert(3,60)
lista1.reverse()
lista1.sort()
lista1.index(40)
#[Out]# 10
lista1.remove(lista1[10])
lista1
#[Out]# [1, 2, 3, 4, 4, 5, 6, 15, 30, 30, 40, 50, 60]
exit()
