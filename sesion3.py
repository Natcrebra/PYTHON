# IPython log file

a=zeros([2,3]) #definiendo una matriz
a
#[Out]# array([[0., 0., 0.],
#[Out]#        [0., 0., 0.]])
type(a)
#[Out]# numpy.ndarray
a=zeros([2,3],int) #definiendo una matriz
a
#[Out]# array([[0, 0, 0],
#[Out]#        [0, 0, 0]])
a=zeros([2,3],int)+5  #definiendo una matriz
a
#[Out]# array([[5, 5, 5],
#[Out]#        [5, 5, 5]])
get_ipython().run_line_magic('clear', '')
a=ones([2,3])  #definiendo una matriz
a
#[Out]# array([[1., 1., 1.],
#[Out]#        [1., 1., 1.]])
a=5*ones([2,3])
a
#[Out]# array([[5., 5., 5.],
#[Out]#        [5., 5., 5.]])
#para que todos los elementos valgan 5 lo multiplicamos por la matriz de unos
x=5
y=x
x
#[Out]# 5
y
#[Out]# 5
x=6
y
#[Out]# 5
x=zeros([2,3])
z
x
#[Out]# array([[0., 0., 0.],
#[Out]#        [0., 0., 0.]])
y=x
y
#[Out]# array([[0., 0., 0.],
#[Out]#        [0., 0., 0.]])
get_ipython().run_line_magic('clear', '')
x[0,0]=3
x
#[Out]# array([[3., 0., 0.],
#[Out]#        [0., 0., 0.]])
y
#[Out]# array([[3., 0., 0.],
#[Out]#        [0., 0., 0.]])
y=x.copy()
y
#[Out]# array([[3., 0., 0.],
#[Out]#        [0., 0., 0.]])
x
#[Out]# array([[3., 0., 0.],
#[Out]#        [0., 0., 0.]])
x[0,0]=0
x
#[Out]# array([[0., 0., 0.],
#[Out]#        [0., 0., 0.]])
y
#[Out]# array([[3., 0., 0.],
#[Out]#        [0., 0., 0.]])
get_ipython().run_line_magic('clear', '')
x=array([1,2,3])
x
#[Out]# array([1, 2, 3])
insert(x,1.20)
insert(x,1,20)
#[Out]# array([ 1, 20,  2,  3])
x
#[Out]# array([1, 2, 3])
a
#[Out]# array([[5., 5., 5.],
#[Out]#        [5., 5., 5.]])
b=ones([2,3])
b
#[Out]# array([[1., 1., 1.],
#[Out]#        [1., 1., 1.]])
get_ipython().run_line_magic('clear', '')
a = np.array((1,2,3))

b = np.array((4,5,6))

np.hstack((a,b))
array([1, 2, 3, 4, 5, 6])

a = np.array([[1],[2],[3]])

b = np.array([[4],[5],[6]])

np.hstack((a,b))
array([[1, 4],
       [2, 5],
       [3, 6]])
