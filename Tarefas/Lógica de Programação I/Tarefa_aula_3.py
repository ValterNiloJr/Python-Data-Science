#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até
#    que o usuário informe um valor válido

nota = int(input('Informe um valor entre 0 e 10: '))

while not (0 <= nota <= 10):
    print('A nota informada é inválida, tente novamente.')
    nota = int(input('Informe um valor entre 0 e 10: '))

print('Nota válida!')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população
#    de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
#    para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pais_A = 80000
taxa_A = 0.03

pais_B = 200000
taxa_B = 0.015

ano = 0

while not (pais_A >= pais_B):
    ano += 1
    pais_A += (pais_A * taxa_A)
    pais_B += (pais_B * taxa_B)

print(f'O número de anos necessários para que a população de A ultrapasse ou iguale a população de B é: {ano}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de
#    qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

#    Tabuada de 5:
#    5 X 1 = 5
#    5 X 2 = 10
#    ...
#    5 X 10 = 50

num = int(input('Informe o número ao qual deseja ver a tabuada: '))

for mul in range (1, 11):
    print(f'{num} X {mul:<2} = {num*mul}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá
#    mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e
#    o número de testes (divisões) executados.

n = int(input('Informe um número inteiro: '))

primos = []
n_divisoes = 0
total_n_divisoes = 0

for i in range(1, n+1):
    for j in range (1, i+1):
        if ((i % j) == 0):
            n_divisoes += 1
        total_n_divisoes += 1
    if n_divisoes == 2:
        primos.append(i)
    n_divisoes = 0


print(f'Os numeros primos entre 1 e {n} são: {primos}')
print(f'O número total de divisões foi de: {total_n_divisoes}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto
#    cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta.
#    Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi
#    contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o
#    exemplo abaixo:

#    Lojas Quase Dois - Tabela de preços
#    1 - R$ 1.99
#    2 - R$ 3.98
#    ...
#    50 - R$ 99.50

tabela = [preco*1.99 for preco in range(1, 51)]

# Exibição
print('Lojas Quase Dois - Tabela de preços')
for index in range(len(tabela)):
    print(f'{index + 1:<2} - R$ {tabela[index]:.2f}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso
#    na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a
#    partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

#    Preço do pão: R$ 0.18
#    Panificadora Pão de Ontem - Tabela de preços
#    1 - R$ 0.18
#    2 - R$ 0.36
#    ...
#    50 - R$ 9.00

preco_pao = float(input('Informe o preço do Pão: '))

tabela = [preco*preco_pao for preco in range(1, 51)]

# Exibição
print(f'Preço do pão: R$ {preco_pao}')
print('Panificadora Pão de Ontem - Tabela de preços')
for index in range(len(tabela)):
    print(f'{index + 1:<2} - R$ {tabela[index]:.2f}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um
#    programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes
#    aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então
#    mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
#    Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o
#    exemplo abaixo:

#    Lojas Tabajara
#    Produto 1: R$ 2.20
#    Produto 2: R$ 5.80
#    Produto 3: R$ 0
#    Total: R$ 9.00
#    Dinheiro: R$ 20.00
#    Troco: R$ 11.00
#    ...

#Exit code = -1
valor = 0
while (valor != -1):
    contador = 1
    valor = -2
    produtos = []
    while (valor != 0):
        valor = float(input(f'Produto {contador}: R$ '))
        produtos.append(valor)
        contador += 1
    total = sum(produtos)
    print(f'Total: R$ {total:.2f}')
    dinheiro = float(input('Dinheiro: R$ '))
    print(f'Troco: R$ {dinheiro - total}')
    valor = float(input(f'{0:>2} -> Próxima venda\n-1 -> Sair\n'))

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros,
#    quantidade de parcelas e valor da parcela.

qt_parcelas = [1, 3, 6, 9, 12]
procentagem_juros = [0, 10, 15, 20, 25]

divida = float(input('Informe o valor da dívida: '))

print('---------------------------------------------------------------------------------')
print('| Valor da dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela |')
print('|-----------------|-----------------|------------------------|------------------|')
for i in range(len(qt_parcelas)):
    valor_juros = divida * (procentagem_juros[i] / 100)
    valor_divida = divida + valor_juros
    valor_parcela = valor_divida / qt_parcelas[i]
    print(
        f'| R$ {valor_divida:<12} | {valor_juros:<15.2f} | {qt_parcelas[i]:<22} | R$ {valor_parcela:<13.2f} |')
print('---------------------------------------------------------------------------------')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 9. O cardápio de uma lanchonete é o seguinte:

#    Especificação   Código  Preço
#    Cachorro Quente 100     R$ 1,20
#    Bauru Simples   101     R$ 1,30
#    Bauru com ovo   102     R$ 1,50
#    Hambúrguer      103     R$ 1,20
#    Cheeseburguer   104     R$ 1,30
#    Refrigerante    105     R$ 1,00
   
#    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item 
#    (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

especificacao = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
codigos = [100, 101, 102, 103, 104, 105]
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]

pedidos = []

codigo = -1
while (codigo != 0):
    codigo = int(input('0 -> Encerrar pedido\nInforme o código do produto: '))
    if codigo in codigos:
        codigo_id = codigos.index(codigo)
        pedidos.append([f'Produto: {especificacao[codigo_id]:<16} | R$ {precos[codigo_id]:.2f}', precos[codigo_id]])

    elif codigo != 0:
        print('Código Inválido')
total = 0
for pedido in pedidos:
    print(pedido[0])
    total += pedido[1]
print(f'{"Total:":>25} | R$ {total:.2f}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 10. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a 
#     resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto 
#     por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos 
#     os alunos terem respondido informar:

#     Maior e Menor Acerto;
#     Total de Alunos que utilizaram o sistema;
#     A Média das Notas da Turma.
    
#     Gabarito da Prova:
    
#     01 - A
#     02 - B
#     03 - C
#     04 - D
#     05 - E
#     06 - E
#     07 - D
#     08 - C
#     09 - B
#     10 - A
#     Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

n_questoes = int(input('Informe o número de questões da prova: '))

gabarito = []

for i in range(n_questoes):
    gabarito.append(input(f'Informe o gabarito da questão: {i+1}: ').upper())

continuar = 's'

while(continuar.lower() != 'n'):
    print('-- INÍCIO --')
    #gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    
    questoes = []
    total_pontos = 0

    for i in range(len(gabarito)):
        questoes.append(input(f'Informe a resposta da questão {i+1}: '))
        if questoes[i].upper() == gabarito[i]:
            total_pontos += 1
        
    print('Gabarito | Questão')
    for i in range(len(gabarito)):    
        print(f'{gabarito[i]:>8} | {questoes[i].upper():<7}')
    print(f'Total de pontos: {total_pontos}')
    continuar = input('Outro aluno deseja verificar sua nota: (s/n): ')

print('-- FIM --')