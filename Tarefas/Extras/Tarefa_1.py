#-----------------------------------------------------------------------------------------------------------------------------------#
# 1 Faça um programa que escreve a mensagem Sou Santander na tela do computador.

print('Sou Santander')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2 Faça um programa que pergunta o nome do usuário e responde Olá [nome] (substituindo "[nome]" pelo nome digitado).

nome = input('Qual o seu nome? ')
print('Olá ' + nome)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3 Faça um programa que pergunta o ano de nascimento do usuário e responde quantos anos ele terá ao final de 2022.

ano_nascimento = int(input('Informe seu ano de nascimento: '))
idade_2022 = 2022 - ano_nascimento
print(f'Sua idade ao final de 2022 será: {idade_2022}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4 Faça um programa que pergunta a nota das 4 provas de um aluno e responde a sua média.

notas = []
for i in range(4):
    nota = float(input(f'Informe a nota da prova {i+1}: '))
    notas.append(nota)
media = sum(notas)/len(notas)
print(media)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5 Faça um programa que pergunte para o motorista a distância que ele dirigiu e o tempo que seu trajeto levou, e responda sua velocidade média.

distancia = float(input('Informe a distância (km): '))
tempo = float(input('Informe o tempo (h): '))
velocidade_media = distancia/tempo
print(f'A sua velocidade média é de: {velocidade_media} (km/h)')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6 Um estacionamento cobra um valor mínimo de 10 reais, correspondente a 1h de uso. Cada hora adicional gera mais 5 reais de cobrança.
# Ex: um carro estacionado por 5 horas irá pagar 10 reais pela primeira hora + 5 reais pela segunda + 5 pela terceira + 5 pela quarta 
# + 5 pela quinta, totalizando 30 reais.
# Faça um programa que pergunte para o usuário quanto tempo seu carro ficou estacionado e responde o valor em reais a ser pago.
# OBS: o estacionamento não considera minutos, tampouco horas fracionárias. Portanto, o seu programa não precisa se preocupar com isso.
# Se a pessoa ficou 5 horas e 2 minutos, ela passou de 5 horas, portanto ela deve digitar a hora inteira mais próxima: 6 horas.

horas = int(input(
    'Informe quantas horas (inteiro mais próximo) em que seu carro ficou estacionado: '))
primeira_hora = 10
total = primeira_hora + ((horas-1)*5)
print(f'Valor total a ser pago: {total}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7 Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius.
# Atenção: apenas trocar "celsius" e "fahrenheit" na equação utilizada no exercício anterior não é a solução.
# Você deve realizar a inversão completa da fórmula (ou utilizar o mesmo truque para consultar essa fórmula no Google).

graus = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (graus * (9/5) + 32)
print(f'A temperatura em Fahrenheit é: {fahrenheit}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8 Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius.
# Atenção: apenas trocar "celsius" e "fahrenheit" na equação utilizada no exercício anterior não é a solução.
# Você deve realizar a inversão completa da fórmula (ou utilizar o mesmo truque para consultar essa fórmula no Google).

fahrenheit = float(input('Digite a temperatura em fahrenheit: '))
graus = (fahrenheit - 32) * (5/9)
print(f'A temperatura em graus é: {graus}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 9 Vai um cupom de desconto aí?
# Faça um programa que pergunta o preço de um produto, o desconto a ser aplicado (em %) e responde o valor total a ser pago.

preco = float(input('Informe o preço do produto: '))
desconto = float(input('Informe o desconto (%): '))
desconto = (preco/100)*desconto
total = preco - desconto
print(f'O preço final com desconto é: {total}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 10 Vamos falar de coisa boa: aumento salarial!
# Faça um programa que pergunta o salário do funcionário, o aumento a ser aplicado (em %) e responde o seu novo salário.

salario = float(input('Informe o salário: '))
aumento = float(input('Informe o aumento (%): '))
aumento = (salario/100)*aumento
total = salario + aumento
print(f'O novo salário com aumento é de: {total}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 11 Exercício avaliado
# Vamos fazer um programa para calcular o rendimento de uma aplicação.
# Faça um programa que pergunta quanto dinheiro o usuário irá aplicar, a taxa de juros ao mês (em %) e a duração da aplicação (em meses).
# Seu programa deve responder as seguintes informações:
# Qual o valor total a ser sacado ao final da aplicação? Quantos reais a pessoa recebeu apenas de juros? Quantos % a aplicação rendeu no total?
# Atenção: ao buscar as fórmulas para utilizar no problema, busque pela fórmula de juros compostos. Não utilize a fórmula de juros simples.

aplicacao = float(input('Informe quanto dinheiro será aplicado: '))
taxa_juros = float(input('Informe a taxa de juros ao mês (%): '))
periodo = int(input('Informe a duração da aplicação (meses): '))
total = aplicacao*(1+(taxa_juros/100))**periodo
juros = total - aplicacao
porcentagem_juros = ((total-aplicacao)/aplicacao)*100
print(f'O valor total a ser sacado ao final da aplicação é de: {total:.2f}')
print(f'O valor recebido apenas de juros foi de: {juros:.2f}')
print(
    f'A porcentagem (%) de rendimento da aplicação é de: {porcentagem_juros:.2f}')
