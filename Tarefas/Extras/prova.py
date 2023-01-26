#-----------------------------------------------------------------------------------------------------------------------------------#
# 2 Capacitores são componentes eletrônicos capazes de temporariamente armazenar carga.
# A grandeza que mede sua capacidade de armazenar carga é chamada de capacitância.
# Há duas maneiras de ligar dois capacitores em um circuito: em série, quando conectamos um terminal de um deles com um terminal de outro, 
# ou em paralelo, quando ligamos ambos os terminais um no outro
# Em ambos os casos, podemos imaginar ambos os capacitores se comportando como um único capacitor com uma capacitância diferente. Porém, 
# a forma de calcular a resistência equivalente é diferente para capacitores em série ou em paralelo.
# Em série a capacitância equivalente é dada por:
# cp = c1 + c2
# Em paralelo a capacitância equivalente é dada por:
# (c1*c2)/(c1+c2)
# A quantidade de carga de um capacitor é dada pela equação:
# Q = CV
# Onde C é a capacitância, e V é a tensão (representada nas imagens acima por uma fonte de tensão).
# Faça um programa que pergunta a capacitância de dois capacitores diferentes e a tensão da fonte. Seu programa deverá responder a 
# capacitância equivalente caso os capacitores sejam ligados em série, a capacitância equivalente caso eles sejam ligados em paralelo e a 
# quantidade de carga que o par de capacitores conseguirá armazenar em cada um dos casos.

c1 = float(input('Digite o valor de Capacitância do capacitor 1: '))
c2 = float(input('Digite o valor de Capacitância do capacitor 2: '))
v = float(input('Digite o valor da fonte de tensão: '))

# Em paralelo
cp = c1 + c2
qp = cp * v

# Em série
cs = (c1*c2)/(c1+c2)
qs = cs * v

