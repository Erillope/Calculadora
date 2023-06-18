import sympy as sp
import numpy as np
from calculadora.arreglos import Vector

class Funcion:
    def __init__(self, expresion, variable):
        self.expresion = str(sp.simplify(expresion))
        self.list_expresion = self.expresion.split(',')
        self.name_variable = np.array(variable)
        self.variable = []
        self.dim_dominio = len(variable)
        self.dim_imagen = len(self.list_expresion)
        self.eval = sp.simplify(expresion)

        for i in range(self.dim_dominio):
            self.variable.append(sp.symbols(self.name_variable[i]))

    def get_expresion(self):
        return self.expresion
    
    def get_name_variable(self):
        return self.name_variable

    def get_variable(self):
        return self.variable
        
    def get_dim_dominio(self):
        return self.dim_dominio
        
    def get_dim_imagen(self):
        return self.dim_imagen

    def evaluar(self, arg):
        argumento = np.transpose(np.array([self.variable, arg]))
        result = self.eval.subs(argumento)
        return Vector(result)

    def evaluar_vector(self, vector):
        arg = vector.get_coord()
        argumento = np.transpose(np.array([self.variable, arg]))
        result = self.eval.subs(argumento)
        return Vector(result)
    
    def composicion(self, funcion):
        v = Vector(funcion.get_variable())
        f_vector = self.evaluar_vector(funcion(v))
        lista_expresiones = []
        for expresion in f_vector:
            lista_expresiones.append(str(expresion))
        
        expresion = ', '.join(lista_expresiones)
        return Funcion(expresion, funcion.get_name_variable())

    def nuevo_objeto(self, expresion, variable):
        return Funcion(expresion, variable)

    def __call__(self, *arg):
        if type(arg[0]) == Funcion:
            return self.composicion(arg[0])
        
        elif type(arg[0]) == Vector:
            return self.evaluar_vector(arg[0])

        else:
            return self.evaluar(arg)
    
    def __str__(self):
        return self.expresion
    
    def __add__(self, funcion):
        exp1 = sp.simplify(self.expresion)
        exp2 = sp.simplify(funcion.get_expresion())

        new_exprecion = np.array(exp1) + np.array(exp2)
        new_variable = np.concatenate((self.name_variable, funcion.get_name_variable()))
        new_variable = np.unique(new_variable)
        
        return self.nuevo_objeto(new_exprecion, new_variable)
    
    def __sub__(self, funcion):
        exp1 = sp.simplify(self.expresion)
        exp2 = sp.simplify(funcion.get_expresion())

        new_exprecion = np.array(exp1) - np.array(exp2)
        new_variable = np.concatenate((self.name_variable, funcion.get_name_variable()))
        new_variable = np.unique(new_variable)
        
        return self.nuevo_objeto(new_exprecion, new_variable)
        




        
