from calculadora.calculadoras import Calculadora
from calculadora.funciones import Funcion
from calculadora.arreglos import Vector
import sympy as sp
import numpy as np

def main():
    exp1 = "x+y+z-t"
    exp2 = "2*x + y**2 + z+t"
    exp3 = "x**2 + y**2 + z**2 + t**2"
    exp4 = 'x'
    exp = f'{exp1}, {exp2}, {exp3}, {exp4}'
    variables = ['x', 'y', 'z', 't']
    f = Funcion(exp, variables)
    exp1 = 'u+v'
    exp2 = 'v**2'
    exp3 = 'v**2 - u**2'
    exp4 = '(u+v)**2'
    exp = f'{exp1}, {exp2}, {exp3}, {exp4}'
    g = Funcion(exp, ['u', 'v'])
    v = Vector(g.get_variable())
    h = f(g)
    a = np.array([5, 7])
    b = np.array([2, 4])
    
    print(f(1,2,3,4))
    print((f+f)(1,2,3,4))
    
    

main()