print('Em paralelo:')
print(f'Cp = {cp:.2f}')
print(f'Qp = {qp:.2f}')
print('Em série:')
print(f'Cs = {cs:.2f}')
print(f'Qs = {qs:.2f}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3 Considere o código em Python abaixo:

for x in range(1, 40):
   if x % 2 == 0 and x % 11 == 0:
       print('comando1')
   if x % 17 == 0 and x % 3 == 0:
       print('comando2')
   if x % 17 == 0 and x % 2 == 0:
       print('comando3')

# Qual ou quais comandos serão executados?

# Alternativas

# comando1 e comando 3 X
# comando3
# comando1
# comando1 e comando2
# comando2 e comando3
# Nenhum dos 3
# comando2
# comando1, comando2 e comando3

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4 O jogo Pedra-Tesoura-Papel-Lagarto-Spock é uma expansão do tradicional jogo jokenpo popularizada pelo seriado The Big Bang Theory.
# As regras são bastante simples. Veja...
# Os jogadores devem simultaneamente anunciar sua jogada dentre as 5 opções. O vencedor é determinado pela relação entre as jogadas:

# Tesoura corta o papel
# Papel cobre a pedra
# Pedra esmaga o lagarto
# Lagarto envenena o Spock
# Spock quebra a tesoura
# Tesoura decapita o lagarto
# Lagarto come o papel
# Papel refuta o Spock
# Spock vaporiza a pedra
# e, como sempre...
# Pedra quebra a tesoura

# Faça um programa que pede para o usuário digitar uma das 5 opções (pedra, tesoura, papel, lagarto ou spock). Em seguida, seu programa deverá sortear uma jogada aleatória para o computador. Seu programa deverá imprimir na tela a jogada do computador e o resultado:

# "Você venceu!"
# "Você perdeu!"
# "Empate!"

import random

sorteio = random.randint(1, 5)

# cada lista contém a condições de vitória ou derrota para cada interação
# ex: 1-Pedra vs 2-Tesoura >> Pedra ganha (2, True)
#     1-Pedra vs 3-Papel   >> Pedra perde (3, False)
pedra = [[2, True], [4, True], [3, False], [5, False]]
tesoura = [[3, True], [4, True], [1, False], [5, False]]
papel = [[5, True], [1, True], [2, False], [4, False]]
lagarto = [[5, True], [3, True], [1, False], [2, False]]
spock = [[1, True], [2, True], [3, False], [4, False]]

condicoes = [pedra] + [tesoura] + [papel] + [lagarto] + [spock]

print('| 1 - Pedra | 2 - Tesoura | 3 - Papel | 4 - Lagarto | 5 - Spock |')
opcao = int(input('Escolha um número das opções acima: ')) - 1

for condicao in condicoes[opcao]:
   if condicao[0] == sorteio and condicao[1] == True:
       print('Você venceu!')
       break
   elif condicao[0] == sorteio and condicao[1] == False:
       print('Você perdeu!')
       break
else:
   print('Empate!')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5 O valor da raiz quadrada de um número positivo x pode ser aproximado pelo método da bissecção. Ele funciona da seguinte maneira:
# Escolha 2 números, i e f, tal que a raiz quadrada de x com certeza esteja contida no intervalo [i, f].
# Escolha a precisão e desejada.
# Enquanto f - i for maior do que e, repita os seguintes passos:
# - Encontre o valor "m" que representa o meio do intervalo.
# - Se m² > x, "f" recebe "m". Caso contrário, "i" recebe "m".
# Ao final do loop, a variável "m" contém a aproximação calculada para a raiz quadrada do número.
# A precisão e tipicamente é um número bem pequeno, como 0.0001 ou 0.00001.
# Implemente um programa que pede para o usuário digitar um número e a precisão aceitável.
# Seu programa deverá calcular e responder a raiz quadrada com a precisão desejada utilizando o método da bissecção.
# Você pode considerar que o usuário sempre irá digitar números inteiros positivos.

# Dica: para determinar o intervalo, faça a si mesmo as seguintes perguntas:
# 1) Qual número sempre será inferior à raiz quadrada de qualquer inteiro positivo? 2) Qual número sempre será superior à raiz quadrada de um número dado?

x = int(input('Digite um número inteiro positivo: '))
e = float(input('Digite a precisão: '))

i = 0
f = x

while (f - i) > e:
    m = f - (f - i) / 2
    if (m**2) > x:
        f = m
    else:
        i = m

print(f'A raíz quadrada de {x} pelo método da bissecção é: {m}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6 Em estatística, frequentemente descrevemos um conjunto de amostras utilizando alguma medida de tendência central, como a média ou a mediana, e uma medida de dispersão, como a variância ou o desvio padrão.

# A variância pode ser calculada pela fórmula:

#      n
# vr = E (vi-md) /n-1
#     i=1

# Onde:

# vi é cada uma das amostras em uma lista "v" (v[0], v[1], v[2] etc)
# md é a média
# n é o número de amostras (o tamanho da lista "v")
# a letra grega sigma representa o somatório.
# Ou seja, deve-se somar: (v[0]-md)^2 + (v[1]-md)^2 + (v[2]-md)^3, e assim sucessivamente, e no final divide-se o resultado por n-1.

# Faça um programa que pergunta quantos alunas o professor tem. Em seguida, leia as notas de todas as alunas pelo teclado.

# O programa deverá exibir a média e a variância das notas da turma na tela.

# Sugestão de teste:

# A lista [9, 1, 8, 2, 7, 3, 6, 4] possui média = 5.0 e variância = 8.57 (aproximadamente)

notas = []
n_alunos = int(input('Informe o número de alunos: '))

for aluno in range(n_alunos):
   notas.append(float(input(f'Digite a nota do {aluno+1}º aluno: ')))

n = len(notas)

media = sum(notas) / n
vr = 0

for vi in notas:
    vr += (vi-media)**2

vr = round(vr / (n - 1), 2)

print(notas)
print(media)
print(vr)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7 A tabela SAC é uma alternativa à tabela Price. Ela também é utilizada para cálculo de prestações de empréstimos, como financiamentos 
# imobiliários.
# Ao contrário da tabela Price, ela não possui valor fixo de prestação. Ao invés disso ela possui valor fixo de amortização. Ou seja, 
# amortiza-se o mesmo valor todo mês.
# Logo no início do cálculo podemos dividir o saldo devedor pelo número total de meses para obter o valor da amortização.
# Em cada mês, iremos aplicar a taxa de juros ao saldo devedor da mesma maneira que na tabela Price para descobrir quanto pagaremos de 
# juros naquele mês. Em seguida, podemos somar taxa de juros e amortização (que é constante) para obter o valor da prestação. O novo saldo 
# devedor é obtido subtraindo o valor amortizado, como na tabela Price.
# Faça um programa que pede a taxa de juros de um empréstimo, o valor emprestado e o prazo (em meses) para quitar o empréstimo.
# Seu programa deverá mostrar, mês a mês, o valor pago de juros, de amortização, o valor total da prestação e o saldo devedor.

juros = float(input('Informe a taxa de juros (%) do empréstimo: ')) / 100
valor = float(input('Informe o valor do empréstimo: '))
prazo = int(input('Informe o prazo (em meses) para quitar o empréstimo: '))

amortizacao = valor / prazo

print('\n---------------------------------------------------------------------------------')
print(f'| Parcela 0\t| J: -\t\t| A: -\t\t| Pgto: -\t| Deve: {valor:.2f}|')
for parcela in range(prazo):
    j = juros * valor
    pv = j + amortizacao
    valor = valor - amortizacao
    print(
        f'| Parcela {parcela+1}\t| J: {j:.2f}\t| A: {amortizacao:.2f}\t| Pgto: {pv:.2f}\t| Deve: {valor:.2f}\t|')

print('---------------------------------------------------------------------------------')
