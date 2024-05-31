# IPython log file

x=linspace(-pi,pi,40)
plot(x,sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x7ff36a6309d0>]
clf();plot(x,sin(x),color='red')##clf: clear figure; para que no conserve la figura anterior
#[Out]# [<matplotlib.lines.Line2D at 0x7ff3689c9070>]
clf();plot(x,sin(x),color='magenta')##clf: clear figure; para que no conserve la figura anterior
#[Out]# [<matplotlib.lines.Line2D at 0x7ff3689733a0>]
clf();plot(x,sin(x),linestyle='-')
#[Out]# [<matplotlib.lines.Line2D at 0x7ff3689399d0>]
clf();plot(x,sin(x),linestyle='-') #línea continua
#[Out]# [<matplotlib.lines.Line2D at 0x7ff3692196d0>]
clf();plot(x,sin(x),linestyle=':') #línea punteada
#[Out]# [<matplotlib.lines.Line2D at 0x7ff369d93dc0>]
clf();plot(x,sin(x),linestyle='--') #línea segmentada
#[Out]# [<matplotlib.lines.Line2D at 0x7ff369da01c0>]
clf();plot(x,sin(x),linestyle='-.') 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff3689499d0>]
clf();plot(x,sin(x),linewidth=2) #cambia anchura de línea 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff369cf5c70>]
get_ipython().run_line_magic('clear', '')
clf();plot(x,sin(x),marker=s)
clf();plot(x,sin(x),marker='s')
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37b5e6e20>]
clf();plot(x,sin(x),marker='s') #marcadores, s=square
#[Out]# [<matplotlib.lines.Line2D at 0x7ff36895fee0>]
clf();plot(x,sin(x),marker='c') #marcadores, s=square
get_ipython().run_line_magic('clear', '')
clf();plot(x,sin(x),marker='s') #marcadores, s=square
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37b5a2160>]
clf();plot(x,sin(x),marker='o') 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff369cf1820>]
clf();plot(x,sin(x),marker='^') 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37dddfeb0>]
clf();plot(x,sin(x),marker='^', markersize=5) 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37b377f40>]
clf();plot(x,sin(x),marker='^', markersize=10) 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37ddac400>]
clf();plot(x,sin(x),marker='v', markersize=5) 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37dd7ca60>]
clf();plot(x,sin(x),marker='*', markersize=5) 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff369d2d490>]
clf();plot(x,sin(x),marker='d', markersize=5) 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37b339d90>]
clf();plot(x,sin(x),'mo-') 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37dcab4f0>]
clf();plot(x,sin(x),'mo--') 
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37dc480d0>]
xlim([-5,5])
#[Out]# (-5, 5)
ylim([-2,2])
#[Out]# (-2, 2)
ylim([-5,5])
#[Out]# (-5, 5)
ylim([-1,1])
#[Out]# (-1, 1)
ylim([-2,2])
#[Out]# (-2, 2)
xtics([-pi,-pi/2,0,pi/2,pi])
xticks([-pi,-pi/2,0,pi/2,pi])
#[Out]# ([<matplotlib.axis.XTick at 0x7ff37dce5760>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dce5700>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dc6e070>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dc6e730>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dc6ec40>],
#[Out]#  <a list of 5 Text xticklabel objects>)
grid()
xticks([-pi,-pi/2,0,pi/2,pi], ['$-\pi$','$-\pi/2$','0','$-\pi/2$','$-\pi$'])#codigos de latex
#[Out]# ([<matplotlib.axis.XTick at 0x7ff37dce5760>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dce5700>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dc6e070>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dc6e730>,
#[Out]#   <matplotlib.axis.XTick at 0x7ff37dc6ec40>],
#[Out]#  <a list of 5 Text xticklabel objects>)
get_ipython().run_line_magic('clear', '')
clf()
plot(x,sin(x),label='sinx')
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37dccd190>]
plot(x,cos(x),label='cosx')
#[Out]# [<matplotlib.lines.Line2D at 0x7ff37b597c40>]
legend(loc='upper left)
legend(loc='upper left')
#[Out]# <matplotlib.legend.Legend at 0x7ff37dc8a1c0>
clf()
x=[3,5,8,2,3,6,4,7,3,6,9,4,3,2,6]
hist(x)
#[Out]# (array([2., 4., 2., 0., 1., 3., 0., 1., 1., 1.]),
#[Out]#  array([2. , 2.7, 3.4, 4.1, 4.8, 5.5, 6.2, 6.9, 7.6, 8.3, 9. ]),
#[Out]#  <a list of 10 Patch objects>)
grid()
clf(); hist(x.5)
clf(); hist(x,5) #número de intervalos
#[Out]# (array([6., 2., 4., 1., 2.]),
#[Out]#  array([2. , 3.4, 4.8, 6.2, 7.6, 9. ]),
#[Out]#  <a list of 5 Patch objects>)
clf(); hist(x,5); grid() #número de intervalos
x=linspace(-pi,pi,40)
clf(); fill(x,sin(x))
#[Out]# [<matplotlib.patches.Polygon at 0x7ff37e4bfe50>]
get_ipython().run_line_magic('clear', '')
x=range(6)
x=range(6) #x vale de 0 a 5
y=[3,4,2,6,4,8]
clf(); bar(x,y) #diagrama de barras
#[Out]# <BarContainer object of 6 artists>
clf(); bar(x,y); grid() #diagrama de barras
clf(); barh(x,y); grid() #diagrama de barras horizontal
erroy=[0.0,0.3,0.5,0.1,0.2,0.7]
clf(); errorbar(x,y,erroy)
#[Out]# <ErrorbarContainer object of 3 artists>
clf(); errorbar(x,y,erroy) #para representar incertidumbres
#[Out]# <ErrorbarContainer object of 3 artists>
clf(); errorbar(x,y,erroy,marker='*'); grid() #para representar incertidumbres
clf(); errorbar(x,y,erroy,marker='o'); grid() #para representar incertidumbres
errox=[0.1,0.3,0.3,0.3,0.4,0.1]
clf(); barh(x,y); grid() #diagrama de barras horizontal
clf(); errorbar(x,y,erroy,marker='o'); grid() #para representar incertidumbres
errox=[0.1,0.3,0.3,0.3,0.4,0.1]
clf();errorbar(x,y,errox,erroy,marker='o'); grid()
clf();errorbar(x,y,errox,erroy,marker='o'); grid() #incertidumbre en x e y
#####################CALCULO SIMBOLICO
from sympy import *
x,a,n=symbols('x a n')
x,a,n=symbols('x a n') #los defino como simbolos de sympy
type(x)
#[Out]# sympy.core.symbol.Symbol
init_printing(use_unicode = True)
get_ipython().run_line_magic('clear', '')
f=sin(a*x)/x
f
#[Out]# sin(a⋅x)
#[Out]# ────────
#[Out]#    x    
init_printing(use_unicode = True) #para que se vean bien las funciones
limit(f,x,0) #limite de f cuando x tiende a 0
#[Out]# a
f=1/x
f
#[Out]# 1
#[Out]# ─
#[Out]# x
limit(f,x,0)
#[Out]# ∞
limit(f,x,0,'+')#por la derecha
#[Out]# ∞
limit(f,x,0,'-')#por la derecha
#[Out]# -∞
limit(f,x,0,'-')#por la izquierda
#[Out]# -∞
limit(f,x,0,'+-')#limite direccional
Limit(f,x,0,'-')
#[Out]#      1
#[Out]#  lim ─
#[Out]# x─→0⁻x
Limit(f,x,0,'-') #lo representa por pantalla
#[Out]#      1
#[Out]#  lim ─
#[Out]# x─→0⁻x
Limit(f,x,0,'+-') #lo representa por pantalla
#[Out]#     1
#[Out]# lim ─
#[Out]# x─→0x
Limit(f,x,oo)
#[Out]#     1
#[Out]# lim ─
#[Out]# x─→∞x
limit(f,x,oo)
#[Out]# 0
limit(n**2/(n**2+1),n,oo)
#[Out]# 1
limit(n**2/(n**2+1),n,oo) #limite de una sucesion
#[Out]# 1
f
#[Out]# 1
#[Out]# ─
#[Out]# x
diff(f,x)
#[Out]# -1 
#[Out]# ───
#[Out]#   2
#[Out]#  x 
diff(f,x,2) #segunda derivada
#[Out]# 2 
#[Out]# ──
#[Out]#  3
#[Out]# x 
y=sumbols('y')
y=symbols('y')
f=sin(x*y)
diff(f,x,y)
#[Out]# -x⋅y⋅sin(x⋅y) + cos(x⋅y)
f=exp(-x**2)
f
#[Out]#    2
#[Out]#  -x 
#[Out]# ℯ   
integrate(f,x)
#[Out]# √π⋅erf(x)
#[Out]# ─────────
#[Out]#     2    
integrate(f,(x,0,1))
#[Out]# √π⋅erf(1)
#[Out]# ─────────
#[Out]#     2    
integrate(f,(x,0,1).evalf())#para saber el número
integrate(f,(x,0,1)).evalf()#para saber el número
#[Out]# 0.746824132812427
integrate(1/x,(x,1,oo))
#[Out]# ∞
integrate(1/x**2,(x,1,oo))
#[Out]# 1
integrate(f,(x,-oo,oo))
#[Out]# √π
integrate(f,(x,-oo,oo)).evalf()
#[Out]# 1.77245385090552
solve(a**2*x**2/(a**2+x**2)-1,x) #para resolver ecuaciones
#[Out]# ⎡        ________         ________⎤
#[Out]# ⎢       ╱   1            ╱   1    ⎥
#[Out]# ⎢-a⋅   ╱  ────── , a⋅   ╱  ────── ⎥
#[Out]# ⎢     ╱    2           ╱    2     ⎥
#[Out]# ⎣   ╲╱    a  - 1     ╲╱    a  - 1 ⎦
s=solve(a**2*x**2/(a**2+x**2)-1,x) #para resolver ecuaciones
s[0] #para sacar la primera solucion
#[Out]#         ________
#[Out]#        ╱   1    
#[Out]# -a⋅   ╱  ────── 
#[Out]#      ╱    2     
#[Out]#    ╲╱    a  - 1 
s[1] #para sacar la segunda solucion
#[Out]#        ________
#[Out]#       ╱   1    
#[Out]# a⋅   ╱  ────── 
#[Out]#     ╱    2     
#[Out]#   ╲╱    a  - 1 
s[0].subs([(a,2)])
#[Out]# -2⋅√3 
#[Out]# ──────
#[Out]#   3   
s[0].subs([(a,2)]).evalf()
#[Out]# -1.15470053837925
s[0].subs([(a,2)]).evalf() #sustituyes a por el valor 2
#[Out]# -1.15470053837925
b,c = symbols('b,c')
solve(a*x**2+b*x+c,x)
#[Out]# ⎡        _____________   ⎛       _____________⎞ ⎤
#[Out]# ⎢       ╱           2    ⎜      ╱           2 ⎟ ⎥
#[Out]# ⎢-b + ╲╱  -4⋅a⋅c + b    -⎝b + ╲╱  -4⋅a⋅c + b  ⎠ ⎥
#[Out]# ⎢─────────────────────, ────────────────────────⎥
#[Out]# ⎣         2⋅a                     2⋅a           ⎦
s=solve(a*x**2+b*x+c,x)
s[0].subs([(a,1),(b,1),(c,1)])
#[Out]#   1   √3⋅ⅈ
#[Out]# - ─ + ────
#[Out]#   2    2  
s[0].subs([(a,1),(b,1),(c,1)]).evalf()
#[Out]# -0.5 + 0.866025403784439⋅ⅈ
f=exp(sin(x))
f
#[Out]#  sin(x)
#[Out]# ℯ      
f.series(x,0,5)
#[Out]#          2    4        
#[Out]#         x    x     ⎛ 5⎞
#[Out]# 1 + x + ── - ── + O⎝x ⎠
#[Out]#         2    8         
f.series(x,0,5)#series de Taylor, polinomios de Taylor
#[Out]#          2    4        
#[Out]#         x    x     ⎛ 5⎞
#[Out]# 1 + x + ── - ── + O⎝x ⎠
#[Out]#         2    8         
f.series(x,0,10)#series de Taylor, polinomios de Taylor
#[Out]#          2    4    5     6    7       8     9          
#[Out]#         x    x    x     x    x    31⋅x     x      ⎛ 10⎞
#[Out]# 1 + x + ── - ── - ── - ─── + ── + ───── + ──── + O⎝x  ⎠
#[Out]#         2    8    15   240   90    5760   5670         
series(f,x,0,10)
#[Out]#          2    4    5     6    7       8     9          
#[Out]#         x    x    x     x    x    31⋅x     x      ⎛ 10⎞
#[Out]# 1 + x + ── - ── - ── - ─── + ── + ───── + ──── + O⎝x  ⎠
#[Out]#         2    8    15   240   90    5760   5670         
integrate(1/x,(x,1,oo))
#[Out]# ∞
integrate(1/x**2,(x,1,oo))
#[Out]# 1
Sum(1/n,(n,1,oo))
#[Out]#   ∞    
#[Out]#  ____  
#[Out]#  ╲     
#[Out]#   ╲    
#[Out]#    ╲  1
#[Out]#    ╱  ─
#[Out]#   ╱   n
#[Out]#  ╱     
#[Out]#  ‾‾‾‾  
#[Out]# n = 1  
Sum(1/n,(n,1,oo))#series
#[Out]#   ∞    
#[Out]#  ____  
#[Out]#  ╲     
#[Out]#   ╲    
#[Out]#    ╲  1
#[Out]#    ╱  ─
#[Out]#   ╱   n
#[Out]#  ╱     
#[Out]#  ‾‾‾‾  
#[Out]# n = 1  
Sum(1/n,(n,1,oo)).doit()#series
#[Out]# ∞
Sum(1/n**2,(n,1,oo)).doit()#series
#[Out]#  2
#[Out]# π 
#[Out]# ──
#[Out]# 6 
Sum(1/n**2,(n,1,oo)).evalf()#series
#[Out]# 1.64493406684823
Sum(1/n**1.01,(n,1,oo)).evalf()#series
#[Out]# 0.e+2
##########Matrices
M=Matrix([1,0,1,3],[2,3,4,7],[-1,-3,-3,-4])
M=Matrix([[1,0,1,3],[2,3,4,7],[-1,-3,-3,-4]])
M
#[Out]# ⎡1   0   1   3 ⎤
#[Out]# ⎢              ⎥
#[Out]# ⎢2   3   4   7 ⎥
#[Out]# ⎢              ⎥
#[Out]# ⎣-1  -3  -3  -4⎦
M.rref() #método de Gauss
#[Out]# ⎛⎡1  0   1    3 ⎤        ⎞
#[Out]# ⎜⎢              ⎥        ⎟
#[Out]# ⎜⎢0  1  2/3  1/3⎥, (0, 1)⎟
#[Out]# ⎜⎢              ⎥        ⎟
#[Out]# ⎝⎣0  0   0    0 ⎦        ⎠
#(0,1) son los indices de los pivotes
type(M)
#[Out]# sympy.matrices.dense.MutableDenseMatrix
M=Matrix([[3,-2,4-2],[5,3,-2,-2],[5,-2,2,-2],[5,-2,-3,3]])
M=Matrix([[3,-2,4-2],[5,3,-3,-2],[5,-2,2,-2],[5,-2,-3,3]])
M=Matrix([[3,-2,4-2],[5,3,-3,-2],[5,-2,2,-2],[5,-2,-3,3]])
M=Matrix([[3,-2,4,-2],[5,3,-3,-2],[5,-2,2,-2],[5,-2,-3,3]])
M
#[Out]# ⎡3  -2  4   -2⎤
#[Out]# ⎢             ⎥
#[Out]# ⎢5  3   -3  -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎢5  -2  2   -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎣5  -2  -3  3 ⎦
M.eigenvals()
#[Out]# {-2: 1, 3: 1, 5: 2}
M.eigenvals() #autovalores
#[Out]# {-2: 1, 3: 1, 5: 2}
#devuelve los autovalores con su multiplicidad
M.eigenvects()
#[Out]# ⎡⎛       ⎡⎡0⎤⎤⎞  ⎛      ⎡⎡1⎤⎤⎞  ⎛      ⎡⎡1⎤  ⎡0 ⎤⎤⎞⎤
#[Out]# ⎢⎜       ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥  ⎢  ⎥⎥⎟⎥
#[Out]# ⎢⎜       ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥  ⎢-1⎥⎥⎟⎥
#[Out]# ⎢⎜-2, 1, ⎢⎢ ⎥⎥⎟, ⎜3, 1, ⎢⎢ ⎥⎥⎟, ⎜5, 2, ⎢⎢ ⎥, ⎢  ⎥⎥⎟⎥
#[Out]# ⎢⎜       ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥  ⎢0 ⎥⎥⎟⎥
#[Out]# ⎢⎜       ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥  ⎢  ⎥⎥⎟⎥
#[Out]# ⎣⎝       ⎣⎣1⎦⎦⎠  ⎝      ⎣⎣1⎦⎦⎠  ⎝      ⎣⎣0⎦  ⎣1 ⎦⎦⎠⎦
#muestra los autovalores y los autovectores
M.eigenvects()#autovectores
#[Out]# ⎡⎛       ⎡⎡0⎤⎤⎞  ⎛      ⎡⎡1⎤⎤⎞  ⎛      ⎡⎡1⎤  ⎡0 ⎤⎤⎞⎤
#[Out]# ⎢⎜       ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥  ⎢  ⎥⎥⎟⎥
#[Out]# ⎢⎜       ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥  ⎢-1⎥⎥⎟⎥
#[Out]# ⎢⎜-2, 1, ⎢⎢ ⎥⎥⎟, ⎜3, 1, ⎢⎢ ⎥⎥⎟, ⎜5, 2, ⎢⎢ ⎥, ⎢  ⎥⎥⎟⎥
#[Out]# ⎢⎜       ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥⎥⎟  ⎜      ⎢⎢1⎥  ⎢0 ⎥⎥⎟⎥
#[Out]# ⎢⎜       ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥⎥⎟  ⎜      ⎢⎢ ⎥  ⎢  ⎥⎥⎟⎥
#[Out]# ⎣⎝       ⎣⎣1⎦⎦⎠  ⎝      ⎣⎣1⎦⎦⎠  ⎝      ⎣⎣0⎦  ⎣1 ⎦⎦⎠⎦
v=M.eigenvects()#autovectores
v[0,0]
v[0]
#[Out]# ⎛       ⎡⎡0⎤⎤⎞
#[Out]# ⎜       ⎢⎢ ⎥⎥⎟
#[Out]# ⎜       ⎢⎢1⎥⎥⎟
#[Out]# ⎜-2, 1, ⎢⎢ ⎥⎥⎟
#[Out]# ⎜       ⎢⎢1⎥⎥⎟
#[Out]# ⎜       ⎢⎢ ⎥⎥⎟
#[Out]# ⎝       ⎣⎣1⎦⎦⎠
v[0][0]
#[Out]# -2
v[0][1]
#[Out]# 1
v[0][2]
#[Out]# ⎡⎡0⎤⎤
#[Out]# ⎢⎢ ⎥⎥
#[Out]# ⎢⎢1⎥⎥
#[Out]# ⎢⎢ ⎥⎥
#[Out]# ⎢⎢1⎥⎥
#[Out]# ⎢⎢ ⎥⎥
#[Out]# ⎣⎣1⎦⎦
P,D=M.diagonalize()
P
#[Out]# ⎡0  1  1  0 ⎤
#[Out]# ⎢           ⎥
#[Out]# ⎢1  1  1  -1⎥
#[Out]# ⎢           ⎥
#[Out]# ⎢1  1  1  0 ⎥
#[Out]# ⎢           ⎥
#[Out]# ⎣1  1  0  1 ⎦
D
#[Out]# ⎡-2  0  0  0⎤
#[Out]# ⎢           ⎥
#[Out]# ⎢0   3  0  0⎥
#[Out]# ⎢           ⎥
#[Out]# ⎢0   0  5  0⎥
#[Out]# ⎢           ⎥
#[Out]# ⎣0   0  0  5⎦
M
#[Out]# ⎡3  -2  4   -2⎤
#[Out]# ⎢             ⎥
#[Out]# ⎢5  3   -3  -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎢5  -2  2   -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎣5  -2  -3  3 ⎦
P
#[Out]# ⎡0  1  1  0 ⎤
#[Out]# ⎢           ⎥
#[Out]# ⎢1  1  1  -1⎥
#[Out]# ⎢           ⎥
#[Out]# ⎢1  1  1  0 ⎥
#[Out]# ⎢           ⎥
#[Out]# ⎣1  1  0  1 ⎦
P*D*P**(-1)
#[Out]# ⎡3  -2  4   -2⎤
#[Out]# ⎢             ⎥
#[Out]# ⎢5  3   -3  -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎢5  -2  2   -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎣5  -2  -3  3 ⎦
M
#[Out]# ⎡3  -2  4   -2⎤
#[Out]# ⎢             ⎥
#[Out]# ⎢5  3   -3  -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎢5  -2  2   -2⎥
#[Out]# ⎢             ⎥
#[Out]# ⎣5  -2  -3  3 ⎦
M**-1 #matriz inversa
#[Out]# ⎡1/3  2/15  -4/15  2/15⎤
#[Out]# ⎢                      ⎥
#[Out]# ⎢           -29        ⎥
#[Out]# ⎢5/6  1/3   ────   2/15⎥
#[Out]# ⎢            30        ⎥
#[Out]# ⎢                      ⎥
#[Out]# ⎢           -23        ⎥
#[Out]# ⎢5/6  2/15  ────   2/15⎥
#[Out]# ⎢            30        ⎥
#[Out]# ⎢                      ⎥
#[Out]# ⎢           -29        ⎥
#[Out]# ⎢5/6  2/15  ────   1/3 ⎥
#[Out]# ⎣            30        ⎦
M*M**-1
#[Out]# ⎡1  0  0  0⎤
#[Out]# ⎢          ⎥
#[Out]# ⎢0  1  0  0⎥
#[Out]# ⎢          ⎥
#[Out]# ⎢0  0  1  0⎥
#[Out]# ⎢          ⎥
#[Out]# ⎣0  0  0  1⎦
M.det_LU_decomposition()
#[Out]# -150
M.det()
#[Out]# -150
p=x**4-5*x**3+2*x**2+20*x-24
p
#[Out]#  4      3      2            
#[Out]# x  - 5⋅x  + 2⋅x  + 20⋅x - 24
p=x**4-5*x**3+2*x**2+20*x-24 #polinomio
roots(p)
#[Out]# {-2: 1, 2: 2, 3: 1}
(x+2)**2*(x-2)*(x-3)
#[Out]#                        2
#[Out]# (x - 3)⋅(x - 2)⋅(x + 2) 
p
#[Out]#  4      3      2            
#[Out]# x  - 5⋅x  + 2⋅x  + 20⋅x - 24
roots(p)
#[Out]# {-2: 1, 2: 2, 3: 1}
expand((x+2)*(x-2)**2*(x-3))
#[Out]#  4      3      2            
#[Out]# x  - 5⋅x  + 2⋅x  + 20⋅x - 24
solve(p,x)
#[Out]# [-2, 2, 3]
#para calcular las raices del polinomio
factor(p)
#[Out]#                2        
#[Out]# (x - 3)⋅(x - 2) ⋅(x + 2)
factor(p) #factoriza p
#[Out]#                2        
#[Out]# (x - 3)⋅(x - 2) ⋅(x + 2)
roots(x**2+1)
#[Out]# {-ⅈ: 1, ⅈ: 1}
s=roots(x**2+1)
s[0]
type(s)
#[Out]# dict
s(0)
dict -help
dict().popitem(0)
dict().popitem()
get_ipython().run_line_magic('clear', '')
zeros[]
zeros[3]
zeros(3)
#[Out]# ⎡0  0  0⎤
#[Out]# ⎢       ⎥
#[Out]# ⎢0  0  0⎥
#[Out]# ⎢       ⎥
#[Out]# ⎣0  0  0⎦
get_ipython().run_line_magic('clear', '')
ones(3,6)
#[Out]# ⎡1  1  1  1  1  1⎤
#[Out]# ⎢                ⎥
#[Out]# ⎢1  1  1  1  1  1⎥
#[Out]# ⎢                ⎥
#[Out]# ⎣1  1  1  1  1  1⎦
eye(3)
#[Out]# ⎡1  0  0⎤
#[Out]# ⎢       ⎥
#[Out]# ⎢0  1  0⎥
#[Out]# ⎢       ⎥
#[Out]# ⎣0  0  1⎦
f=x**2
diff(f,x)
#[Out]# 2⋅x
f.subs([x,1])
f.subs([(x,1)])
#[Out]# 1
f=lambdify(x,x**2)
f(2)
#[Out]# 4
#para funciones que queramos 'llamar'
f=lambdify((x,y),sin(x*y))
f(1,2)
#[Out]# 0.9092974268256817
exit()
