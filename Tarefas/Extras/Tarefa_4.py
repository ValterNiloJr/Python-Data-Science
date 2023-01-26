#-----------------------------------------------------------------------------------------------------------------------------------#
# 1 Faça um programa que pede para o usuário digitar um número. O programa deverá utilizar um laço do tipo for para exibir a tabuada 
# daquele número.

numero = int(input('Digite um número: '))
for i in range(1, 11):
   print(f'{numero} x {i} = {numero * i}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2 Faça um programa que pede para o usuário digitar um número inteiro positivo. Seu programa deverá utilizar um laço do tipo for para 
# responder a soma de do número com todos os seus antecessores positivos.
# Ex: se o número digitado for 5, a conta a ser realizada será 5 + 4 + 3 + 2 + 1, e o resultado na tela será "15".

numero = int(input('Digite um número inteiro positivo: '))
soma = 0
for i in range(numero):
   soma = soma + (numero - i)
print(soma)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3 Faça um programa que pede para o usuário digitar um número inteiro positivo. O programa deverá utilizar um laço do tipo for para 
# calcular e exibir na tela o fatorial do número digitado.
# Lembrete: o fatorial de um número "n", denotado por "n!", é o produto dele com todos os seus antecessores inteiros positivos.
# Ex: 5! = 1 x 2 x 3 x 4 x 5

numero = int(input('Digite um número inteiro positivo: '))
fatorial = 1
for i in range(numero):
   fatorial = fatorial * (numero - i)
print(fatorial)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4 Faça um programa que pergunta quantas provas o usuário fez. Em seguida, o programa deverá utilizar um laço for para ler cada uma 
# de suas notas pelo teclado e informar sua média.

n_provas = int(input('Digite a quantidade de provas feitas: '))

nota = 0

for i in range(n_provas):
   nota = nota + float(input(f'Informe a nota da prova {i+1}: '))

print(f'A média final é: {(nota / n_provas):.2f}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5 Uma progressão aritmética (PA) possui uma razão e um termo inicial.
# Podemos chamar o termo inicial de termo 0.
# Um termo "n" qualquer pode ser obtido somando a razão "n" vezes ao termo inicial.
# Por exemplo, a PA com razão = 4 e termo inicial = 1 terá os seguintes termos:
# 1, 5, 9, 13, 17, 21, 25...
# onde 1 é o termo 0, 5 é o termo 1, 9 é o termo 2, e assim sucessivamente.
# Faça um programa que pergunta para o usuário:
# a razão de uma PA
# o termo inicial da PA
# quantos termos ela gostaria de ver na tela
# O seu programa deverá calcular e exibir os "n" termos solicitados pela usuário.

r = int(input('Informe a razão da PA: '))
a1 = int(input('Digite o primeiro termo da PA: '))
an = int(input('Digite quantos termos da PA gostaria de ver na tela: '))

pa = []

for n in range(an):
    pa.append(a1 + (n * r))

print(pa)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6 Uma progressão geométrica (PG) possui uma razão e um termo inicial.
# Podemos chamar o termo inicial de termo 0.
# Um termo "n" qualquer pode ser obtido multiplicando a razão "n" vezes ao termo inicial.
# Por exemplo, a PA com razão = 2 e termo inicial = 3 terá os seguintes termos:
# 3, 6, 12, 24, 48, 96...
# onde 3 é o termo 0, 6 é o termo 1, 12 é o termo 2, e assim sucessivamente.
# Faça um programa que pergunta para a usuária:
# a razão de uma PG
# o termo inicial da PG
# quantos termos ela gostaria de ver na tela
# O seu programa deverá calcular e exibir os "n" termos solicitados pela usuária.

r = int(input('Informe a razão da PG: '))
a1 = int(input('Digite o primeiro termo da PG: '))
an = int(input('Digite quantos termos da PG gostaria de ver na tela: '))

pg = []

for n in range(an):
   pg.append(a1*(r**(n)))

print(pg)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7 A sequência de Fibonacci é definida da seguinte maneira:
# Termo(0) = 1
# Termo(1) = 1
# Termo(n) = Termo(n-1) + Termo(n-2)
# Ou seja, temos 2 termos iniciais que valem 1, e o restante dos termos é definido pela soma dos dois antecessores. Os primeiros termos da 
# sequência são:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# Note que qualquer termo da sequência equivale à soma dos dois antecessores.
# Faça um programa que pergunta para a usuária quantos termos da sequência de Fibonacci ela gostaria de ver. O seu programa deverá calcular 
# e exibir a quantidade de termos desejada por ela.

an = int(input('Digite quantos termos da sequência de Fibonacci gostaria de ver na tela: '))
fibonacci = [1, 1]
for n in range(2, an):
   fibonacci.append((fibonacci[n-1]) + (fibonacci[n-2]))
print(fibonacci)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8 A constante π (leia "pi"), que representa a relação entre o comprimento de uma circunferência e o seu diâmetro, possui valor aproximado 
# de 3.14159265.
#Acredita-se que ele possui infinitas casas após o ponto decimal, sem repetição. Isso nos impede de determinar seu valor exato, mas há várias 
# técnicas diferentes para calcular aproximações arbitrariamente boas.
#Muitas dessas técnicas envolvem calcular a soma de sequências convergentes, isto é, sequências onde conforme somamos mais termos seguindo 
# alguma regra, mais ela se aproxima de um valor específico.
#Uma dessas técnicas é a Fórmula de Leibniz:
#Note que existe uma regra fácil de deduzir para quais seriam os próximos denominadores e sinais. Quanto mais termos forem acrescentados, 
# mais a soma se aproxima de π/4. Portanto, ao calcularmos essa soma com milhares ou milhões de termos e multiplicarmos o resultado por 4, 
# devemos ter uma boa aproximação de π.
#Faça um programa que pergunta para o usuário com quantos termos ele gostaria de fazer a conta. Seu programa deverá calcular π utilizando a 
# fórmula de Leibniz com a quantidade de termos especificada pelo usuário.
#Desafio: quando seu programa estiver pronto, experimente alguns valores e veja quantos termos são necessários para determinar o valor de π 
# com uma precisão que você considere satisfatória.

an = int(input('Digite quantos termos gostaria de usar para calcular π: '))

pi = 0

for n in range(an):
   pi = pi + ((-1) ** n) / (2*n + 1)

pi = pi * 4
print(pi)
#1000000 é um bom valor

#-----------------------------------------------------------------------------------------------------------------------------------#
# 9 Faça um programa que pergunta a quantidade de provas realizadas pelo usuário.
# O seu programa deverá ler as notas das provas pelo teclado e responder:
# a média das provas
# a maior nota
# a menor nota

n_provas = int(input('Digite a quantidade de provas feitas: '))

notas = []

for i in range(n_provas):
   notas.append(float(input(f'Informe a nota da prova {i+1}: ')))

print(f'A média final é: {(sum(notas)/len(notas)):.2f}')
print(f'A maior nota é: {max(notas)}')
print(f'A menor nota é: {min(notas)}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 10 Faça um programa que pede para o usuário digitar uma base e um expoente.
# O seu programa deverá responder o resultado da operação de potência entre os números digitados sem utilizar o operador ** do Python.

base = int(input('Digite a base: '))
exp = int(input('Digite o expoente: '))

pot = 1

for i in range(exp):
   pot = pot * base

print(pot)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 11 Questão Avaliada
# Vamos implementar uma Tabela Price.
# A tabela Price é utilizada em empréstimos de longo prazo, como no financiamento de um imóvel.
# Um empréstimo pelo sistema Price utiliza prestações com valor fixo, isto é, você sempre irá pagar o mesmo valor todo mês.
# Porém, uma taxa de juros corrige o seu saldo devedor, sendo assim, parte do valor que você paga no mês serve apenas para pagar juros, 
# e outra parte realmente reduz o seu sald devedor. Essa redução é a chamada amortização.
# Como o saldo devedor diminui com o tempo, a parcela de juros diminui a cada mês, nos primeiros meses a maior parte do valor pago por 
# mês serve para pagar juros, enquanto mais próximo do final, a maior parte do valor está de fato amortizando a dívida.
# Você pode aprender mais sobre as colunas da tabela e o cálculo para determinar o valor das prestações neste site.
# Conhecendo o valor fixo, como fazemos para determinar quanto de amortização, quanto de juros e qual o novo saldo devedor a cada mês?
# Primeiro aplica-se a taxa de juros sobre o saldo devedor (multiplicar por i). Esse valor é o valor de juros pagos no mês. Subtraindo-se 
# os juros do valor da prestação, descobre-se o quanto se amortizou naquele mês. O novo saldo devedor é obtido subtraindo a amortização do valor.
# Faça um programa que pergunta:
# o valor de um empréstimo
# a taxa de juros do empréstimo
# o tempo para pagamento
#O seu programa deverá imprimir na tela uma "tabela" mostrando, mês a mês, o saldo devedor, juros, amortização e o valor da prestação.

pv = float(input('Informe o valor do empréstimo: '))
i = float(input('Informe a taxa de juros (%): '))/100
n = int(input('Informe o tempo para pagamento (meses): '))

p = pv * ((((1+i)**n) * i) / (((1+i)**n) - 1))

print('\n---------------------------------------------------------------------------------')

for parcela in range(n):
    j = i*pv
    a = p-j
    pv = pv-a
    print(
        f'| Parcela {parcela+1}\t| J: {j:.2f}\t| A: {a:.2f}\t| Pgto: {p:.2f}\t| Deve: {pv:.2f}\t|')

print('---------------------------------------------------------------------------------')
