#-----------------------------------------------------------------------------------------------------------------------------------#
# 1 Faça um programa que pede para o usuário digitar um número inteiro positivo. O programa deve exibir todos os números inteiros 
# de 0 até o número digitado.

max_range = int(input('Digite um número inteiro positivo: '))
count = 0
while count <= max_range:
  print(count)
  count = count + 1

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2 Modifique o programa anterior para, além de ler o valor final pelo teclado, ler também o valor inicial.

# a)
inicio, fim = input('Digite dois números (separados por espaço) representando o valor de início e fim: ').split(' ')
contador = int(inicio)
while contador <= int(fim):
   print(contador)
   contador = contador + 1

# b)
inicio = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
contador = inicio
while contador <= fim:
   print(contador)
   contador = contador + 1

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3 Modifique o programa anterior para perguntar também o "passo", ou seja, de quantas em quantas unidades a contagem irá saltar.

inicio = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
passo = int(input('Digite o passo: '))
contador = inicio
while contador <= fim:
  print(contador)
  contador = contador + passo

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4 Faça um programa que pede para a usuária digitar um número. O programa deverá exibir a tabuada daquele número.

numero = int(input('Digite um número inteiro: '))
contador = 1
while contador <= 10:
  print(f'{numero} x {contador} = {numero * contador}')
  contador = contador + 1

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5 Faça um programa que pede para a usuária digitar um número inteiro positivo. Seu programa deverá responder a soma de do número 
# com todos os seus antecessores positivos.
# Ex: se o número digitado for 5, a conta a ser realizada será 5 + 4 + 3 + 2 + 1, e o resultado na tela será "15".

numero = int(input('Digite um número inteiro positivo: '))
contator = 1
soma = 0
while contator <= numero:
  soma = soma + contator
  contator = contator + 1
print(soma)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6 Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deverá calcular e exibir na tela o 
# fatorial do número digitado.
# Lembrete: o fatorial de um número "n", denotado por "n!", é o produto dele com todos os seus antecessores inteiros positivos.
# Ex: 5! = 1 x 2 x 3 x 4 x 5

numero = int(input('Digite um número inteiro positivo: '))
contator = 1
fatorial = 1
while contator <= numero:
  fatorial = fatorial * contator
  contator = contator + 1
print(fatorial)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7 Faça um programa que pergunta quantas provas o usuário fez. Em seguida, o programa deverá ler cada uma de suas notas pelo teclado 
# e informar sua média.

n_provas = int(input('Digite a quantidade de provas feitas: '))
contador = 1
nota = 0
while contador <= n_provas:
  nota = nota + float(input(f'Informe a nota da prova {contador}: '))
  contador = contador + 1
print(f'A média final é: {nota / n_provas}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8 Iremos novamente fazer o programa da média do exercício anterior, mas com uma diferença: agora não iremos perguntar a quantidade 
# de notas. O usuário deverá digitar uma nota negativa quando desejar parar de digitar mais notas.
# Atenção: o número negativo não deve ser considerado uma nota (portanto, não deve interferir na média).

nota = 0
nota_aux = 0
n_provas = 0
while nota_aux >= 0:
  nota_aux = float(input(f'Informe a nota da prova {n_provas}: (Informe um número negativo para sair) '))
  if nota_aux >= 0:
      print(nota_aux)
      nota = nota + nota_aux
      n_provas = n_provas + 1
print(f'A média final é: {nota / n_provas}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 9 Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:
# Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
# Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
# Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'
# Caso uma opção diferente das listadas acima seja digitada, o programa deverá repetir a pergunta até que uma das opções válidas seja digitada.

nome = input('Qual o seu nome? ')
genero = ''
while genero != 'M' and genero != 'F' and genero != 'NEUTRO' and genero != 'OUTRO':
   genero = input('Qual o seu Gênero? (F/M/Neutro/Outro)').upper()
   if genero == 'M':
       print(f'Seja bem-vindo, {nome}')
   elif genero == 'F':
       print(f'Seja bem-vinda, {nome}')
   elif genero == 'NEUTRO' or genero == 'OUTRO':
       print(f'Sej@ bem-vind@, {nome}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 10 Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:
# Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
# Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
# Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'
# Caso uma opção diferente das listadas acima seja digitada, o programa deverá repetir a pergunta até que uma das opções válidas seja digitada.

nome = input('Qual o seu nome? ')
genero = ''
while genero != 'M' and genero != 'F' and genero != 'NEUTRO' and genero != 'OUTRO':
   genero = input('Qual o seu Gênero? (F/M/Neutro/Outro)').upper()
   if genero == 'M':
       print(f'Seja bem-vindo, {nome}')
   elif genero == 'F':
       print(f'Seja bem-vinda, {nome}')
   elif genero == 'NEUTRO' or genero == 'OUTRO':
       print(f'Sej@ bem-vind@, {nome}')
else:
   print('FIM')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 11 Questão avaliada
# Juros de novo! :)
# Pergunte para a usuária o valor que será investido em uma aplicação, a taxa de juros ao mês e o tempo que o dinheiro ficará aplicado.
# Seu programa deverá exibir quanto de juros será pago e o saldo total em cada mês.

aplicacao = float(input('Informe quanto dinheiro será aplicado: '))
taxa_juros = float(input('Informe a taxa de juros ao mês (%): '))
periodo = int(input('Informe a duração da aplicação (meses): '))

total_anterior = 0
contador = 1

while contador <= periodo:
    total = (aplicacao * (1 + (taxa_juros / 100)) ** contador)
    juros_mensais = (total - total_anterior)
    
    print(f'Mês {contador}: Juros: {juros_mensais:.2f} reais, saldo: {total:.2f} reais')
    
    total_anterior = total
    contador = contador + 1
