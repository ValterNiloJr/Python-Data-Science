#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Escreva um programa que retorna a parte decimal de um número. O programa deve solicitar por teclado um número, 
#    se a parte decimal for 0 mostrar a mensagem 'O número informado é um inteiro.'. Se a parte decimal for diferente de 0, 
#    mostrar a mensagem 'A parte decimal é: x' ('x' é o valor decimal).

numero = float(input('Digite um número: '))

decimal = numero - int(numero)

if decimal != 0:
    print(f'A parte decimal é: {decimal:.2f}')
else:
    print('O número informado é um inteiro')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Uma empresa decidiu dar bonificação de 5% ao funcionário se o seu tempo de serviço for superior a 5 anos. 
#    Pergunte ao usuário seu salário e anos de serviço e imprima o valor líquido do bônus.

bonificacao = 0.5
tempo_minimo = 5

salario = float(input('Informe o seu salário: '))
tempo = float(input('Informe o tempo de serviço: '))

if tempo > tempo_minimo:
    salario = salario * bonificacao
    print(f'Parabéns! Seu bônus vai ser de: {salario}')
else:
    print(f'Seu bônus vai ser de: {salario}')
#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. A Ada decidiu organizar um bolão para a copa do Mundo. As regras para atribuir pontos são as seguintes:
#    Acertar o placar exato dá 25 pontos.
#    Acertar o vencedor e o número de gols da equipe vencedora dá 18 pontos.
#    Acertar o vencedor e a diferença de gols entre o vencedor e perdedor dá 15 pontos.
#    Acertar que a partida terminaria em empate dá 15 pontos.
#    Acertar o time vencedor e o número de gols do time perdedor dá 12 pontos.
#    Acertar apenas o vencedor da partida dá 10 pontos.
#    Previu que o jogo seria um empate e não foi empate dá 4 pontos.
#    Qualquer outro caso, serão 0 pontos.
#    Construa um programa que verifique quantos pontos a usuário ganhou em uma partida. O programa deve solicitar 
#    os valores do escore real e os valores preditos pelo usuário.

#    Exemplos:

#    O resultado do jogo foi: Time_A vs Time_B (2 - 3)

#    Para o palpite (1 - 3), o usuário ganha 18 pontos (acertou vencedor e numero de gols da equipe vencedora.)
#    Para o palpite (0 - 1), o usuário ganha 15 pontos (acertou vencedor e diferença de gols.)
#    Para o palpite (0 - 2), o usuário ganha 10 pontos (acertou unicamente o vencedor.)
#    Para o palpite (2 - 2), o usuário unicamente ganha 4 pontos.

score_vencedor=0
score_perdedor=0
palpite_score_vencedor=0
palpite_score_perdedor=0
vencedor = ''
palpite_vencedor= '-'

#pegando os inputs
score1= int(input('Informe o score do primeiro time:'))
score2= int(input('Informe o score do segundo time:'))
palpite1= int(input('Informe seu palpite sobre o primeiro time:'))
palpite2= int(input('Informe seu palpite sobre o primeiro time:'))

#verificando o vencedor 
if score1>score2:
    vencedor = 'TimeA'
    score_vencedor = score1
    score_perdedor = score2
elif score1<score2:
    vencedor = 'TimeB'
    score_vencedor = score2
    score_perdedor = score1
else:
    empate = True
diferenca= abs(score1 - score2)
    
#verificando quem o usuario achou que venceria
if palpite1>palpite2:
    palpite_vencedor = 'TimeA'
    palpite_score_vencedor = palpite1
    palpite_score_perdedor = palpite2
elif palpite1<palpite2:
    palpite_vencedor = 'TimeB'
    palpite_score_vencedor = palpite2
    palpite_score_perdedor = palpite1
else:
    palpite_empate = True
palpite_diferenca = abs(palpite1 - palpite2)

#print(score_vencedor)
#print(palpite_score_vencedor)
print(empate)
print(palpite_empate)
print(diferenca)
print(palpite_diferenca)

    
if (score1 == palpite1) and (score2 == palpite2):
    print('25 pontos.')
elif (vencedor == palpite_vencedor) and (score_vencedor == palpite_score_vencedor):
    print('18 pontos.')
elif (vencedor == palpite_vencedor) and (diferenca == palpite_diferenca) and (diferenca!=0):
    print('15 pontos 1.')
elif (score1==score2) and (palpite1 == palpite2):
    print('15 pontos 2.')
elif (vencedor==palpite_vencedor) and (score_perdedor == palpite_score_perdedor):
    print('12 pontos.')
elif (vencedor==palpite_vencedor):
    print('10 pontos.')
elif (palpite1==palpite2) and (score1!=score2):
    print('4 pontos')
else:
    print('0 pontos')