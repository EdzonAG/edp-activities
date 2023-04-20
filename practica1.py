import numpy as np
import sympy as sp

def adeltante(fun,x,h):
    ad = (fun(x+h)-fun(x))/h
    return ad

def atras(fun,x,h):
    at = (fun(x)-fun(x-h))/h
    return at

def centrada(fun,x,h):
    c = (fun(x+h)-fun(x-h))/(2*h)
    return c

def real(fun,p):
    x = sp.symbols('x')
    expr = sp.simplify(fun(x))
    der = expr.diff(x)
    dif = der.subs(x,p)
    return dif.evalf()

fun = [lambda x: x/np.sqrt(x**2+9), lambda x: x**3/(x**2+1), lambda x: np.log(np.cos(x) + np.sin(x)), lambda x: np.exp(x)*np.cos(x)]
funr = [lambda x: x/sp.sqrt(x**2+9), lambda x: x**3/(x**2+1), lambda x: sp.log(sp.cos(x) + sp.sin(x)), lambda x: sp.exp(x)*sp.cos(x)]
x = [3, 2, np.pi/2, np.pi]
h = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

for i in h:
    print(f'---PARA H = {i}:---\n')
    for j in range(4):
        print(f'Funcion {j+1}\n\nHacia Adelante = {adeltante(fun[j],x[j],i)}\nHacia Atras = {atras(fun[j],x[j],i)}\nCentrada = {centrada(fun[j],x[j],i)}\n\nValor Real = {real(funr[j],x[j])}\n')