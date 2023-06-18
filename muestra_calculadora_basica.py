from calculadora.calculadoras import Calculadora

def main():
    calculadora = Calculadora()
    exp1 = '3 + 5*(pi) - e'
    resutl1 = calculadora.eval(exp1)
    print(f'{exp1} = {resutl1}')

    calculadora.add_constante('a', 4.3)
    calculadora.add_constante('m', 0.1)
    exp2 = 'a + (a-m)*(pi) - e'
    resutl2 = calculadora.eval(exp2)
    print(f'{exp2} = {resutl2}')

    print(calculadora.get_constantes())
    calculadora.delete_constante('a')
    print(calculadora.get_constantes())


main()