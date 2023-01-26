#-----------------------------------------------------------------------------------------------------------------------------------#
# 1 Faça um programa que pede para a usuária digitar dois números, inicio e fim.
# O seu programa deverá preencher uma lista com todos os números no intervalo (inclusive os valores inicial e final) e exibi-la na tela.

inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor de fim: '))

valores = []

for i in range(inicio, fim+1):
    valores.append(i)
print(valores)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2 Faça um programa que preenche uma lista inicialmente vazia com 20 números aleatórios entre 0 e 100.
# Você pode utilizar a biblioteca random para isso. Comece importando-a no início de seu código:
# import random
# Para sortear um número, você pode usar a linha abaixo:
# sorteio = random.randint(0, 100)

import random

numeros = []
numeros = [random.randint(0, 100) for i in range(20)]
print(numeros)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3 Faça um programa que percorre uma lista de números aleatórios (ver exercício 2) e exibe na tela apenas os números pares.

import random

numeros = [random.randint(0, 100) for i in range(20)]

for numero in numeros:
   if numero % 2 == 0:
       print(numero, end=' ')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4 Faça um programa que calcula a média dos números de uma lista numérica.

import random

numeros = [random.randint(0, 100) for i in range(20)]

media = sum(numeros)/len(numeros)
print(numeros)
print(f'Média: {media}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5 Faça um programa que percorre uma lista de números. Os números abaixo da média dos valores deverão ser inseridos em uma lista, e 
# os valores acima da média deverão ser inseridos em outra lista.

import random

numeros = [random.randint(0, 100) for i in range(20)]

media = sum(numeros)/len(numeros)

acima_media = [n for n in numeros if n > media]
abaixo_media = [n for n in numeros if n < media]

print(numeros)
print(f'Média: {media}')
print(f'Acima da média: {acima_media}')
print(f'Abaixo da média: {abaixo_media}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6 Faça um programa que pergunta o número de atividades avaliativas realizadas pela usuária (no mínimo 4).
# O programa deverá exibir:
# a menor nota
# a maior nota
# a média calculada desconsiderando a maior e a menor nota

n_notas = 0
notas = []

while n_notas <= 4:
    n_notas = int(input('Digite o número de atividades avaliativas realizadas (mímino de 4): '))

for i in range(n_notas):
    notas.append(float(input(f'Digite a nota da {i+1}ª prova: ')))

print('Notas - ', notas)

menor_nota = min(notas)
maior_nota = max(notas)
notas.remove(menor_nota)
notas.remove(maior_nota)
media = sum(notas)/len(notas)

print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')
print(f'Média: {media:.2f}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7 Faça um programa que leia as coordenadas de dois vetores a partir do teclado e armazene-as em listas.
# O seu programa deverá realizar a soma vetorial.

len_vetor = int(input('Digite quantas coordenadas o vetor terá: '))

vetor1 = [int(input(f'Digite a {i+1}ª coordenada vetorial do vetor 1: ')) for i in range(len_vetor)]
vetor2 = [int(input(f'Digite a {i+1}ª coordenada vetorial do vetor 2: ')) for i in range(len_vetor)]
soma_vetorial = [vetor1[i] + vetor2[i] for i in range(len_vetor)]

print('Vetor 1:', vetor1)
print('Vetor 2:', vetor2)
print('Soma vetorial:', soma_vetorial)
    

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8 Faça um programa que leia as coordenadas de dois vetores a partir do teclado e armazene-as em listas.
# O seu programa deverá realizar o produto escalar. 

len_vetor = int(input('Digite quantas coordenadas o vetor terá: '))

vetor1 = [int(input(f'Digite a {i+1}ª coordenada vetorial do vetor 1: ')) for i in range(len_vetor)]
vetor2 = [int(input(f'Digite a {i+1}ª coordenada vetorial do vetor 2: ')) for i in range(len_vetor)]
produto_escalar = [vetor1[i] * vetor2[i] for i in range(len_vetor)]

print('Vetor 1:', vetor1)
print('Vetor 2:', vetor2)
print('Produto escalar:', sum(produto_escalar))

#-----------------------------------------------------------------------------------------------------------------------------------#
# 9 Crie uma tabela de preços (pode ser fixa no seu código) usando lista de listas.
# Ela pode ser implementada da seguinte maneira: cada "lista interna" é uma lista de 2 elementos: na posição 0 temos o nome do produto, 
# na posição 1 temos o preço.
# Faça um programa que permita consultar valores na lista.
# Ele deverá perguntar para a usuária o nome do produto que ela deseja consultar. Caso o produto exista na lista, seu preço será exibido.
# Caso contrário, a mensagem "produto não encontrado" será exibida.
# O programa deverá repetir a pergunta após mostrar o resultado, até que a usuária digite "sair".

produtos = [
    ['Chocolate', 5.12],
    ['Doritos', 15.25],
    ['Fandangos', 7.54],
]

produto_nome = ''
while produto_nome.lower() != 'sair':
    produto_nome = input('Digite o nome do produto que deseja consultar: ')
    for produto in produtos:
        if produto_nome.lower() in produto[0].lower():
            print(f'O preço do produto {produto[0]} é: {produto[1]}')
            break
    else:
        print('Produto não encontrado')
            

#-----------------------------------------------------------------------------------------------------------------------------------#
# 10 Vamos fazer um programa para representar uma aluna em formato amigável para salvar em uma tabela ou banco de dados.

# Peça para a usuária digitar:

# o nome da aluna
# o número de matrícula
# a quantidade de provas realizadas
# a nota de cada uma das provas
# o percentual de presenças
# A aluna deverá ser representada em uma lista obedecendo a seguinte estrutura:

# índice 0: número de matrícula
# índice 1: nome
# índice 2: uma lista com todas as suas notas
# índice 3: sua média
# índice 4: seu percentual de presenças
# índice 5: um booleano indicando se a aluna foi aprovada ou reprovada
# Considere como critério de aprovação nota maior ou igual a 6.0 e presença igual ou superior a 70%.

aluna = []
notas = []

aluna.insert(1, input('Digite o nome da Aluna: '))
aluna.insert(0, int(input('Digite seu número de matrícula: ')))

n_provas = int(input('Digite o número de provas realizadas: '))

for i in range(n_provas):
    notas.append(float(input(f'Digite a nota da {i+1}ª prova: ')))

presenca = float(input('Digite o percentual (%) de presenças: '))

media = sum(notas)/len(notas)

aluna.append(notas)
aluna.append(media)
aluna.append(presenca)

if media >= 6.0 and presenca >= 70:
    aluna.append(True)
else:
    aluna.append(False)

print(aluna)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 11 Questão avaliada
# Nesta questão, reaproveite o código da questão avaliada da lista de exercícios anterior!
# Modifique seu código para, ao invés de exibir a tabela Price na tela, armazenar a tabela utilizando uma lista de listas.
# Cada "lista interna" deve conter juros daquele mês, amortização daquele mês, valor da prestação e saldo devedor.
# Todas essas listas deverão ser adicionadas, na ordem correta, em uma lista geral, que será nossa tabela.
# Uma vez criada e calculada toda a tabela, pergunte (em loop) para a usuária qual mês ela deseja consultar e mostre para ela 
# quanto de juros serão pagos, quanto será amortizado e qual será o seu saldo devedor naquele mês. Caso ela digite um mês inválido, 
# informe para ela que aquele mês não existe. Caso ela digite um mês negativo, encerre o programa.

tabela = []

pv = float(input('Informe o valor do empréstimo: '))
i = float(input('Informe a taxa de juros (%): '))/100
n = int(input('Informe o tempo para pagamento (meses): '))

p = pv * ((((1+i)**n) * i) / (((1+i)**n) - 1))

for parcela in range(n):

    j = i*pv
    a = p-j
    pv = pv-a

    tabela.append([j, a, p, pv])

mes = 0

while mes >= 0:
    mes = int(input('Informe o mês que deseja consultar (Numero negativo para encerrar): '))
    if mes <= len(tabela) and mes > 0:
        print(f'| Mês {mes} | J: {tabela[mes-1][0]:.2f} | A: {tabela[mes-1][1]:.2f} | Pgto: {tabela[mes-1][2]:.2f} | Deve: {tabela[mes-1][3]:.2f} |\n')
    else:
        print('Mês não encontrado')
else:
    print('FIM')