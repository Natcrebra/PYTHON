# IPython log file

x= [1,2,3]
[i*i for i in x]
#[Out]# [1, 4, 9]
type(x)
#[Out]# list
x= array([1,2,3])
type(x)
#[Out]# numpy.ndarray
x*x
#[Out]# array([1, 4, 9])
x*x #con numpy podemos trabajar con listas como si fueran numeros
#[Out]# array([1, 4, 9])
list(x)
#[Out]# [1, 2, 3]
x.ndim
#[Out]# 1
x[0]
#[Out]# 1
x.size()
x.size
#[Out]# 3
len(x)
#[Out]# 3
x.itemsize
#[Out]# 8
x.dtype
#[Out]# dtype('int64')
x[::-1]
#[Out]# array([3, 2, 1])
3 in x
#[Out]# True
8 in x
#[Out]# False
list(range(5))
#[Out]# [0, 1, 2, 3, 4]
list(range(0,5,0.2))
arange(0,5,0.2)
#[Out]# array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4,
#[Out]#        2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.4, 4.6, 4.8])
arange(0,5,0.2) #nunca supera al 5
#[Out]# array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4,
#[Out]#        2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.4, 4.6, 4.8])
x=arange(0,5,0.2)
len(x)
#[Out]# 25
linspace(0,5,25)
#[Out]# array([0.        , 0.20833333, 0.41666667, 0.625     , 0.83333333,
#[Out]#        1.04166667, 1.25      , 1.45833333, 1.66666667, 1.875     ,
#[Out]#        2.08333333, 2.29166667, 2.5       , 2.70833333, 2.91666667,
#[Out]#        3.125     , 3.33333333, 3.54166667, 3.75      , 3.95833333,
#[Out]#        4.16666667, 4.375     , 4.58333333, 4.79166667, 5.        ])
ones([1,5])
#[Out]# array([[1., 1., 1., 1., 1.]])
ones([1,5], 'int')
#[Out]# array([[1, 1, 1, 1, 1]])
ones([2,5])  #matriz de dos filas y 5 columnas
#[Out]# array([[1., 1., 1., 1., 1.],
#[Out]#        [1., 1., 1., 1., 1.]])
a=ones([2,5])  #matriz de dos filas y 5 columnas
a
#[Out]# array([[1., 1., 1., 1., 1.],
#[Out]#        [1., 1., 1., 1., 1.]])
a[1,4]
#[Out]# 1.0
a[1,4] #para acceder a los elementos
#[Out]# 1.0
a.ndim
#[Out]# 2
x
#[Out]# array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4,
#[Out]#        2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.4, 4.6, 4.8])
x.ndim
#[Out]# 1
x[0]
#[Out]# 0.0
a[0,0]
#[Out]# 1.0
exit()
