#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o 
#    seguinte resultado:

#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))

media = (n1 + n2) / 2


if(media == 10):
    print(f'Aluno Aprovado com Distinção. Média: {media}')
elif (10 > media >= 7):
    print(f'Aluno Aprovado. Média: {media}')
else:
    print(f'Aluno Reprovado. Média: {media}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Faça um Programa que leia três números inteiros e mostre o maior deles.

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe um número inteiro: '))
num3 = int(input('Informe um número inteiro: '))

num_max = max(([num1, num2, num3]))

print(f' O maior número é {num_max}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
#    mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Informe o turno que você estuda:\nM - Matutino\nV - Vespentino\nN - Noturno\n')

if turno.upper().strip() == 'M':
    print('Bom Dia!')
elif turno.upper().strip() == 'V':
    print('Boa Tarde!')
elif turno.upper().strip() == 'N':
    print('Boa Noite!')
else:
    print('Comando inválido!')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5%
#    Após o aumento ser realizado, informe na tela:

#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.

salario_inicial = float(input('Informe seu salário atual (R$): '))
aumento = 0
if 0 < salario_inicial <= 280:
    aumento = 0.2
elif 280 < salario_inicial <= 700:
    aumento = 0.15
elif salario_inicial <= 1500:
    aumento = 0.1
elif 1500 < salario_inicial:
    aumento = 0.05
else:
    aumento = -1

if aumento >= 0:
    percentual_aumento = int(aumento * 100)
    valor_aumento = (salario_inicial * aumento)
    salario_final = salario_inicial + valor_aumento

    print(f'O salário antes do reajuste era de: R$ {salario_inicial:.2f}')
    print(f'O percentual de aumento aplicado foi de: {percentual_aumento}%')
    print(f'O valor aumentado foi de: R$ {valor_aumento:.2f}')
    print(f'O novo salário, após o reajuste é de: R$ {salario_final:.2f}')

else:
    print('Salário informado inválido')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do 
#    salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
#    (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o 
#    valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:

#    Salário Bruto até 900 (inclusive) - isento

#    Salário Bruto até 1500 (inclusive) - desconto de 5%

#    Salário Bruto até 2500 (inclusive) - desconto de 10%

#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o 
#    valor da hora é 5 e a quantidade de hora é 220.

#    Salário Bruto: (5 * 220): R$ 1100,00

#    (-) IR (5%): R$ 55,00
#    (-) INSS ( 10%): R$ 110,00
#    FGTS (11%): R$ 121,00
#    Total de descontos: R$ 165,00
#    Salário Liquido: R$ 935,00

FGTS = 0.11
INSS = 0.03

valor_hora = float(input('Informe o valor de sua hora trabalhada: '))
horas_trabalhadas = float(input('Informe a quantidade de Horas trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas

if 0 < salario_bruto <= 900:
    porcentagem_IR = 0
elif salario_bruto <= 1500:
    porcentagem_IR = 0.05
elif salario_bruto <= 2500:
    porcentagem_IR = 0.1
elif salario_bruto > 2500:
    porcentagem_IR = 0.2
else:
    porcentagem_IR = -1

if porcentagem_IR >= 0:
    valor_IR = (salario_bruto * porcentagem_IR)
    valor_INSS = (salario_bruto * INSS)
    valor_FGTS = (salario_bruto * FGTS)
    descontos = valor_IR + valor_INSS
    salario_liquido = salario_bruto - descontos

    print(f'O salário bruto é de: {salario_bruto:.2f}')
    print(f'(-) IR ({int(porcentagem_IR * 100)}%): R$ {valor_IR:.2f}')
    print(f'(-) INSS ({INSS * 100}): R$ {valor_INSS:.2f}')
    print(f'FGTS ({int(FGTS * 100)}%): R$ {valor_FGTS:.2f}')
    print(f'Total de descontos: R$ {descontos:.2f}')
    print(f'Salário Líquido: R$ {salario_liquido}')
    
else:
    print('O Valor da hora ou as horas trabalhadas informadas são inválidas')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# desconsiderando anos bissextos

dia, mes, ano = input('Informe uma data no formato (dd/mm/aaaa): ').split('/')

dia = int(dia)
mes = int(mes)

mes_maximo_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dia_formatado = (0 < dia <= mes_maximo_dias[mes-1])
mes_formatado = (0 < mes <= 12)
ano_formatado = (len(ano) == 4) # Considerando os anos desde 0001 até 9999

if dia_formatado and mes_formatado and ano_formatado:
    print('A data informada é valida!')
else:
    print('A data informada não é valida!')

'''
def gerador_de_quadrados(iteravel_de_numeros):
    count = 0
    for numero in iteravel_de_numeros:
        count += 1
        print(count)
        yield numero**2
        

number = gerador_de_quadrados(range(3))
print(f'yield {next(number)}')
print(f'yield {next(number)}')
print(f'yield {next(number)}')


exercício 4
nova_lista = [i for i in a if i % 2 == 0 and i % 3 == 0 and i % 4 == 0]
Tiago Guedes21:52
lista_final = [n if n in lista_mult3 and n in list_mult]
Mayara Medeiros21:52
lista_multiplos = []

for n in lista:
    if n % 2 == 0 and n % 3 == 0 and n % 4 == 0:
        lista_multiplos.append(n)
'''
