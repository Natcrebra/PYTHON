# IPython log file

2+3 #suma 
#[Out]# 5
4-5 #resta
#[Out]# -1
4*5 #multiplicación
#[Out]# 20
8/3 #division
#[Out]# 2.6666666666666665
8/0
8//3 #division entera
#[Out]# 2
8%3 #calculo del resto
#[Out]# 2
6%4
#[Out]# 2
3**2 #potencias
#[Out]# 9
5-2*3
#[Out]# -1
5-2*3 #operaciones combinadas
#[Out]# -1
(5-2)*3 #operaciones combinadas con parentesis
#[Out]# 9
x= 5
7-x #ahora x=5 siempre
#[Out]# 2
print(x)
x=8 #cambio de valor de la variable
7+x
#[Out]# 15
y= 7+x
print(y)
z
type(y)  #te dice de que tipo es la variable
#[Out]# int
type(8)
#[Out]# int
s= 'ola a todas'
print(s)
type(s)
#[Out]# str
s
#[Out]# 'ola a todas'
len(s)
#[Out]# 11
len(s)  #te dice la longitud de la cadena
#[Out]# 11
s= 'pepe'
len(s)
#[Out]# 4
len(x)
x.bit_length
#[Out]# <function int.bit_length()>
x.bit_length()
#[Out]# 4
c= 4+2j #numeros complejos, en python j
type(c)
#[Out]# complex
c.imag
#[Out]# 2.0
b= True
type(b)
#[Out]# bool
c2= 3-4j
c+c2
#[Out]# (7-2j)
c,c2
#[Out]# ((4+2j), (3-4j))
c*c2
#[Out]# (20-10j)
5=x
a=5, b=False , c= 'ola'
a=5; b=False ;c= 'ola'
a=5,b=False,c= 'ola'
a,b,c=5,False,'ola'
a,b,c
#[Out]# (5, False, 'ola')
vars()
#[Out]# {'__name__': '__main__',
#[Out]#  '__doc__': 'Automatically created module for IPython interactive environment',
#[Out]#  '__package__': None,
#[Out]#  '__loader__': None,
#[Out]#  '__spec__': None,
#[Out]#  '__builtin__': <module 'builtins' (built-in)>,
#[Out]#  '__builtins__': <module 'builtins' (built-in)>,
#[Out]#  '_ih': ['',
#[Out]#   "get_ipython().run_line_magic('logstart', '-o sesion1.py')",
#[Out]#   '2+3 #suma ',
#[Out]#   '4-5 #resta',
#[Out]#   '4*5 #multiplicación',
#[Out]#   '8/3 #division',
#[Out]#   '8/0',
#[Out]#   '8//3 #division entera',
#[Out]#   '8%3 #calculo del resto',
#[Out]#   '6%4',
#[Out]#   '3**2 #potencias',
#[Out]#   '5-2*3',
#[Out]#   '5-2*3 #operaciones combinadas',
#[Out]#   '(5-2)*3 #operaciones combinadas con parentesis',
#[Out]#   'x= 5',
#[Out]#   '7-x #ahora x=5 siempre',
#[Out]#   'print(x)',
#[Out]#   'x=8 #cambio de valor de la variable',
#[Out]#   '7+x',
#[Out]#   'y= 7+x',
#[Out]#   'print(y)',
#[Out]#   'z',
#[Out]#   'type(y)  #te dice de que tipo es la variable',
#[Out]#   'type(8)',
#[Out]#   "s= 'ola a todas'",
#[Out]#   'print(s)',
#[Out]#   'type(s)',
#[Out]#   's',
#[Out]#   'len(s)',
#[Out]#   'len(s)  #te dice la longitud de la cadena',
#[Out]#   "s= 'pepe'",
#[Out]#   'len(s)',
#[Out]#   'len(x)',
#[Out]#   'x.bit_length',
#[Out]#   'x.bit_length()',
#[Out]#   'c= 4+2j #numeros complejos, en python j',
#[Out]#   'type(c)',
#[Out]#   'c.imag',
#[Out]#   'b= True',
#[Out]#   'type(b)',
#[Out]#   'c2= 3-4j',
#[Out]#   'c+c2',
#[Out]#   'c,c2',
#[Out]#   'c*c2',
#[Out]#   '5=x',
#[Out]#   "a=5, b=False , c= 'ola'",
#[Out]#   "a=5; b=False ;c= 'ola'",
#[Out]#   "a=5,b=False,c= 'ola'",
#[Out]#   "a,b,c=5,False,'ola'",
#[Out]#   'a,b,c',
#[Out]#   'vars()'],
#[Out]#  '_oh': {2: 5,
#[Out]#   3: -1,
#[Out]#   4: 20,
#[Out]#   5: 2.6666666666666665,
#[Out]#   7: 2,
#[Out]#   8: 2,
#[Out]#   9: 2,
#[Out]#   10: 9,
#[Out]#   11: -1,
#[Out]#   12: -1,
#[Out]#   13: 9,
#[Out]#   15: 2,
#[Out]#   18: 15,
#[Out]#   22: int,
#[Out]#   23: int,
#[Out]#   26: str,
#[Out]#   27: 'ola a todas',
#[Out]#   28: 11,
#[Out]#   29: 11,
#[Out]#   31: 4,
#[Out]#   33: <function int.bit_length()>,
#[Out]#   34: 4,
#[Out]#   36: complex,
#[Out]#   37: 2.0,
#[Out]#   39: bool,
#[Out]#   41: (7-2j),
#[Out]#   42: ((4+2j), (3-4j)),
#[Out]#   43: (20-10j),
#[Out]#   49: (5, False, 'ola')},
#[Out]#  '_dh': ['/home/RAI/natalia.crespo.bravo'],
#[Out]#  'In': ['',
#[Out]#   "get_ipython().run_line_magic('logstart', '-o sesion1.py')",
#[Out]#   '2+3 #suma ',
#[Out]#   '4-5 #resta',
#[Out]#   '4*5 #multiplicación',
#[Out]#   '8/3 #division',
#[Out]#   '8/0',
#[Out]#   '8//3 #division entera',
#[Out]#   '8%3 #calculo del resto',
#[Out]#   '6%4',
#[Out]#   '3**2 #potencias',
#[Out]#   '5-2*3',
#[Out]#   '5-2*3 #operaciones combinadas',
#[Out]#   '(5-2)*3 #operaciones combinadas con parentesis',
#[Out]#   'x= 5',
#[Out]#   '7-x #ahora x=5 siempre',
#[Out]#   'print(x)',
#[Out]#   'x=8 #cambio de valor de la variable',
#[Out]#   '7+x',
#[Out]#   'y= 7+x',
#[Out]#   'print(y)',
#[Out]#   'z',
#[Out]#   'type(y)  #te dice de que tipo es la variable',
#[Out]#   'type(8)',
#[Out]#   "s= 'ola a todas'",
#[Out]#   'print(s)',
#[Out]#   'type(s)',
#[Out]#   's',
#[Out]#   'len(s)',
#[Out]#   'len(s)  #te dice la longitud de la cadena',
#[Out]#   "s= 'pepe'",
#[Out]#   'len(s)',
#[Out]#   'len(x)',
#[Out]#   'x.bit_length',
#[Out]#   'x.bit_length()',
#[Out]#   'c= 4+2j #numeros complejos, en python j',
#[Out]#   'type(c)',
#[Out]#   'c.imag',
#[Out]#   'b= True',
#[Out]#   'type(b)',
#[Out]#   'c2= 3-4j',
#[Out]#   'c+c2',
#[Out]#   'c,c2',
#[Out]#   'c*c2',
#[Out]#   '5=x',
#[Out]#   "a=5, b=False , c= 'ola'",
#[Out]#   "a=5; b=False ;c= 'ola'",
#[Out]#   "a=5,b=False,c= 'ola'",
#[Out]#   "a,b,c=5,False,'ola'",
#[Out]#   'a,b,c',
#[Out]#   'vars()'],
#[Out]#  'Out': {2: 5,
#[Out]#   3: -1,
#[Out]#   4: 20,
#[Out]#   5: 2.6666666666666665,
#[Out]#   7: 2,
#[Out]#   8: 2,
#[Out]#   9: 2,
#[Out]#   10: 9,
#[Out]#   11: -1,
#[Out]#   12: -1,
#[Out]#   13: 9,
#[Out]#   15: 2,
#[Out]#   18: 15,
#[Out]#   22: int,
#[Out]#   23: int,
#[Out]#   26: str,
#[Out]#   27: 'ola a todas',
#[Out]#   28: 11,
#[Out]#   29: 11,
#[Out]#   31: 4,
#[Out]#   33: <function int.bit_length()>,
#[Out]#   34: 4,
#[Out]#   36: complex,
#[Out]#   37: 2.0,
#[Out]#   39: bool,
#[Out]#   41: (7-2j),
#[Out]#   42: ((4+2j), (3-4j)),
#[Out]#   43: (20-10j),
#[Out]#   49: (5, False, 'ola')},
#[Out]#  'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x7f5ddb6fba60>>,
#[Out]#  'exit': <IPython.core.autocall.ExitAutocall at 0x7f5ddb6fb7f0>,
#[Out]#  'quit': <IPython.core.autocall.ExitAutocall at 0x7f5ddb6fb7f0>,
#[Out]#  '_': (5, False, 'ola'),
#[Out]#  '__': (20-10j),
#[Out]#  '___': ((4+2j), (3-4j)),
#[Out]#  '_i': 'a,b,c',
#[Out]#  '_ii': "a,b,c=5,False,'ola'",
#[Out]#  '_iii': "a=5,b=False,c= 'ola'",
#[Out]#  '_i1': '%logstart -o sesion1.py',
#[Out]#  '_i2': '2+3 #suma ',
#[Out]#  '_2': 5,
#[Out]#  '_i3': '4-5 #resta',
#[Out]#  '_3': -1,
#[Out]#  '_i4': '4*5 #multiplicación',
#[Out]#  '_4': 20,
#[Out]#  '_i5': '8/3 #division',
#[Out]#  '_5': 2.6666666666666665,
#[Out]#  '_i6': '8/0',
#[Out]#  '_i7': '8//3 #division entera',
#[Out]#  '_7': 2,
#[Out]#  '_i8': '8%3 #calculo del resto',
#[Out]#  '_8': 2,
#[Out]#  '_i9': '6%4',
#[Out]#  '_9': 2,
#[Out]#  '_i10': '3**2 #potencias',
#[Out]#  '_10': 9,
#[Out]#  '_i11': '5-2*3',
#[Out]#  '_11': -1,
#[Out]#  '_i12': '5-2*3 #operaciones combinadas',
#[Out]#  '_12': -1,
#[Out]#  '_i13': '(5-2)*3 #operaciones combinadas con parentesis',
#[Out]#  '_13': 9,
#[Out]#  '_i14': 'x= 5',
#[Out]#  'x': 8,
#[Out]#  '_i15': '7-x #ahora x=5 siempre',
#[Out]#  '_15': 2,
#[Out]#  '_i16': 'print(x)',
#[Out]#  '_i17': 'x=8 #cambio de valor de la variable',
#[Out]#  '_i18': '7+x',
#[Out]#  '_18': 15,
#[Out]#  '_i19': 'y= 7+x',
#[Out]#  'y': 15,
#[Out]#  '_i20': 'print(y)',
#[Out]#  '_i21': 'z',
#[Out]#  '_i22': 'type(y)  #te dice de que tipo es la variable',
#[Out]#  '_22': int,
#[Out]#  '_i23': 'type(8)',
#[Out]#  '_23': int,
#[Out]#  '_i24': "s= 'ola a todas'",
#[Out]#  's': 'pepe',
#[Out]#  '_i25': 'print(s)',
#[Out]#  '_i26': 'type(s)',
#[Out]#  '_26': str,
#[Out]#  '_i27': 's',
#[Out]#  '_27': 'ola a todas',
#[Out]#  '_i28': 'len(s)',
#[Out]#  '_28': 11,
#[Out]#  '_i29': 'len(s)  #te dice la longitud de la cadena',
#[Out]#  '_29': 11,
#[Out]#  '_i30': "s= 'pepe'",
#[Out]#  '_i31': 'len(s)',
#[Out]#  '_31': 4,
#[Out]#  '_i32': 'len(x)',
#[Out]#  '_i33': 'x.bit_length',
#[Out]#  '_33': <function int.bit_length()>,
#[Out]#  '_i34': 'x.bit_length()',
#[Out]#  '_34': 4,
#[Out]#  '_i35': 'c= 4+2j #numeros complejos, en python j',
#[Out]#  'c': 'ola',
#[Out]#  '_i36': 'type(c)',
#[Out]#  '_36': complex,
#[Out]#  '_i37': 'c.imag',
#[Out]#  '_37': 2.0,
#[Out]#  '_i38': 'b= True',
#[Out]#  'b': False,
#[Out]#  '_i39': 'type(b)',
#[Out]#  '_39': bool,
#[Out]#  '_i40': 'c2= 3-4j',
#[Out]#  'c2': (3-4j),
#[Out]#  '_i41': 'c+c2',
#[Out]#  '_41': (7-2j),
#[Out]#  '_i42': 'c,c2',
#[Out]#  '_42': ((4+2j), (3-4j)),
#[Out]#  '_i43': 'c*c2',
#[Out]#  '_43': (20-10j),
#[Out]#  '_i44': '5=x',
#[Out]#  '_i45': "a=5, b=False , c= 'ola'",
#[Out]#  '_i46': "a=5; b=False ;c= 'ola'",
#[Out]#  'a': 5,
#[Out]#  '_i47': "a=5,b=False,c= 'ola'",
#[Out]#  '_i48': "a,b,c=5,False,'ola'",
#[Out]#  '_i49': 'a,b,c',
#[Out]#  '_49': (5, False, 'ola'),
#[Out]#  '_i50': 'vars()'}
'c' in vars()
#[Out]# True
abs(x)
#[Out]# 8
type(x)
#[Out]# int
x=3.4
abs(x)
#[Out]# 3.4
type(x)
#[Out]# float
c= 4-3j
abs(c)
#[Out]# 5.0
int(3.2)
#[Out]# 3
float(4)
#[Out]# 4.0
from math import *
pi
#[Out]# 3.141592653589793
e
#[Out]# 2.718281828459045
type(e)
#[Out]# float
sin(180)
#[Out]# -0.8011526357338304
sin(pi/4)
#[Out]# 0.7071067811865475
sinh(10)
#[Out]# 11013.232874703393
log(4)
#[Out]# 1.3862943611198906
ln(2)
exp(2)=
exp(2)
#[Out]# 7.38905609893065
e**2
#[Out]# 7.3890560989306495
x=5.7
int(X)
int(x)
#[Out]# 5
ceil(x)
#[Out]# 6
floor(x)
#[Out]# 5
round(x)
#[Out]# 6
ceil(x)
#[Out]# 6
from cmath import *
c= complex (-1,2)
c
#[Out]# (-1+2j)
type(c)
#[Out]# complex
c.real
#[Out]# -1.0
c.imag
#[Out]# 2.0
phase(c)
#[Out]# 2.0344439357957027
abs(c)
#[Out]# 2.23606797749979
c.conjugate()
#[Out]# (-1-2j)
get_ipython().run_line_magic('clear', '')
polar(c)
#[Out]# (2.23606797749979, 2.0344439357957027)
phase(c)
#[Out]# 2.0344439357957027
atan2(c.imag,c.real)
#[Out]# 2.0344439357957027
atan2(c.imag,c.real) #arcotangente parte imaginaria/parte real
#[Out]# 2.0344439357957027
atan2(c.imag/c.real) #arcotangente parte imaginaria/parte real
get_ipython().run_line_magic('pinfo', 'atan2')
c
#[Out]# (-1+2j)
polar(c)
#[Out]# (2.23606797749979, 2.0344439357957027)
rect(polar(c))
rect(abs(c),phase(c))
#[Out]# (-1+2j)
get_ipython().run_line_magic('clear', '')
x=[4,7.4,True,4+2j,'ola',[2,1]]
print(x)
x
#[Out]# [4, 7.4, True, (4+2j), 'ola', [2, 1]]
type(x)
#[Out]# list
x.[0]
x[0]
#[Out]# 4
x[-1] #para el ultimo elemento, asi no hay que contarlo
#[Out]# [2, 1]
x[1]
#[Out]# 7.4
x[6]
len(x)
#[Out]# 6
x[-2] #el penultimo elemento
#[Out]# 'ola'
x= [1,2,3,4,5,6,7,8,9]
max(x)
#[Out]# 9
min(x)
#[Out]# 1
sum(x)
#[Out]# 45
x[3]=20
x
#[Out]# [1, 2, 3, 20, 5, 6, 7, 8, 9]
x[3:5]
#[Out]# [20, 5]
x[3:5] #para acceder a varios elementos
#[Out]# [20, 5]
x[3:6] 
#[Out]# [20, 5, 6]
x[3:] #desde 3 hasta el final
#[Out]# [20, 5, 6, 7, 8, 9]
x[:6] #desde el principio hasta el 6
#[Out]# [1, 2, 3, 20, 5, 6]
x[:6] #desde el principio hasta el 5***
#[Out]# [1, 2, 3, 20, 5, 6]
get_ipython().run_line_magic('clear', '')
x[2:4]
#[Out]# [3, 20]
x[2:4]=[30,30]
x
#[Out]# [1, 2, 30, 30, 5, 6, 7, 8, 9]
x[2:4]=[30,30] #para cambiar los valores
get_ipython().run_line_magic('clear', '')
x[4:7]=[]
x
#[Out]# [1, 2, 30, 30, 8, 9]
x[4:7]=[] #para eliminar elementos
x[2] = []
x
#[Out]# [1, 2, [], 30]
range(6)
#[Out]# range(0, 6)
list(range(6))
#[Out]# [0, 1, 2, 3, 4, 5]
list(range(6)) #te saca una lista de rango 6
#[Out]# [0, 1, 2, 3, 4, 5]
list(range(1,6)) #si queremos que empiece en 1 y no 0
#[Out]# [1, 2, 3, 4, 5]
y=list(range(1,6)) #si queremos que empiece en 1 y no 0
sum(y)
#[Out]# 15
range(1,6,2)
#[Out]# range(1, 6, 2)
list(range(1,6,2))
#[Out]# [1, 3, 5]
list(range(1,6,2)) #la lista va de 2 en 2
#[Out]# [1, 3, 5]
get_ipython().run_line_magic('clear', '')
x
#[Out]# [1, 2, [], 30]
x[1:3] = [2,3]
x
#[Out]# [1, 2, 3, 30]
x[1:3] = [8,9,7]
x
#[Out]# [1, 8, 9, 7, 30]
x[1:3] = [8,9,7] #cambia la longitud de la lista
get_ipython().run_line_magic('clear', '')
x=[2,4,1,8,2]
x
#[Out]# [2, 4, 1, 8, 2]
len(x)
#[Out]# 5
1 in x
#[Out]# True
8 not in x
#[Out]# False
5 not in x
#[Out]# True
x
#[Out]# [2, 4, 1, 8, 2]
get_ipython().run_line_magic('clear', '')
c
#[Out]# (-1+2j)
x
#[Out]# [2, 4, 1, 8, 2]
x.append(5) #mete el 5 al final de la lista
x
#[Out]# [2, 4, 1, 8, 2, 5]
x.insert(3,10)
x
#[Out]# [2, 4, 1, 10, 8, 2, 5]
x.insert(3,10) #inserta un elemento en una posicion dada
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('pinfo', 'x.insert')
x.reverse()
x
#[Out]# [5, 2, 8, 10, 10, 1, 4, 2]
x.reverse() #les da la vuelta
x
#[Out]# [2, 4, 1, 10, 10, 8, 2, 5]
get_ipython().run_line_magic('clear', '')
x
#[Out]# [2, 4, 1, 10, 10, 8, 2, 5]
x[::-1] #tambien le da la vuelta a la lista
#[Out]# [5, 2, 8, 10, 10, 1, 4, 2]
x[::-1] #tambien le da la vuelta a la lista
#[Out]# [5, 2, 8, 10, 10, 1, 4, 2]
x.sort() #ordena
x
#[Out]# [1, 2, 2, 4, 5, 8, 10, 10]
x.sort(reverse=True)
x
#[Out]# [10, 10, 8, 5, 4, 2, 2, 1]
x.sort(reverse=True) #orden decreciente
get_ipython().run_line_magic('clear', '')
x.count(2) #cuenta cuantos elementos hay iguales a 2
#[Out]# 2
x.count(9)
#[Out]# 0
9 in x
#[Out]# False
get_ipython().run_line_magic('clear', '')
x.remove(8)
x
#[Out]# [10, 10, 5, 4, 2, 2, 1]
x.remove(10)
x
#[Out]# [10, 5, 4, 2, 2, 1]
get_ipython().run_line_magic('clear', '')
x.remove(2)
x
#[Out]# [10, 5, 4, 2, 1]
x.index(2)
#[Out]# 3
x.index(9)
x[2]=[]
x
#[Out]# [10, 5, [], 2, 1]
del x[2]
x
#[Out]# [10, 5, 2, 1]
get_ipython().run_line_magic('clear', '')
x=[3.5,3.1,8.4]
[int(i) for i in x] #sentencia for
#[Out]# [3, 3, 8]
[int(i) for i in x] #vectorizar 
#[Out]# [3, 3, 8]
[int(i) for i in x] #vectorizar. Aplica la funcion i para todos los elementos de la lista en una sola linea.
#[Out]# [3, 3, 8]
[i*i for i in x] 
#[Out]# [12.25, 9.610000000000001, 70.56]
vars()
#[Out]# {'__name__': '__main__',
#[Out]#  '__doc__': 'Automatically created module for IPython interactive environment',
#[Out]#  '__package__': None,
#[Out]#  '__loader__': None,
#[Out]#  '__spec__': None,
#[Out]#  '__builtin__': <module 'builtins' (built-in)>,
#[Out]#  '__builtins__': <module 'builtins' (built-in)>,
#[Out]#  '_ih': ['',
#[Out]#   "get_ipython().run_line_magic('logstart', '-o sesion1.py')",
#[Out]#   '2+3 #suma ',
#[Out]#   '4-5 #resta',
#[Out]#   '4*5 #multiplicación',
#[Out]#   '8/3 #division',
#[Out]#   '8/0',
#[Out]#   '8//3 #division entera',
#[Out]#   '8%3 #calculo del resto',
#[Out]#   '6%4',
#[Out]#   '3**2 #potencias',
#[Out]#   '5-2*3',
#[Out]#   '5-2*3 #operaciones combinadas',
#[Out]#   '(5-2)*3 #operaciones combinadas con parentesis',
#[Out]#   'x= 5',
#[Out]#   '7-x #ahora x=5 siempre',
#[Out]#   'print(x)',
#[Out]#   'x=8 #cambio de valor de la variable',
#[Out]#   '7+x',
#[Out]#   'y= 7+x',
#[Out]#   'print(y)',
#[Out]#   'z',
#[Out]#   'type(y)  #te dice de que tipo es la variable',
#[Out]#   'type(8)',
#[Out]#   "s= 'ola a todas'",
#[Out]#   'print(s)',
#[Out]#   'type(s)',
#[Out]#   's',
#[Out]#   'len(s)',
#[Out]#   'len(s)  #te dice la longitud de la cadena',
#[Out]#   "s= 'pepe'",
#[Out]#   'len(s)',
#[Out]#   'len(x)',
#[Out]#   'x.bit_length',
#[Out]#   'x.bit_length()',
#[Out]#   'c= 4+2j #numeros complejos, en python j',
#[Out]#   'type(c)',
#[Out]#   'c.imag',
#[Out]#   'b= True',
#[Out]#   'type(b)',
#[Out]#   'c2= 3-4j',
#[Out]#   'c+c2',
#[Out]#   'c,c2',
#[Out]#   'c*c2',
#[Out]#   '5=x',
#[Out]#   "a=5, b=False , c= 'ola'",
#[Out]#   "a=5; b=False ;c= 'ola'",
#[Out]#   "a=5,b=False,c= 'ola'",
#[Out]#   "a,b,c=5,False,'ola'",
#[Out]#   'a,b,c',
#[Out]#   'vars()',
#[Out]#   "'c' in vars()",
#[Out]#   'abs(x)',
#[Out]#   'type(x)',
#[Out]#   'x=3.4',
#[Out]#   'abs(x)',
#[Out]#   'type(x)',
#[Out]#   'c= 4-3j',
#[Out]#   'abs(c)',
#[Out]#   'int(3.2)',
#[Out]#   'float(4)',
#[Out]#   'from math import *',
#[Out]#   'pi',
#[Out]#   'e',
#[Out]#   'type(e)',
#[Out]#   'sin(180)',
#[Out]#   'sin(pi/4)',
#[Out]#   'sinh(10)',
#[Out]#   'log(4)',
#[Out]#   'ln(2)',
#[Out]#   'exp(2)=',
#[Out]#   'exp(2)',
#[Out]#   'e**2',
#[Out]#   'x=5.7',
#[Out]#   'int(X)',
#[Out]#   'int(x)',
#[Out]#   'ceil(x)',
#[Out]#   'floor(x)',
#[Out]#   'round(x)',
#[Out]#   'ceil(x)',
#[Out]#   'from cmath import *',
#[Out]#   'c= complex (-1,2)',
#[Out]#   'c',
#[Out]#   'type(c)',
#[Out]#   'c.real',
#[Out]#   'c.imag',
#[Out]#   'phase(c)',
#[Out]#   'abs(c)',
#[Out]#   'c.conjugate()',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'polar(c)',
#[Out]#   'phase(c)',
#[Out]#   'atan2(c.imag,c.real)',
#[Out]#   'atan2(c.imag,c.real) #arcotangente parte imaginaria/parte real',
#[Out]#   'atan2(c.imag/c.real) #arcotangente parte imaginaria/parte real',
#[Out]#   "get_ipython().run_line_magic('pinfo', 'atan2')",
#[Out]#   'c',
#[Out]#   'polar(c)',
#[Out]#   'rect(polar(c))',
#[Out]#   'rect(abs(c),phase(c))',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   "x=[4,7.4,True,4+2j,'ola',[2,1]]",
#[Out]#   'print(x)',
#[Out]#   'x',
#[Out]#   'type(x)',
#[Out]#   'x.[0]',
#[Out]#   'x[0]',
#[Out]#   'x[-1] #para el ultimo elemento, asi no hay que contarlo',
#[Out]#   'x[1]',
#[Out]#   'x[6]',
#[Out]#   'len(x)',
#[Out]#   'x[-2] #el penultimo elemento',
#[Out]#   'x= [1,2,3,4,5,6,7,8,9]',
#[Out]#   'max(x)',
#[Out]#   'min(x)',
#[Out]#   'sum(x)',
#[Out]#   'x[3]=20',
#[Out]#   'x',
#[Out]#   'x[3:5]',
#[Out]#   'x[3:5] #para acceder a varios elementos',
#[Out]#   'x[3:6] ',
#[Out]#   'x[3:] #desde 3 hasta el final',
#[Out]#   'x[:6] #desde el principio hasta el 6',
#[Out]#   'x[:6] #desde el principio hasta el 5***',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x[2:4]',
#[Out]#   'x[2:4]=[30,30]',
#[Out]#   'x',
#[Out]#   'x[2:4]=[30,30] #para cambiar los valores',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x[4:7]=[]',
#[Out]#   'x',
#[Out]#   'x[4:7]=[] #para eliminar elementos',
#[Out]#   'x[2] = []',
#[Out]#   'x',
#[Out]#   'range(6)',
#[Out]#   'list(range(6))',
#[Out]#   'list(range(6)) #te saca una lista de rango 6',
#[Out]#   'list(range(1,6)) #si queremos que empiece en 1 y no 0',
#[Out]#   'y=list(range(1,6)) #si queremos que empiece en 1 y no 0',
#[Out]#   'sum(y)',
#[Out]#   'range(1,6,2)',
#[Out]#   'list(range(1,6,2))',
#[Out]#   'list(range(1,6,2)) #la lista va de 2 en 2',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x',
#[Out]#   'x[1:3] = [2,3]',
#[Out]#   'x',
#[Out]#   'x[1:3] = [8,9,7]',
#[Out]#   'x',
#[Out]#   'x[1:3] = [8,9,7] #cambia la longitud de la lista',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x=[2,4,1,8,2]',
#[Out]#   'x',
#[Out]#   'len(x)',
#[Out]#   '1 in x',
#[Out]#   '8 not in x',
#[Out]#   '5 not in x',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'c',
#[Out]#   'x',
#[Out]#   'x.append(5) #mete el 5 al final de la lista',
#[Out]#   'x',
#[Out]#   'x.insert(3,10)',
#[Out]#   'x',
#[Out]#   'x.insert(3,10) #inserta un elemento en una posicion dada',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   "get_ipython().run_line_magic('pinfo', 'x.insert')",
#[Out]#   'x.reverse()',
#[Out]#   'x',
#[Out]#   'x.reverse() #les da la vuelta',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x',
#[Out]#   'x[::-1] #tambien le da la vuelta a la lista',
#[Out]#   'x[::-1] #tambien le da la vuelta a la lista',
#[Out]#   'x.sort() #ordena',
#[Out]#   'x',
#[Out]#   'x.sort(reverse=True)',
#[Out]#   'x',
#[Out]#   'x.sort(reverse=True) #orden decreciente',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x.count(2) #cuenta cuantos elementos hay iguales a 2',
#[Out]#   'x.count(9)',
#[Out]#   '9 in x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x.remove(8)',
#[Out]#   'x',
#[Out]#   'x.remove(10)',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x.remove(2)',
#[Out]#   'x',
#[Out]#   'x.index(2)',
#[Out]#   'x.index(9)',
#[Out]#   'x[2]=[]',
#[Out]#   'x',
#[Out]#   'del x[2]',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x=[3.5,3.1,8.4]',
#[Out]#   '[int(i) for i in x] #sentencia for',
#[Out]#   '[int(i) for i in x] #vectorizar ',
#[Out]#   '[int(i) for i in x] #vectorizar. Aplica la funcion i para todos los elementos de la lista en una sola linea.',
#[Out]#   '[i*i for i in x] ',
#[Out]#   'vars()'],
#[Out]#  '_oh': {2: 5,
#[Out]#   3: -1,
#[Out]#   4: 20,
#[Out]#   5: 2.6666666666666665,
#[Out]#   7: 2,
#[Out]#   8: 2,
#[Out]#   9: 2,
#[Out]#   10: 9,
#[Out]#   11: -1,
#[Out]#   12: -1,
#[Out]#   13: 9,
#[Out]#   15: 2,
#[Out]#   18: 15,
#[Out]#   22: int,
#[Out]#   23: int,
#[Out]#   26: str,
#[Out]#   27: 'ola a todas',
#[Out]#   28: 11,
#[Out]#   29: 11,
#[Out]#   31: 4,
#[Out]#   33: <function int.bit_length()>,
#[Out]#   34: 4,
#[Out]#   36: complex,
#[Out]#   37: 2.0,
#[Out]#   39: bool,
#[Out]#   41: (7-2j),
#[Out]#   42: ((4+2j), (3-4j)),
#[Out]#   43: (20-10j),
#[Out]#   49: (5, False, 'ola'),
#[Out]#   50: {...},
#[Out]#   51: True,
#[Out]#   52: 8,
#[Out]#   53: int,
#[Out]#   55: 3.4,
#[Out]#   56: float,
#[Out]#   58: 5.0,
#[Out]#   59: 3,
#[Out]#   60: 4.0,
#[Out]#   62: 3.141592653589793,
#[Out]#   63: 2.718281828459045,
#[Out]#   64: float,
#[Out]#   65: -0.8011526357338304,
#[Out]#   66: 0.7071067811865475,
#[Out]#   67: 11013.232874703393,
#[Out]#   68: 1.3862943611198906,
#[Out]#   71: 7.38905609893065,
#[Out]#   72: 7.3890560989306495,
#[Out]#   75: 5,
#[Out]#   76: 6,
#[Out]#   77: 5,
#[Out]#   78: 6,
#[Out]#   79: 6,
#[Out]#   82: (-1+2j),
#[Out]#   83: complex,
#[Out]#   84: -1.0,
#[Out]#   85: 2.0,
#[Out]#   86: 2.0344439357957027,
#[Out]#   87: 2.23606797749979,
#[Out]#   88: (-1-2j),
#[Out]#   90: (2.23606797749979, 2.0344439357957027),
#[Out]#   91: 2.0344439357957027,
#[Out]#   92: 2.0344439357957027,
#[Out]#   93: 2.0344439357957027,
#[Out]#   96: (-1+2j),
#[Out]#   97: (2.23606797749979, 2.0344439357957027),
#[Out]#   99: (-1+2j),
#[Out]#   103: [4, 7.4, True, (4+2j), 'ola', [2, 1]],
#[Out]#   104: list,
#[Out]#   106: 4,
#[Out]#   107: [2, 1],
#[Out]#   108: 7.4,
#[Out]#   110: 6,
#[Out]#   111: 'ola',
#[Out]#   113: 9,
#[Out]#   114: 1,
#[Out]#   115: 45,
#[Out]#   117: [1, 8, 9, 7, 7, 30],
#[Out]#   118: [20, 5],
#[Out]#   119: [20, 5],
#[Out]#   120: [20, 5, 6],
#[Out]#   121: [20, 5, 6, 7, 8, 9],
#[Out]#   122: [1, 2, 3, 20, 5, 6],
#[Out]#   123: [1, 2, 3, 20, 5, 6],
#[Out]#   125: [3, 20],
#[Out]#   127: [1, 8, 9, 7, 7, 30],
#[Out]#   131: [1, 8, 9, 7, 7, 30],
#[Out]#   134: [1, 8, 9, 7, 7, 30],
#[Out]#   135: range(0, 6),
#[Out]#   136: [0, 1, 2, 3, 4, 5],
#[Out]#   137: [0, 1, 2, 3, 4, 5],
#[Out]#   138: [1, 2, 3, 4, 5],
#[Out]#   140: 15,
#[Out]#   141: range(1, 6, 2),
#[Out]#   142: [1, 3, 5],
#[Out]#   143: [1, 3, 5],
#[Out]#   145: [1, 8, 9, 7, 7, 30],
#[Out]#   147: [1, 8, 9, 7, 7, 30],
#[Out]#   149: [1, 8, 9, 7, 7, 30],
#[Out]#   153: [10, 5, 2, 1],
#[Out]#   154: 5,
#[Out]#   155: True,
#[Out]#   156: False,
#[Out]#   157: True,
#[Out]#   158: [10, 5, 2, 1],
#[Out]#   160: (-1+2j),
#[Out]#   161: [10, 5, 2, 1],
#[Out]#   163: [10, 5, 2, 1],
#[Out]#   165: [10, 5, 2, 1],
#[Out]#   170: [10, 5, 2, 1],
#[Out]#   172: [10, 5, 2, 1],
#[Out]#   174: [10, 5, 2, 1],
#[Out]#   175: [5, 2, 8, 10, 10, 1, 4, 2],
#[Out]#   176: [5, 2, 8, 10, 10, 1, 4, 2],
#[Out]#   178: [10, 5, 2, 1],
#[Out]#   180: [10, 5, 2, 1],
#[Out]#   183: 2,
#[Out]#   184: 0,
#[Out]#   185: False,
#[Out]#   188: [10, 5, 2, 1],
#[Out]#   190: [10, 5, 2, 1],
#[Out]#   193: [10, 5, 2, 1],
#[Out]#   194: 3,
#[Out]#   197: [10, 5, 2, 1],
#[Out]#   199: [10, 5, 2, 1],
#[Out]#   202: [3, 3, 8],
#[Out]#   203: [3, 3, 8],
#[Out]#   204: [3, 3, 8],
#[Out]#   205: [12.25, 9.610000000000001, 70.56]},
#[Out]#  '_dh': ['/home/RAI/natalia.crespo.bravo'],
#[Out]#  'In': ['',
#[Out]#   "get_ipython().run_line_magic('logstart', '-o sesion1.py')",
#[Out]#   '2+3 #suma ',
#[Out]#   '4-5 #resta',
#[Out]#   '4*5 #multiplicación',
#[Out]#   '8/3 #division',
#[Out]#   '8/0',
#[Out]#   '8//3 #division entera',
#[Out]#   '8%3 #calculo del resto',
#[Out]#   '6%4',
#[Out]#   '3**2 #potencias',
#[Out]#   '5-2*3',
#[Out]#   '5-2*3 #operaciones combinadas',
#[Out]#   '(5-2)*3 #operaciones combinadas con parentesis',
#[Out]#   'x= 5',
#[Out]#   '7-x #ahora x=5 siempre',
#[Out]#   'print(x)',
#[Out]#   'x=8 #cambio de valor de la variable',
#[Out]#   '7+x',
#[Out]#   'y= 7+x',
#[Out]#   'print(y)',
#[Out]#   'z',
#[Out]#   'type(y)  #te dice de que tipo es la variable',
#[Out]#   'type(8)',
#[Out]#   "s= 'ola a todas'",
#[Out]#   'print(s)',
#[Out]#   'type(s)',
#[Out]#   's',
#[Out]#   'len(s)',
#[Out]#   'len(s)  #te dice la longitud de la cadena',
#[Out]#   "s= 'pepe'",
#[Out]#   'len(s)',
#[Out]#   'len(x)',
#[Out]#   'x.bit_length',
#[Out]#   'x.bit_length()',
#[Out]#   'c= 4+2j #numeros complejos, en python j',
#[Out]#   'type(c)',
#[Out]#   'c.imag',
#[Out]#   'b= True',
#[Out]#   'type(b)',
#[Out]#   'c2= 3-4j',
#[Out]#   'c+c2',
#[Out]#   'c,c2',
#[Out]#   'c*c2',
#[Out]#   '5=x',
#[Out]#   "a=5, b=False , c= 'ola'",
#[Out]#   "a=5; b=False ;c= 'ola'",
#[Out]#   "a=5,b=False,c= 'ola'",
#[Out]#   "a,b,c=5,False,'ola'",
#[Out]#   'a,b,c',
#[Out]#   'vars()',
#[Out]#   "'c' in vars()",
#[Out]#   'abs(x)',
#[Out]#   'type(x)',
#[Out]#   'x=3.4',
#[Out]#   'abs(x)',
#[Out]#   'type(x)',
#[Out]#   'c= 4-3j',
#[Out]#   'abs(c)',
#[Out]#   'int(3.2)',
#[Out]#   'float(4)',
#[Out]#   'from math import *',
#[Out]#   'pi',
#[Out]#   'e',
#[Out]#   'type(e)',
#[Out]#   'sin(180)',
#[Out]#   'sin(pi/4)',
#[Out]#   'sinh(10)',
#[Out]#   'log(4)',
#[Out]#   'ln(2)',
#[Out]#   'exp(2)=',
#[Out]#   'exp(2)',
#[Out]#   'e**2',
#[Out]#   'x=5.7',
#[Out]#   'int(X)',
#[Out]#   'int(x)',
#[Out]#   'ceil(x)',
#[Out]#   'floor(x)',
#[Out]#   'round(x)',
#[Out]#   'ceil(x)',
#[Out]#   'from cmath import *',
#[Out]#   'c= complex (-1,2)',
#[Out]#   'c',
#[Out]#   'type(c)',
#[Out]#   'c.real',
#[Out]#   'c.imag',
#[Out]#   'phase(c)',
#[Out]#   'abs(c)',
#[Out]#   'c.conjugate()',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'polar(c)',
#[Out]#   'phase(c)',
#[Out]#   'atan2(c.imag,c.real)',
#[Out]#   'atan2(c.imag,c.real) #arcotangente parte imaginaria/parte real',
#[Out]#   'atan2(c.imag/c.real) #arcotangente parte imaginaria/parte real',
#[Out]#   "get_ipython().run_line_magic('pinfo', 'atan2')",
#[Out]#   'c',
#[Out]#   'polar(c)',
#[Out]#   'rect(polar(c))',
#[Out]#   'rect(abs(c),phase(c))',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   "x=[4,7.4,True,4+2j,'ola',[2,1]]",
#[Out]#   'print(x)',
#[Out]#   'x',
#[Out]#   'type(x)',
#[Out]#   'x.[0]',
#[Out]#   'x[0]',
#[Out]#   'x[-1] #para el ultimo elemento, asi no hay que contarlo',
#[Out]#   'x[1]',
#[Out]#   'x[6]',
#[Out]#   'len(x)',
#[Out]#   'x[-2] #el penultimo elemento',
#[Out]#   'x= [1,2,3,4,5,6,7,8,9]',
#[Out]#   'max(x)',
#[Out]#   'min(x)',
#[Out]#   'sum(x)',
#[Out]#   'x[3]=20',
#[Out]#   'x',
#[Out]#   'x[3:5]',
#[Out]#   'x[3:5] #para acceder a varios elementos',
#[Out]#   'x[3:6] ',
#[Out]#   'x[3:] #desde 3 hasta el final',
#[Out]#   'x[:6] #desde el principio hasta el 6',
#[Out]#   'x[:6] #desde el principio hasta el 5***',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x[2:4]',
#[Out]#   'x[2:4]=[30,30]',
#[Out]#   'x',
#[Out]#   'x[2:4]=[30,30] #para cambiar los valores',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x[4:7]=[]',
#[Out]#   'x',
#[Out]#   'x[4:7]=[] #para eliminar elementos',
#[Out]#   'x[2] = []',
#[Out]#   'x',
#[Out]#   'range(6)',
#[Out]#   'list(range(6))',
#[Out]#   'list(range(6)) #te saca una lista de rango 6',
#[Out]#   'list(range(1,6)) #si queremos que empiece en 1 y no 0',
#[Out]#   'y=list(range(1,6)) #si queremos que empiece en 1 y no 0',
#[Out]#   'sum(y)',
#[Out]#   'range(1,6,2)',
#[Out]#   'list(range(1,6,2))',
#[Out]#   'list(range(1,6,2)) #la lista va de 2 en 2',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x',
#[Out]#   'x[1:3] = [2,3]',
#[Out]#   'x',
#[Out]#   'x[1:3] = [8,9,7]',
#[Out]#   'x',
#[Out]#   'x[1:3] = [8,9,7] #cambia la longitud de la lista',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x=[2,4,1,8,2]',
#[Out]#   'x',
#[Out]#   'len(x)',
#[Out]#   '1 in x',
#[Out]#   '8 not in x',
#[Out]#   '5 not in x',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'c',
#[Out]#   'x',
#[Out]#   'x.append(5) #mete el 5 al final de la lista',
#[Out]#   'x',
#[Out]#   'x.insert(3,10)',
#[Out]#   'x',
#[Out]#   'x.insert(3,10) #inserta un elemento en una posicion dada',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   "get_ipython().run_line_magic('pinfo', 'x.insert')",
#[Out]#   'x.reverse()',
#[Out]#   'x',
#[Out]#   'x.reverse() #les da la vuelta',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x',
#[Out]#   'x[::-1] #tambien le da la vuelta a la lista',
#[Out]#   'x[::-1] #tambien le da la vuelta a la lista',
#[Out]#   'x.sort() #ordena',
#[Out]#   'x',
#[Out]#   'x.sort(reverse=True)',
#[Out]#   'x',
#[Out]#   'x.sort(reverse=True) #orden decreciente',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x.count(2) #cuenta cuantos elementos hay iguales a 2',
#[Out]#   'x.count(9)',
#[Out]#   '9 in x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x.remove(8)',
#[Out]#   'x',
#[Out]#   'x.remove(10)',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x.remove(2)',
#[Out]#   'x',
#[Out]#   'x.index(2)',
#[Out]#   'x.index(9)',
#[Out]#   'x[2]=[]',
#[Out]#   'x',
#[Out]#   'del x[2]',
#[Out]#   'x',
#[Out]#   "get_ipython().run_line_magic('clear', '')",
#[Out]#   'x=[3.5,3.1,8.4]',
#[Out]#   '[int(i) for i in x] #sentencia for',
#[Out]#   '[int(i) for i in x] #vectorizar ',
#[Out]#   '[int(i) for i in x] #vectorizar. Aplica la funcion i para todos los elementos de la lista en una sola linea.',
#[Out]#   '[i*i for i in x] ',
#[Out]#   'vars()'],
#[Out]#  'Out': {2: 5,
#[Out]#   3: -1,
#[Out]#   4: 20,
#[Out]#   5: 2.6666666666666665,
#[Out]#   7: 2,
#[Out]#   8: 2,
#[Out]#   9: 2,
#[Out]#   10: 9,
#[Out]#   11: -1,
#[Out]#   12: -1,
#[Out]#   13: 9,
#[Out]#   15: 2,
#[Out]#   18: 15,
#[Out]#   22: int,
#[Out]#   23: int,
#[Out]#   26: str,
#[Out]#   27: 'ola a todas',
#[Out]#   28: 11,
#[Out]#   29: 11,
#[Out]#   31: 4,
#[Out]#   33: <function int.bit_length()>,
#[Out]#   34: 4,
#[Out]#   36: complex,
#[Out]#   37: 2.0,
#[Out]#   39: bool,
#[Out]#   41: (7-2j),
#[Out]#   42: ((4+2j), (3-4j)),
#[Out]#   43: (20-10j),
#[Out]#   49: (5, False, 'ola'),
#[Out]#   50: {...},
#[Out]#   51: True,
#[Out]#   52: 8,
#[Out]#   53: int,
#[Out]#   55: 3.4,
#[Out]#   56: float,
#[Out]#   58: 5.0,
#[Out]#   59: 3,
#[Out]#   60: 4.0,
#[Out]#   62: 3.141592653589793,
#[Out]#   63: 2.718281828459045,
#[Out]#   64: float,
#[Out]#   65: -0.8011526357338304,
#[Out]#   66: 0.7071067811865475,
#[Out]#   67: 11013.232874703393,
#[Out]#   68: 1.3862943611198906,
#[Out]#   71: 7.38905609893065,
#[Out]#   72: 7.3890560989306495,
#[Out]#   75: 5,
#[Out]#   76: 6,
#[Out]#   77: 5,
#[Out]#   78: 6,
#[Out]#   79: 6,
#[Out]#   82: (-1+2j),
#[Out]#   83: complex,
#[Out]#   84: -1.0,
#[Out]#   85: 2.0,
#[Out]#   86: 2.0344439357957027,
#[Out]#   87: 2.23606797749979,
#[Out]#   88: (-1-2j),
#[Out]#   90: (2.23606797749979, 2.0344439357957027),
#[Out]#   91: 2.0344439357957027,
#[Out]#   92: 2.0344439357957027,
#[Out]#   93: 2.0344439357957027,
#[Out]#   96: (-1+2j),
#[Out]#   97: (2.23606797749979, 2.0344439357957027),
#[Out]#   99: (-1+2j),
#[Out]#   103: [4, 7.4, True, (4+2j), 'ola', [2, 1]],
#[Out]#   104: list,
#[Out]#   106: 4,
#[Out]#   107: [2, 1],
#[Out]#   108: 7.4,
#[Out]#   110: 6,
#[Out]#   111: 'ola',
#[Out]#   113: 9,
#[Out]#   114: 1,
#[Out]#   115: 45,
#[Out]#   117: [1, 8, 9, 7, 7, 30],
#[Out]#   118: [20, 5],
#[Out]#   119: [20, 5],
#[Out]#   120: [20, 5, 6],
#[Out]#   121: [20, 5, 6, 7, 8, 9],
#[Out]#   122: [1, 2, 3, 20, 5, 6],
#[Out]#   123: [1, 2, 3, 20, 5, 6],
#[Out]#   125: [3, 20],
#[Out]#   127: [1, 8, 9, 7, 7, 30],
#[Out]#   131: [1, 8, 9, 7, 7, 30],
#[Out]#   134: [1, 8, 9, 7, 7, 30],
#[Out]#   135: range(0, 6),
#[Out]#   136: [0, 1, 2, 3, 4, 5],
#[Out]#   137: [0, 1, 2, 3, 4, 5],
#[Out]#   138: [1, 2, 3, 4, 5],
#[Out]#   140: 15,
#[Out]#   141: range(1, 6, 2),
#[Out]#   142: [1, 3, 5],
#[Out]#   143: [1, 3, 5],
#[Out]#   145: [1, 8, 9, 7, 7, 30],
#[Out]#   147: [1, 8, 9, 7, 7, 30],
#[Out]#   149: [1, 8, 9, 7, 7, 30],
#[Out]#   153: [10, 5, 2, 1],
#[Out]#   154: 5,
#[Out]#   155: True,
#[Out]#   156: False,
#[Out]#   157: True,
#[Out]#   158: [10, 5, 2, 1],
#[Out]#   160: (-1+2j),
#[Out]#   161: [10, 5, 2, 1],
#[Out]#   163: [10, 5, 2, 1],
#[Out]#   165: [10, 5, 2, 1],
#[Out]#   170: [10, 5, 2, 1],
#[Out]#   172: [10, 5, 2, 1],
#[Out]#   174: [10, 5, 2, 1],
#[Out]#   175: [5, 2, 8, 10, 10, 1, 4, 2],
#[Out]#   176: [5, 2, 8, 10, 10, 1, 4, 2],
#[Out]#   178: [10, 5, 2, 1],
#[Out]#   180: [10, 5, 2, 1],
#[Out]#   183: 2,
#[Out]#   184: 0,
#[Out]#   185: False,
#[Out]#   188: [10, 5, 2, 1],
#[Out]#   190: [10, 5, 2, 1],
#[Out]#   193: [10, 5, 2, 1],
#[Out]#   194: 3,
#[Out]#   197: [10, 5, 2, 1],
#[Out]#   199: [10, 5, 2, 1],
#[Out]#   202: [3, 3, 8],
#[Out]#   203: [3, 3, 8],
#[Out]#   204: [3, 3, 8],
#[Out]#   205: [12.25, 9.610000000000001, 70.56]},
#[Out]#  'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x7f5ddb6fba60>>,
#[Out]#  'exit': <IPython.core.autocall.ExitAutocall at 0x7f5ddb6fb7f0>,
#[Out]#  'quit': <IPython.core.autocall.ExitAutocall at 0x7f5ddb6fb7f0>,
#[Out]#  '_': [12.25, 9.610000000000001, 70.56],
#[Out]#  '__': [3, 3, 8],
#[Out]#  '___': [3, 3, 8],
#[Out]#  '_i': '[i*i for i in x] ',
#[Out]#  '_ii': '[int(i) for i in x] #vectorizar. Aplica la funcion i para todos los elementos de la lista en una sola linea.',
#[Out]#  '_iii': '[int(i) for i in x] #vectorizar ',
#[Out]#  '_i1': '%logstart -o sesion1.py',
#[Out]#  '_i2': '2+3 #suma ',
#[Out]#  '_2': 5,
#[Out]#  '_i3': '4-5 #resta',
#[Out]#  '_3': -1,
#[Out]#  '_i4': '4*5 #multiplicación',
#[Out]#  '_4': 20,
#[Out]#  '_i5': '8/3 #division',
#[Out]#  '_5': 2.6666666666666665,
#[Out]#  '_i6': '8/0',
#[Out]#  '_i7': '8//3 #division entera',
#[Out]#  '_7': 2,
#[Out]#  '_i8': '8%3 #calculo del resto',
#[Out]#  '_8': 2,
#[Out]#  '_i9': '6%4',
#[Out]#  '_9': 2,
#[Out]#  '_i10': '3**2 #potencias',
#[Out]#  '_10': 9,
#[Out]#  '_i11': '5-2*3',
#[Out]#  '_11': -1,
#[Out]#  '_i12': '5-2*3 #operaciones combinadas',
#[Out]#  '_12': -1,
#[Out]#  '_i13': '(5-2)*3 #operaciones combinadas con parentesis',
#[Out]#  '_13': 9,
#[Out]#  '_i14': 'x= 5',
#[Out]#  'x': [3.5, 3.1, 8.4],
#[Out]#  '_i15': '7-x #ahora x=5 siempre',
#[Out]#  '_15': 2,
#[Out]#  '_i16': 'print(x)',
#[Out]#  '_i17': 'x=8 #cambio de valor de la variable',
#[Out]#  '_i18': '7+x',
#[Out]#  '_18': 15,
#[Out]#  '_i19': 'y= 7+x',
#[Out]#  'y': [1, 2, 3, 4, 5],
#[Out]#  '_i20': 'print(y)',
#[Out]#  '_i21': 'z',
#[Out]#  '_i22': 'type(y)  #te dice de que tipo es la variable',
#[Out]#  '_22': int,
#[Out]#  '_i23': 'type(8)',
#[Out]#  '_23': int,
#[Out]#  '_i24': "s= 'ola a todas'",
#[Out]#  's': 'pepe',
#[Out]#  '_i25': 'print(s)',
#[Out]#  '_i26': 'type(s)',
#[Out]#  '_26': str,
#[Out]#  '_i27': 's',
#[Out]#  '_27': 'ola a todas',
#[Out]#  '_i28': 'len(s)',
#[Out]#  '_28': 11,
#[Out]#  '_i29': 'len(s)  #te dice la longitud de la cadena',
#[Out]#  '_29': 11,
#[Out]#  '_i30': "s= 'pepe'",
#[Out]#  '_i31': 'len(s)',
#[Out]#  '_31': 4,
#[Out]#  '_i32': 'len(x)',
#[Out]#  '_i33': 'x.bit_length',
#[Out]#  '_33': <function int.bit_length()>,
#[Out]#  '_i34': 'x.bit_length()',
#[Out]#  '_34': 4,
#[Out]#  '_i35': 'c= 4+2j #numeros complejos, en python j',
#[Out]#  'c': (-1+2j),
#[Out]#  '_i36': 'type(c)',
#[Out]#  '_36': complex,
#[Out]#  '_i37': 'c.imag',
#[Out]#  '_37': 2.0,
#[Out]#  '_i38': 'b= True',
#[Out]#  'b': False,
#[Out]#  '_i39': 'type(b)',
#[Out]#  '_39': bool,
#[Out]#  '_i40': 'c2= 3-4j',
#[Out]#  'c2': (3-4j),
#[Out]#  '_i41': 'c+c2',
#[Out]#  '_41': (7-2j),
#[Out]#  '_i42': 'c,c2',
#[Out]#  '_42': ((4+2j), (3-4j)),
#[Out]#  '_i43': 'c*c2',
#[Out]#  '_43': (20-10j),
#[Out]#  '_i44': '5=x',
#[Out]#  '_i45': "a=5, b=False , c= 'ola'",
#[Out]#  '_i46': "a=5; b=False ;c= 'ola'",
#[Out]#  'a': 5,
#[Out]#  '_i47': "a=5,b=False,c= 'ola'",
#[Out]#  '_i48': "a,b,c=5,False,'ola'",
#[Out]#  '_i49': 'a,b,c',
#[Out]#  '_49': (5, False, 'ola'),
#[Out]#  '_i50': 'vars()',
#[Out]#  '_50': {...},
#[Out]#  '_i51': "'c' in vars()",
#[Out]#  '_51': True,
#[Out]#  '_i52': 'abs(x)',
#[Out]#  '_52': 8,
#[Out]#  '_i53': 'type(x)',
#[Out]#  '_53': int,
#[Out]#  '_i54': 'x=3.4',
#[Out]#  '_i55': 'abs(x)',
#[Out]#  '_55': 3.4,
#[Out]#  '_i56': 'type(x)',
#[Out]#  '_56': float,
#[Out]#  '_i57': 'c= 4-3j',
#[Out]#  '_i58': 'abs(c)',
#[Out]#  '_58': 5.0,
#[Out]#  '_i59': 'int(3.2)',
#[Out]#  '_59': 3,
#[Out]#  '_i60': 'float(4)',
#[Out]#  '_60': 4.0,
#[Out]#  '_i61': 'from math import *',
#[Out]#  'acos': <function cmath.acos(z, /)>,
#[Out]#  'acosh': <function cmath.acosh(z, /)>,
#[Out]#  'asin': <function cmath.asin(z, /)>,
#[Out]#  'asinh': <function cmath.asinh(z, /)>,
#[Out]#  'atan': <function cmath.atan(z, /)>,
#[Out]#  'atan2': <function math.atan2(y, x, /)>,
#[Out]#  'atanh': <function cmath.atanh(z, /)>,
#[Out]#  'ceil': <function math.ceil(x, /)>,
#[Out]#  'copysign': <function math.copysign(x, y, /)>,
#[Out]#  'cos': <function cmath.cos(z, /)>,
#[Out]#  'cosh': <function cmath.cosh(z, /)>,
#[Out]#  'degrees': <function math.degrees(x, /)>,
#[Out]#  'dist': <function math.dist(p, q, /)>,
#[Out]#  'erf': <function math.erf(x, /)>,
#[Out]#  'erfc': <function math.erfc(x, /)>,
#[Out]#  'exp': <function cmath.exp(z, /)>,
#[Out]#  'expm1': <function math.expm1(x, /)>,
#[Out]#  'fabs': <function math.fabs(x, /)>,
#[Out]#  'factorial': <function math.factorial(x, /)>,
#[Out]#  'floor': <function math.floor(x, /)>,
#[Out]#  'fmod': <function math.fmod(x, y, /)>,
#[Out]#  'frexp': <function math.frexp(x, /)>,
#[Out]#  'fsum': <function math.fsum(seq, /)>,
#[Out]#  'gamma': <function math.gamma(x, /)>,
#[Out]#  'gcd': <function math.gcd(x, y, /)>,
#[Out]#  'hypot': <function math.hypot>,
#[Out]#  'isclose': <function cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)>,
#[Out]#  'isfinite': <function cmath.isfinite(z, /)>,
#[Out]#  'isinf': <function cmath.isinf(z, /)>,
#[Out]#  'isnan': <function cmath.isnan(z, /)>,
#[Out]#  'isqrt': <function math.isqrt(n, /)>,
#[Out]#  'ldexp': <function math.ldexp(x, i, /)>,
#[Out]#  'lgamma': <function math.lgamma(x, /)>,
#[Out]#  'log': <function cmath.log>,
#[Out]#  'log1p': <function math.log1p(x, /)>,
#[Out]#  'log10': <function cmath.log10(z, /)>,
#[Out]#  'log2': <function math.log2(x, /)>,
#[Out]#  'modf': <function math.modf(x, /)>,
#[Out]#  'pow': <function math.pow(x, y, /)>,
#[Out]#  'radians': <function math.radians(x, /)>,
#[Out]#  'remainder': <function math.remainder(x, y, /)>,
#[Out]#  'sin': <function cmath.sin(z, /)>,
#[Out]#  'sinh': <function cmath.sinh(z, /)>,
#[Out]#  'sqrt': <function cmath.sqrt(z, /)>,
#[Out]#  'tan': <function cmath.tan(z, /)>,
#[Out]#  'tanh': <function cmath.tanh(z, /)>,
#[Out]#  'trunc': <function math.trunc(x, /)>,
#[Out]#  'prod': <function math.prod(iterable, /, *, start=1)>,
#[Out]#  'perm': <function math.perm(n, k=None, /)>,
#[Out]#  'comb': <function math.comb(n, k, /)>,
#[Out]#  'pi': 3.141592653589793,
#[Out]#  'e': 2.718281828459045,
#[Out]#  'tau': 6.283185307179586,
#[Out]#  'inf': inf,
#[Out]#  'nan': nan,
#[Out]#  '_i62': 'pi',
#[Out]#  '_62': 3.141592653589793,
#[Out]#  '_i63': 'e',
#[Out]#  '_63': 2.718281828459045,
#[Out]#  '_i64': 'type(e)',
#[Out]#  '_64': float,
#[Out]#  '_i65': 'sin(180)',
#[Out]#  '_65': -0.8011526357338304,
#[Out]#  '_i66': 'sin(pi/4)',
#[Out]#  '_66': 0.7071067811865475,
#[Out]#  '_i67': 'sinh(10)',
#[Out]#  '_67': 11013.232874703393,
#[Out]#  '_i68': 'log(4)',
#[Out]#  '_68': 1.3862943611198906,
#[Out]#  '_i69': 'ln(2)',
#[Out]#  '_i70': 'exp(2)=',
#[Out]#  '_i71': 'exp(2)',
#[Out]#  '_71': 7.38905609893065,
#[Out]#  '_i72': 'e**2',
#[Out]#  '_72': 7.3890560989306495,
#[Out]#  '_i73': 'x=5.7',
#[Out]#  '_i74': 'int(X)',
#[Out]#  '_i75': 'int(x)',
#[Out]#  '_75': 5,
#[Out]#  '_i76': 'ceil(x)',
#[Out]#  '_76': 6,
#[Out]#  '_i77': 'floor(x)',
#[Out]#  '_77': 5,
#[Out]#  '_i78': 'round(x)',
#[Out]#  '_78': 6,
#[Out]#  '_i79': 'ceil(x)',
#[Out]#  '_79': 6,
#[Out]#  '_i80': 'from cmath import *',
#[Out]#  'phase': <function cmath.phase(z, /)>,
#[Out]#  'polar': <function cmath.polar(z, /)>,
#[Out]#  'rect': <function cmath.rect(r, phi, /)>,
#[Out]#  'infj': infj,
#[Out]#  'nanj': nanj,
#[Out]#  '_i81': 'c= complex (-1,2)',
#[Out]#  '_i82': 'c',
#[Out]#  '_82': (-1+2j),
#[Out]#  '_i83': 'type(c)',
#[Out]#  '_83': complex,
#[Out]#  '_i84': 'c.real',
#[Out]#  '_84': -1.0,
#[Out]#  '_i85': 'c.imag',
#[Out]#  '_85': 2.0,
#[Out]#  '_i86': 'phase(c)',
#[Out]#  '_86': 2.0344439357957027,
#[Out]#  '_i87': 'abs(c)',
#[Out]#  '_87': 2.23606797749979,
#[Out]#  '_i88': 'c.conjugate()',
#[Out]#  '_88': (-1-2j),
#[Out]#  '_i89': 'clear',
#[Out]#  '_exit_code': 0,
#[Out]#  '_i90': 'polar(c)',
#[Out]#  '_90': (2.23606797749979, 2.0344439357957027),
#[Out]#  '_i91': 'phase(c)',
#[Out]#  '_91': 2.0344439357957027,
#[Out]#  '_i92': 'atan2(c.imag,c.real)',
#[Out]#  '_92': 2.0344439357957027,
#[Out]#  '_i93': 'atan2(c.imag,c.real) #arcotangente parte imaginaria/parte real',
#[Out]#  '_93': 2.0344439357957027,
#[Out]#  '_i94': 'atan2(c.imag/c.real) #arcotangente parte imaginaria/parte real',
#[Out]#  '_i95': '?atan2',
#[Out]#  '_i96': 'c',
#[Out]#  '_96': (-1+2j),
#[Out]#  '_i97': 'polar(c)',
#[Out]#  '_97': (2.23606797749979, 2.0344439357957027),
#[Out]#  '_i98': 'rect(polar(c))',
#[Out]#  '_i99': 'rect(abs(c),phase(c))',
#[Out]#  '_99': (-1+2j),
#[Out]#  '_i100': 'clear',
#[Out]#  '_i101': "x=[4,7.4,True,4+2j,'ola',[2,1]]",
#[Out]#  '_i102': 'print(x)',
#[Out]#  '_i103': 'x',
#[Out]#  '_103': [4, 7.4, True, (4+2j), 'ola', [2, 1]],
#[Out]#  '_i104': 'type(x)',
#[Out]#  '_104': list,
#[Out]#  '_i105': 'x.[0]',
#[Out]#  '_i106': 'x[0]',
#[Out]#  '_106': 4,
#[Out]#  '_i107': 'x[-1] #para el ultimo elemento, asi no hay que contarlo',
#[Out]#  '_107': [2, 1],
#[Out]#  '_i108': 'x[1]',
#[Out]#  '_108': 7.4,
#[Out]#  '_i109': 'x[6]',
#[Out]#  '_i110': 'len(x)',
#[Out]#  '_110': 6,
#[Out]#  '_i111': 'x[-2] #el penultimo elemento',
#[Out]#  '_111': 'ola',
#[Out]#  '_i112': 'x= [1,2,3,4,5,6,7,8,9]',
#[Out]#  '_i113': 'max(x)',
#[Out]#  '_113': 9,
#[Out]#  '_i114': 'min(x)',
#[Out]#  '_114': 1,
#[Out]#  '_i115': 'sum(x)',
#[Out]#  '_115': 45,
#[Out]#  '_i116': 'x[3]=20',
#[Out]#  '_i117': 'x',
#[Out]#  '_117': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i118': 'x[3:5]',
#[Out]#  '_118': [20, 5],
#[Out]#  '_i119': 'x[3:5] #para acceder a varios elementos',
#[Out]#  '_119': [20, 5],
#[Out]#  '_i120': 'x[3:6] ',
#[Out]#  '_120': [20, 5, 6],
#[Out]#  '_i121': 'x[3:] #desde 3 hasta el final',
#[Out]#  '_121': [20, 5, 6, 7, 8, 9],
#[Out]#  '_i122': 'x[:6] #desde el principio hasta el 6',
#[Out]#  '_122': [1, 2, 3, 20, 5, 6],
#[Out]#  '_i123': 'x[:6] #desde el principio hasta el 5***',
#[Out]#  '_123': [1, 2, 3, 20, 5, 6],
#[Out]#  '_i124': 'clear',
#[Out]#  '_i125': 'x[2:4]',
#[Out]#  '_125': [3, 20],
#[Out]#  '_i126': 'x[2:4]=[30,30]',
#[Out]#  '_i127': 'x',
#[Out]#  '_127': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i128': 'x[2:4]=[30,30] #para cambiar los valores',
#[Out]#  '_i129': 'clear',
#[Out]#  '_i130': 'x[4:7]=[]',
#[Out]#  '_i131': 'x',
#[Out]#  '_131': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i132': 'x[4:7]=[] #para eliminar elementos',
#[Out]#  '_i133': 'x[2] = []',
#[Out]#  '_i134': 'x',
#[Out]#  '_134': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i135': 'range(6)',
#[Out]#  '_135': range(0, 6),
#[Out]#  '_i136': 'list(range(6))',
#[Out]#  '_136': [0, 1, 2, 3, 4, 5],
#[Out]#  '_i137': 'list(range(6)) #te saca una lista de rango 6',
#[Out]#  '_137': [0, 1, 2, 3, 4, 5],
#[Out]#  '_i138': 'list(range(1,6)) #si queremos que empiece en 1 y no 0',
#[Out]#  '_138': [1, 2, 3, 4, 5],
#[Out]#  '_i139': 'y=list(range(1,6)) #si queremos que empiece en 1 y no 0',
#[Out]#  '_i140': 'sum(y)',
#[Out]#  '_140': 15,
#[Out]#  '_i141': 'range(1,6,2)',
#[Out]#  '_141': range(1, 6, 2),
#[Out]#  '_i142': 'list(range(1,6,2))',
#[Out]#  '_142': [1, 3, 5],
#[Out]#  '_i143': 'list(range(1,6,2)) #la lista va de 2 en 2',
#[Out]#  '_143': [1, 3, 5],
#[Out]#  '_i144': 'clear',
#[Out]#  '_i145': 'x',
#[Out]#  '_145': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i146': 'x[1:3] = [2,3]',
#[Out]#  '_i147': 'x',
#[Out]#  '_147': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i148': 'x[1:3] = [8,9,7]',
#[Out]#  '_i149': 'x',
#[Out]#  '_149': [1, 8, 9, 7, 7, 30],
#[Out]#  '_i150': 'x[1:3] = [8,9,7] #cambia la longitud de la lista',
#[Out]#  '_i151': 'clear',
#[Out]#  '_i152': 'x=[2,4,1,8,2]',
#[Out]#  '_i153': 'x',
#[Out]#  '_153': [10, 5, 2, 1],
#[Out]#  '_i154': 'len(x)',
#[Out]#  '_154': 5,
#[Out]#  '_i155': '1 in x',
#[Out]#  '_155': True,
#[Out]#  '_i156': '8 not in x',
#[Out]#  '_156': False,
#[Out]#  '_i157': '5 not in x',
#[Out]#  '_157': True,
#[Out]#  '_i158': 'x',
#[Out]#  '_158': [10, 5, 2, 1],
#[Out]#  '_i159': 'clear',
#[Out]#  '_i160': 'c',
#[Out]#  '_160': (-1+2j),
#[Out]#  '_i161': 'x',
#[Out]#  '_161': [10, 5, 2, 1],
#[Out]#  '_i162': 'x.append(5) #mete el 5 al final de la lista',
#[Out]#  '_i163': 'x',
#[Out]#  '_163': [10, 5, 2, 1],
#[Out]#  '_i164': 'x.insert(3,10)',
#[Out]#  '_i165': 'x',
#[Out]#  '_165': [10, 5, 2, 1],
#[Out]#  '_i166': 'x.insert(3,10) #inserta un elemento en una posicion dada',
#[Out]#  '_i167': 'clear',
#[Out]#  '_i168': '?x.insert',
#[Out]#  '_i169': 'x.reverse()',
#[Out]#  '_i170': 'x',
#[Out]#  '_170': [10, 5, 2, 1],
#[Out]#  '_i171': 'x.reverse() #les da la vuelta',
#[Out]#  '_i172': 'x',
#[Out]#  '_172': [10, 5, 2, 1],
#[Out]#  '_i173': 'clear',
#[Out]#  '_i174': 'x',
#[Out]#  '_174': [10, 5, 2, 1],
#[Out]#  '_i175': 'x[::-1] #tambien le da la vuelta a la lista',
#[Out]#  '_175': [5, 2, 8, 10, 10, 1, 4, 2],
#[Out]#  '_i176': 'x[::-1] #tambien le da la vuelta a la lista',
#[Out]#  '_176': [5, 2, 8, 10, 10, 1, 4, 2],
#[Out]#  '_i177': 'x.sort() #ordena',
#[Out]#  '_i178': 'x',
#[Out]#  '_178': [10, 5, 2, 1],
#[Out]#  '_i179': 'x.sort(reverse=True)',
#[Out]#  '_i180': 'x',
#[Out]#  '_180': [10, 5, 2, 1],
#[Out]#  '_i181': 'x.sort(reverse=True) #orden decreciente',
#[Out]#  '_i182': 'clear',
#[Out]#  '_i183': 'x.count(2) #cuenta cuantos elementos hay iguales a 2',
#[Out]#  '_183': 2,
#[Out]#  '_i184': 'x.count(9)',
#[Out]#  '_184': 0,
#[Out]#  '_i185': '9 in x',
#[Out]#  '_185': False,
#[Out]#  '_i186': 'clear',
#[Out]#  '_i187': 'x.remove(8)',
#[Out]#  '_i188': 'x',
#[Out]#  '_188': [10, 5, 2, 1],
#[Out]#  '_i189': 'x.remove(10)',
#[Out]#  '_i190': 'x',
#[Out]#  '_190': [10, 5, 2, 1],
#[Out]#  '_i191': 'clear',
#[Out]#  '_i192': 'x.remove(2)',
#[Out]#  '_i193': 'x',
#[Out]#  '_193': [10, 5, 2, 1],
#[Out]#  '_i194': 'x.index(2)',
#[Out]#  '_194': 3,
#[Out]#  '_i195': 'x.index(9)',
#[Out]#  '_i196': 'x[2]=[]',
#[Out]#  '_i197': 'x',
#[Out]#  '_197': [10, 5, 2, 1],
#[Out]#  '_i198': 'del x[2]',
#[Out]#  '_i199': 'x',
#[Out]#  '_199': [10, 5, 2, 1],
#[Out]#  '_i200': 'clear',
#[Out]#  '_i201': 'x=[3.5,3.1,8.4]',
#[Out]#  '_i202': '[int(i) for i in x] #sentencia for',
#[Out]#  '_202': [3, 3, 8],
#[Out]#  '_i203': '[int(i) for i in x] #vectorizar ',
#[Out]#  '_203': [3, 3, 8],
#[Out]#  '_i204': '[int(i) for i in x] #vectorizar. Aplica la funcion i para todos los elementos de la lista en una sola linea.',
#[Out]#  '_204': [3, 3, 8],
#[Out]#  '_i205': '[i*i for i in x] ',
#[Out]#  '_205': [12.25, 9.610000000000001, 70.56],
#[Out]#  '_i206': 'vars()'}
'count' in dir(x)
#[Out]# True
'print' in dir(x)
#[Out]# False
x.print()
print(x)
get_ipython().run_line_magic('clear', '')
a=(1,2,3,4,5) #tuplas son listas que no cambian
type(a)
#[Out]# tuple
y=(1,2,3,4,5) #tuplas son listas que no cambian
type(y)
#[Out]# tuple
get_ipython().run_line_magic('clear', '')
x[0]=20
y[0]=10
len(y)
#[Out]# 5
s='ola a todas'
len(s)
#[Out]# 11
get_ipython().run_line_magic('clear', '')
s.count('o')
#[Out]# 2
s.count(' ')
#[Out]# 2
s.index()
s.index(' ')
#[Out]# 3
get_ipython().run_line_magic('clear', '')
s.fin(' ')
s.find(' ')
#[Out]# 3
get_ipython().run_line_magic('clear', '')
s.find('p')
#[Out]# -1
s.find('p') #si no esta te da un -1
#[Out]# -1
flatnonzero([i.isspace() for i in s]) #para comprobar si los caracters en s son espacio 
s.isspace()
#[Out]# False
[i.isspace() for i in s]
#[Out]# [False, False, False, True, False, True, False, False, False, False, False]
get_ipython().run_line_magic('clear', '')
flatnonzero([i.isspace() for i in s]) #para comprobar si los caracters en s son espacio 
from numpy import *
flatnonzero([i.isspace() for i in s]) #para comprobar si los caracters en s son espacio 
#[Out]# array([3, 5])
[i.isspace() for i in s]
#[Out]# [False, False, False, True, False, True, False, False, False, False, False]
get_ipython().run_line_magic('clear', '')
s.count(' ')
#[Out]# 2
' '  in s
#[Out]# True
s= 'x=123'
s
#[Out]# 'x=123'
'5'.isdigit()
#[Out]# True
s
#[Out]# 'x=123'
get_ipython().run_line_magic('clear', '')
[i.isdigit() for i in s]
#[Out]# [False, False, True, True, True]
sum([i.isdigit() for i in s])
#[Out]# 3
exit()