#[Out]# array([[1, 4],
#[Out]#        [2, 5],
#[Out]#        [3, 6]])
x
#[Out]# array([1, 2, 3])
append(x,10)
#[Out]# array([ 1,  2,  3, 10])
x
#[Out]# array([1, 2, 3])
x=append(x,10)
x
#[Out]# array([ 1,  2,  3, 10])
get_ipython().run_line_magic('clear', '')
delete(x,2)
#[Out]# array([ 1,  2, 10])
x
#[Out]# array([ 1,  2,  3, 10])
x=delete(x,2)
x
#[Out]# array([ 1,  2, 10])
a.T
#[Out]# array([[1, 2, 3]])
a.flatten()
#[Out]# array([1, 2, 3])
b
#[Out]# array([[4],
#[Out]#        [5],
#[Out]#        [6]])
b.flatten()
#[Out]# array([4, 5, 6])
b.flatten()
#[Out]# array([4, 5, 6])
get_ipython().run_line_magic('clear', '')
ravel(a)
#[Out]# array([1, 2, 3])
x
#[Out]# array([ 1,  2, 10])
y
#[Out]# array([[3., 0., 0.],
#[Out]#        [0., 0., 0.]])
y=array([4,9,2,5])
x
#[Out]# array([ 1,  2, 10])
y
#[Out]# array([4, 9, 2, 5])
concatenate(x,y)
concatenate((x,y))
#[Out]# array([ 1,  2, 10,  4,  9,  2,  5])
get_ipython().run_line_magic('clear', '')
vstack((x,y))
x
#[Out]# array([ 1,  2, 10])
y
#[Out]# array([4, 9, 2, 5])
x=x.append(10)
x=append(x,10)
x
#[Out]# array([ 1,  2, 10, 10])
vstack((x,y))
#[Out]# array([[ 1,  2, 10, 10],
#[Out]#        [ 4,  9,  2,  5]])
b=array([[6,4,1],[5,1,6]])
b
#[Out]# array([[6, 4, 1],
#[Out]#        [5, 1, 6]])
a
#[Out]# array([[1],
#[Out]#        [2],
#[Out]#        [3]])
c=([[3,4,5],[6,7,8]])
c
#[Out]# [[3, 4, 5], [6, 7, 8]]
hstack(b,c)
hstack((b,c))
#[Out]# array([[6, 4, 1, 3, 4, 5],
#[Out]#        [5, 1, 6, 6, 7, 8]])
vstack((b,c))
#[Out]# array([[6, 4, 1],
#[Out]#        [5, 1, 6],
#[Out]#        [3, 4, 5],
#[Out]#        [6, 7, 8]])
vstack((a,[1,2,3]))
vstack((b,[1,2,3]))
#[Out]# array([[6, 4, 1],
#[Out]#        [5, 1, 6],
#[Out]#        [1, 2, 3]])
b
#[Out]# array([[6, 4, 1],
#[Out]#        [5, 1, 6]])
b=vstack((b,[1,2,3]))
b
#[Out]# array([[6, 4, 1],
#[Out]#        [5, 1, 6],
#[Out]#        [1, 2, 3]])
c
#[Out]# [[3, 4, 5], [6, 7, 8]]
get_ipython().run_line_magic('clear', '')
hstack((b,c,b))
hstack((b,c,b))
b
#[Out]# array([[6, 4, 1],
#[Out]#        [5, 1, 6],
#[Out]#        [1, 2, 3]])
c
#[Out]# [[3, 4, 5], [6, 7, 8]]
c.T
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1],
#[Out]#        [2],
#[Out]#        [3]])
a.T
#[Out]# array([[1, 2, 3]])
hstack((a[:,0:2],b,a[:,2:]))
#[Out]# array([[1, 6, 4, 1],
#[Out]#        [2, 5, 1, 6],
#[Out]#        [3, 1, 2, 3]])
b=array([1,2,3])
vstack((a[0:1,:],b,a[1:,:]))
hstack((a[0:1,:],b,a[1:,:]))
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1],
#[Out]#        [2],
#[Out]#        [3]])
a=a.T
a
#[Out]# array([[1, 2, 3]])
b
#[Out]# array([1, 2, 3])
vstack((a[0:1,:],b,a[1:,:]))
#[Out]# array([[1, 2, 3],
#[Out]#        [1, 2, 3]])
hstack((a[0:1,:],b,a[1:,:]))
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1, 2, 3]])
a[0,:] #para acceder a la primera fila
#[Out]# array([1, 2, 3])
a[0] #para acceder a la primera fila
#[Out]# array([1, 2, 3])
a[1] #para acceder a la segunda fila
#salta error porque a solo tiene una fila
a=array([[1,2,3],[4,5,6]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
a[1] #para acceder a la segunda fila
#[Out]# array([4, 5, 6])
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
a[:,0] #para acceder a la primera columna
#[Out]# array([1, 4])
a[:,1] #para acceder a la segunda columna
#[Out]# array([2, 5])
a[:,2] #para acceder a la tercera columna
#[Out]# array([3, 6])
shape(a)
#[Out]# (2, 3)
nf=shape(a)[0]
nf
#[Out]# 2
nc=shape(a)[1]
nc
#[Out]# 3
nf,nc
#[Out]# (2, 3)
a.reshape(3,2)
#[Out]# array([[1, 2],
#[Out]#        [3, 4],
#[Out]#        [5, 6]])
a.T
#[Out]# array([[1, 4],
#[Out]#        [2, 5],
#[Out]#        [3, 6]])
z=9
z**2
#[Out]# 81
x
#[Out]# array([ 1,  2, 10, 10])
x**2
x
#[Out]# array([ 1,  2, 10, 10])
l=[1,2,3]
l**2
[i**2 for i in l]
#[Out]# [1, 4, 9]
get_ipython().run_line_magic('clear', '')
x
#[Out]# array([ 1,  2, 10, 10])
y
#[Out]# array([4, 9, 2, 5])
x+y
#[Out]# array([ 5, 11, 12, 15])
b=array([[5,4,1],[6,1,7]])
b
#[Out]# array([[5, 4, 1],
#[Out]#        [6, 1, 7]])
a+b
#[Out]# array([[ 6,  6,  4],
#[Out]#        [10,  6, 13]])
x/y
#[Out]# array([0.25      , 0.22222222, 5.        , 2.        ])
x*y
#[Out]# array([ 4, 18, 20, 50])
a*b
#[Out]# array([[ 5,  8,  3],
#[Out]#        [24,  5, 42]])
a/b
#[Out]# array([[0.2       , 0.5       , 3.        ],
#[Out]#        [0.66666667, 5.        , 0.85714286]])
a/2
#[Out]# array([[0.5, 1. , 1.5],
#[Out]#        [2. , 2.5, 3. ]])
x
#[Out]# array([ 1,  2, 10, 10])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
x=delete(x,3)
x
#[Out]# array([ 1,  2, 10])
dot(a,x)
#[Out]# array([35, 74])
dot(x,x)
#[Out]# 105
dot(a,b.T)
#[Out]# array([[16, 29],
#[Out]#        [46, 71]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
b
#[Out]# array([[5, 4, 1],
#[Out]#        [6, 1, 7]])
b.T
#[Out]# array([[5, 6],
#[Out]#        [4, 1],
#[Out]#        [1, 7]])
5>3
#[Out]# True
5>3
#[Out]# True
5<3
#[Out]# False
z
#[Out]# 9
z>6
#[Out]# True
z==1
#[Out]# False
z!8
z!=8
#[Out]# True
get_ipython().run_line_magic('clear', '')
x
#[Out]# array([ 1,  2, 10])
x>5
#[Out]# array([False, False,  True])
#se aplica componente a componente
as
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
a>3
#[Out]# array([[False, False, False],
#[Out]#        [ True,  True,  True]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
b
#[Out]# array([[5, 4, 1],
#[Out]#        [6, 1, 7]])
a*b
#[Out]# array([[ 5,  8,  3],
#[Out]#        [24,  5, 42]])
dot(a,b.T)
#[Out]# array([[16, 29],
#[Out]#        [46, 71]])
x
#[Out]# array([ 1,  2, 10])
sin(x) #se aplica componente a componente
#[Out]# array([ 0.84147098,  0.90929743, -0.54402111])
round_(x)
#[Out]# array([ 1,  2, 10])
x=array([0.8,0.1,2.6])
round_(x)
#[Out]# array([1., 0., 3.])
int_(x)
#[Out]# array([0, 0, 2])
get_ipython().run_line_magic('clear', '')
sort(x)
#[Out]# array([0.1, 0.8, 2.6])
sort(x)[::-1]
#[Out]# array([2.6, 0.8, 0.1])
x.sort()
x
#[Out]# array([0.1, 0.8, 2.6])
x=array([9,3,5,1,0])
argsort(x)
#[Out]# array([4, 3, 1, 2, 0])
sort(x)
#[Out]# array([0, 1, 3, 5, 9])
x
#[Out]# array([9, 3, 5, 1, 0])
x%2==0
#[Out]# array([False, False, False, False,  True])
x[x%2==0]
#[Out]# array([0])
x[x%2==1] #para los impares
#[Out]# array([9, 3, 5, 1])
get_ipython().run_line_magic('clear', '')
flatnonzero(x%2==0)
#[Out]# array([4])
flatnonzero(x%2==1)
#[Out]# array([0, 1, 2, 3])
x%2==1
#[Out]# array([ True,  True,  True,  True, False])
where(x%2==1)
#[Out]# (array([0, 1, 2, 3]),)
where(x%2==1)[0]
#[Out]# array([0, 1, 2, 3])
a=array([[1,2,3],[4,5,6],[7,8,9]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
a%2==0
#[Out]# array([[False,  True, False],
#[Out]#        [ True, False,  True],
#[Out]#        [False,  True, False]])
diagonal(a)
#[Out]# array([1, 5, 9])
sum(a)
#[Out]# 45
prod(a)
#[Out]# 362880
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
get_ipython().run_line_magic('clear', '')
a.sum(0)
#[Out]# array([12, 15, 18])
a.sum(1)
#[Out]# array([ 6, 15, 24])
a.prod(0)
#[Out]# array([ 28,  80, 162])
a.prod(1)
#[Out]# array([  6, 120, 504])
prod(diagonal(a))
#[Out]# 45
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
all(a)
#[Out]# True
a[0,0]=0
all(a)
#[Out]# False
all(a,0)
#[Out]# array([False,  True,  True])
a
#[Out]# array([[0, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
all(a,1)
#[Out]# array([False,  True,  True])
all(a%2==1,0)
#[Out]# array([False, False, False])
a[2,0]=6
a
#[Out]# array([[0, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [6, 8, 9]])
all(a%2==0,0)
#[Out]# array([ True, False, False])
all(a%2==0,1)
#[Out]# array([False, False, False])
get_ipython().run_line_magic('clear', '')
x
#[Out]# array([9, 3, 5, 1, 0])
any(x==5)
#[Out]# True
any(x==4)
#[Out]# False
all(x>=0)
#[Out]# True
all(x>0)
#[Out]# False
a
#[Out]# array([[0, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [6, 8, 9]])
any(a==5,0)
#[Out]# array([False,  True, False])
x
#[Out]# array([9, 3, 5, 1, 0])
get_ipython().run_line_magic('clear', '')
c
#[Out]# [[3, 4, 5], [6, 7, 8]]
x
#[Out]# array([9, 3, 5, 1, 0])
x%2==1
#[Out]# array([ True,  True,  True,  True, False])
sum(x%2==1)
#[Out]# 4
extract(x%2==1,x)
#[Out]# array([9, 3, 5, 1])
a
#[Out]# array([[0, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [6, 8, 9]])
b
#[Out]# array([[5, 4, 1],
#[Out]#        [6, 1, 7]])
a=array([[1,2,3],[4,5,6]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
b
#[Out]# array([[5, 4, 1],
#[Out]#        [6, 1, 7]])
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
b
#[Out]# array([[5, 4, 1],
#[Out]#        [6, 1, 7]])
a==b
#[Out]# array([[False, False, False],
#[Out]#        [False, False, False]])
b=a.copy()
a==b
#[Out]# array([[ True,  True,  True],
#[Out]#        [ True,  True,  True]])
array_equal(a,b)
#[Out]# True
allclose(a,b)
#[Out]# True
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
b
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6]])
a=a.astype('float')
a
#[Out]# array([[1., 2., 3.],
#[Out]#        [4., 5., 6.]])
b=b.astype('float')
b
#[Out]# array([[1., 2., 3.],
#[Out]#        [4., 5., 6.]])
array_equal(a,b)
#[Out]# True
b[0,0]=b[0,0]+1e-9
array_equal(a,b)
#[Out]# False
allclose(a,b)
#[Out]# True
b[0,0]=a[0,0]+1e-7
allclose(a,b)
#[Out]# True
b[0,0]=a[0,0]+1e-6
allclose(a,b)
#[Out]# True
b[0,0]=a[0,0]+1e-3
allclose(a,b)
#[Out]# False
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1., 2., 3.],
#[Out]#        [4., 5., 6.]])
b
#[Out]# array([[1.001, 2.   , 3.   ],
#[Out]#        [4.   , 5.   , 6.   ]])
a==b
#[Out]# array([[False,  True,  True],
#[Out]#        [ True,  True,  True]])
equal(a,b)
#[Out]# array([[False,  True,  True],
#[Out]#        [ True,  True,  True]])
a>b
#[Out]# array([[False, False, False],
#[Out]#        [False, False, False]])
greater(a,b)
#[Out]# array([[False, False, False],
#[Out]#        [False, False, False]])
a!=b
#[Out]# array([[ True, False, False],
#[Out]#        [False, False, False]])
not_equal(a,b)
#[Out]# array([[ True, False, False],
#[Out]#        [False, False, False]])
1 and 0
#[Out]# 0
true and false
True and False
#[Out]# False
True and True
#[Out]# True
logical_and(True,True)
#[Out]# True
logical_or(True,False)
#[Out]# True
logical_or(False,False)
#[Out]# False
logical_or(0,1)
#[Out]# True
1 or 0
#[Out]# 1
a
#[Out]# array([[1., 2., 3.],
#[Out]#        [4., 5., 6.]])
logical_and(a,b)
#[Out]# array([[ True,  True,  True],
#[Out]#        [ True,  True,  True]])
a[0,0]=0
logical_and(a,b)
#[Out]# array([[False,  True,  True],
#[Out]#        [ True,  True,  True]])
get_ipython().run_line_magic('clear', '')
logical_or(a,b)
#[Out]# array([[ True,  True,  True],
#[Out]#        [ True,  True,  True]])
b[0,0]=0
a
#[Out]# array([[0., 2., 3.],
#[Out]#        [4., 5., 6.]])
b
#[Out]# array([[0., 2., 3.],
#[Out]#        [4., 5., 6.]])
logical_or(a,b)
#[Out]# array([[False,  True,  True],
#[Out]#        [ True,  True,  True]])
get_ipython().run_line_magic('clear', '')
x
#[Out]# array([9, 3, 5, 1, 0])
where(x%2==1)
#[Out]# (array([0, 1, 2, 3]),)
where(x%2==1)[0]
get_ipython().run_line_magic('clear', '')
where(x%2==1)[0]
#[Out]# array([0, 1, 2, 3])
a=array([[1,2,3],[4,5,6],[7,8,9]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
where(logical_and(a>=2,a<=6),-1,0) #donde se cumpla la condicion pone -1 y donde no pone 0
#[Out]# array([[ 0, -1, -1],
#[Out]#        [-1, -1, -1],
#[Out]#        [ 0,  0,  0]])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
get_ipython().run_line_magic('clear', '')
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
max(a)
amax(a)
#[Out]# 9
argmax(a)
#[Out]# 8
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
ptp(a)
#[Out]# 8
mean(a)
#[Out]# 5.0
std(a)
#[Out]# 2.581988897471611
median(a)
#[Out]# 5.0
var(a)
#[Out]# 6.666666666666667
get_ipython().run_line_magic('clear', '')
x
#[Out]# array([9, 3, 5, 1, 0])
a
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', 'datos.txt')
savetxt('datos.txt',a)
get_ipython().run_line_magic('ls', '')
savetxt('datos.txt',a,'%i')
get_ipython().run_line_magic('ls', '')
savetxt('datos.txt',a,'%2f')
get_ipython().run_line_magic('ls', '')
savetxt('datos.txt',a,'%.2f')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('clear', '')
savetxt('datos.txt',a,'%i')
c=loadtxt('datos.txt')
c
#[Out]# array([[1., 2., 3.],
#[Out]#        [4., 5., 6.],
#[Out]#        [7., 8., 9.]])
c=loadtxt('datos.txt','int')
c
#[Out]# array([[1, 2, 3],
#[Out]#        [4, 5, 6],
#[Out]#        [7, 8, 9]])
get_ipython().run_line_magic('clear', '')
from numpy import *
import random
random.random()
#[Out]# 0.9705781430588488
random.random()
#[Out]# 0.5465590465977993
random.random()
#[Out]# 0.3935893935358954
random.uniform(3,7)
#[Out]# 4.389632672649906
random.uniform(3,7)
#[Out]# 4.750258589304899
random.uniform(3,7)
#[Out]# 6.629292818379783
random.randint(3,7)
#[Out]# 4
random.randint(3,7)
#[Out]# 3
random.randint(3,7)
#[Out]# 5
random.randint(3,7)
#[Out]# 7
random.randint(3,7)
#[Out]# 4
random.randint(3,7)
#[Out]# 6
random.randint(3,7)
#[Out]# 3
random.randrange(3,20)
#[Out]# 10
random.randrange(3,20)
#[Out]# 10
random.randrange(3,20)
#[Out]# 17
random.randrange(3,20)
#[Out]# 15
random.randrange(3,20)
#[Out]# 17
random.randrange(3,20)
#[Out]# 8
random.randrange(3,20)
#[Out]# 13
random.randrange(3,20)
#[Out]# 4
range(3,20)
#[Out]# range(3, 20)
list(range(3,20))
#[Out]# [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
random.choice(range(3,20))
#[Out]# 19
random.choice(range(3,20))
#[Out]# 6
random.choice(range(3,20))
#[Out]# 9
random.choice(range(3,20))
#[Out]# 15
random.choice(range(3,20))
#[Out]# 8
random.shuffle(x)
x
#[Out]# array([5, 1, 0, 9, 3])
random.shuffle(x)
x
#[Out]# array([5, 0, 1, 3, 9])
random.sample(x,3) #devuelve 3 elementos aleatorios de x
random.sample(x,2) #devuelve 3 elementos aleatorios de x
x=[3,4,8,1,0,5]
random.sample(x,2) #devuelve 3 elementos aleatorios de x
#[Out]# [1, 5]
random.choice(x)
#[Out]# 1
random.choice(x)
#[Out]# 4
random.choice(x)
#[Out]# 8
random.choice(x)
#[Out]# 5
random.choice(x)
#[Out]# 1
from numpy.random import *
get_ipython().run_line_magic('clear', '')
rand()
#[Out]# 0.763127968206821
rand()
#[Out]# 0.03843622806246205
rand()
#[Out]# 0.6711575989939801
rand()
#[Out]# 0.5468352330308105
rand()
#[Out]# 0.2625409511396355
rand(2,3)
#[Out]# array([[0.71511563, 0.36005897, 0.16381761],
#[Out]#        [0.86021162, 0.84488718, 0.29522769]])
random([2,3])
#[Out]# array([[0.39862056, 0.33932663, 0.10596408],
#[Out]#        [0.85101509, 0.36609228, 0.47045618]])
randint(3,15,10)
#[Out]# array([ 7, 10, 10, 14, 13, 13, 13,  4,  7,  6])
#10 numeros enteros entre 3 y 15
rand(2,3)
#[Out]# array([[0.51582905, 0.85328472, 0.29350101],
#[Out]#        [0.62644361, 0.29089959, 0.65475863]])
9*rand(2,3)+1
#[Out]# array([[6.08194856, 3.47559196, 3.11684892],
#[Out]#        [4.17156206, 4.06657881, 4.21859526]])
round_(9*rand(2,3)+1)  #matriz con numeros aleatorios entre 1 y 9
#[Out]# array([[ 4.,  2.,  6.],
#[Out]#        [ 4., 10.,  2.]])
round_(9*rand(2,3)+1)  #matriz con numeros aleatorios entre 1 y 9
#[Out]# array([[7., 3., 7.],
#[Out]#        [2., 8., 2.]])
get_ipython().run_line_magic('clear', '')
x
#[Out]# [3, 4, 8, 1, 0, 5]
shuffle(x)
x
#[Out]# [5, 3, 0, 4, 1, 8]
shuffle(x)
x
#[Out]# [8, 3, 1, 0, 4, 5]
get_ipython().run_line_magic('clear', '')
permutation(3) #realiza permutaciones sobre range(3)
#[Out]# array([1, 2, 0])
permutation(3) #realiza permutaciones sobre range(3)
#[Out]# array([0, 1, 2])
permutation(3) #realiza permutaciones sobre range(3)
#[Out]# array([2, 1, 0])
permutation(3) #realiza permutaciones sobre range(3)
#[Out]# array([1, 2, 0])
permutation(5)
#[Out]# array([3, 2, 4, 1, 0])
permutation([5,7,4,2])
#[Out]# array([2, 5, 4, 7])
permutation([5,7,4,2])
#[Out]# array([7, 4, 5, 2])
permutation([5,7,4,2])
#[Out]# array([7, 4, 2, 5])
permutation([5,7,4,2])
#[Out]# array([4, 5, 7, 2])
get_ipython().run_line_magic('clear', '')
#MATPLOTLIB--------------------------REPRESENTACIONES GRAFICAS-----------------------------------
x=linspace(-pi,pi,100)
x
#[Out]# array([-3.14159265, -3.07812614, -3.01465962, -2.9511931 , -2.88772658,
#[Out]#        -2.82426006, -2.76079354, -2.69732703, -2.63386051, -2.57039399,
#[Out]#        -2.50692747, -2.44346095, -2.37999443, -2.31652792, -2.2530614 ,
#[Out]#        -2.18959488, -2.12612836, -2.06266184, -1.99919533, -1.93572881,
#[Out]#        -1.87226229, -1.80879577, -1.74532925, -1.68186273, -1.61839622,
#[Out]#        -1.5549297 , -1.49146318, -1.42799666, -1.36453014, -1.30106362,
#[Out]#        -1.23759711, -1.17413059, -1.11066407, -1.04719755, -0.98373103,
#[Out]#        -0.92026451, -0.856798  , -0.79333148, -0.72986496, -0.66639844,
#[Out]#        -0.60293192, -0.53946541, -0.47599889, -0.41253237, -0.34906585,
#[Out]#        -0.28559933, -0.22213281, -0.1586663 , -0.09519978, -0.03173326,
#[Out]#         0.03173326,  0.09519978,  0.1586663 ,  0.22213281,  0.28559933,
#[Out]#         0.34906585,  0.41253237,  0.47599889,  0.53946541,  0.60293192,
#[Out]#         0.66639844,  0.72986496,  0.79333148,  0.856798  ,  0.92026451,
#[Out]#         0.98373103,  1.04719755,  1.11066407,  1.17413059,  1.23759711,
#[Out]#         1.30106362,  1.36453014,  1.42799666,  1.49146318,  1.5549297 ,
#[Out]#         1.61839622,  1.68186273,  1.74532925,  1.80879577,  1.87226229,
#[Out]#         1.93572881,  1.99919533,  2.06266184,  2.12612836,  2.18959488,
#[Out]#         2.2530614 ,  2.31652792,  2.37999443,  2.44346095,  2.50692747,
#[Out]#         2.57039399,  2.63386051,  2.69732703,  2.76079354,  2.82426006,
#[Out]#         2.88772658,  2.9511931 ,  3.01465962,  3.07812614,  3.14159265])
plot(x,sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x7f0c3443b310>]
xlabel('Tempo (s)')
#[Out]# Text(0.5, 23.52222222222222, 'Tempo (s)')
ylabel('Tension (mV)')
#[Out]# Text(22.097222222222214, 0.5, 'Tension (mV)')
ylabel('Tensión (mV)')
#[Out]# Text(22.097222222222214, 0.5, 'Tensión (mV)')
title('Tensión frente a tiempo')
#[Out]# Text(0.5, 1, 'Tensión frente a tiempo')
title('Tensión frente a tempo')
#[Out]# Text(0.5, 1, 'Tensión frente a tempo')
grid(True)
savefig('tension.png')
savefig('tension.pdf')
exit()
