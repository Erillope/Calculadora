import numpy as np

class Calculadora:
    def __init__(self):
        self.constantes = {'pi': np.pi, 'e': np.e}
        self.variables_locales = {}
        self.set_variables()

    #Getters
    def get_constantes(self):
        return self.constantes

    #Setters
    def add_constante(self, name, valor):
        self.constantes[name] = valor
        self.set_variables()

    def set_variables(self):
        self.variables_locales.update(self.constantes)
    
    #Deleters
    def delete_constante(self, name):
        del self.constantes[name]
        del self.variables_locales[name]
    
    #Cálculos
    def eval(self, expresion):
        #Evalúa expreciones
        return eval(expresion, self.variables_locales)