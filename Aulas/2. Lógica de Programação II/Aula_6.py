#-----------------------------------------------------------------------------------------------------------------------------------#
# Faça uma calculadora que receba expressões aritméticas simples. A expressão deve conter dois operandos com um operador entre eles, 
# de acordo com o exemplo:
# ```py
# Entrada: 10 + 20
# Saída: 30

# Entrada: 2 ^ 4
# Saída: 16
# ```
# Faça o tratamento de erros para quando a entrada não estiver no formato adequado, os dados de entrada não forem dados válidos ou o 
# operador for inválido. Ao final, mostre a saída da operação.

def soma (a, b):
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    return a/b

def exponenciacao(a,b):
    return a**b

def calcula(a, operador, b):
    operacoes = {'+':soma, '-':subtracao, '*':multiplicacao, '/':divisao, '^':exponenciacao}

    try:
        a = float(a)
        b = float(b)

        if a == 0 and b == 0 and operador == '^':
            print('0 ^ 0 é uma indeterminação matemática!')
            return

        print(f'Saída: {operacoes[operador](a,b)}')

    except ValueError:
        print(f'Os valores ({a} e {b}) informados devem ser numéricos')

    except KeyError:
        print(f'O operador {operador} informado não foi encontrado. Operadores disponíveis: | + | - | * | / | ^ |')
    
    except ZeroDivisionError:
        print(f'Não é possível dividir por 0 na operação: {a} / {b}')

    finally:
        return
    

print('\'exit\' - para sair')
entrada = input('Entrada: ').split()
while entrada[0].lower() != 'exit':
    try:
        calcula(*entrada)
    except TypeError:
        print('A entrada informada não é válida. (Formato padrão aceito: \'número operador número\' - Ex: 2 + 2)')
    entrada = input('Entrada: ').split()