#!/usr/bin/python3
from tkinter import *
from math import *
fields=('a','b','c',u'Solución')
def calcular(entries):
	a=float(entries['a'].get())
	b=float(entries['b'].get())
	c=float(entries['c'].get())
	if a==0:
		if b==0:
			if c==0:
				solucion='IR'
			else:
				solucion='Ø'
		else:
			solucion='%.3f'%(-c/b)
	else:
		d=b*b-4*a*c;a2=2*a;rd=sqrt(abs(d))
		if d<0:
			re=-b/a2;im=rd/a2;
			solucion='x=%.3f +- I*%.3f'%(re,abs(im))
		elif d==0:
			solucion='x1=x2=%.3f'%(-b/a2)
		else:
			solucion='x1=%.3f x2=%.3f'%((-b-rd)/a2,(-b-rd)/a2)
	entries[u'Solución'].delete(0,END)	
	entries[u'Solución'].insert(0,solucion)		

def makeform(root, fields):
	entries = {}
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=8, text=field+": ", anchor='w')
		ent = Entry(row)
		ent.insert(0,"1")
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries[field] = ent
	return entries

if __name__ == '__main__':
	root = Tk()
	root.title(u'Ecuación de 2º grao')
	ents = makeform(root, fields)
	b1 = Button(root, text='Calcular',
			command=(lambda e=ents: calcular(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()
