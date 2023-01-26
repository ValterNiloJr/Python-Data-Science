#-----------------------------------------------------------------------------------------------------------------------------------#
# 1 Faça um programa que pede para a usuária digitar um número e responde se o número é positivo ou negativo.

numero = float(input('Informe um número: '))

if numero > 0:
   print('O número informado é positivo')
elif numero < 0:
   print('O número informado é negativo')
else:
   print('O número informado é neutro')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2 Faça um programa que pede para o usuário digitar um número e responde se o número é par ou ímpar.

numero = float(input('Informe um número: '))
if (numero % 2) == 0:
   print('O número informado é par')
else:
   print('O número informado é ímpar')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3 Faça um programa que pergunta o nome da usuária e o horário do dia (apenas horas, sem os minutos). O programa deverá responder:
# Bom dia, [nome]! caso o horário esteja entre 4 e 11.
# Boa tarde, [nome]! caso o horário esteja entre 12 e 17.
# Boa noite, [nome]! caso o horário esteja entre 18 e 23 ou 0 e 3.
# Horário inválido caso o horário seja superior a 23 ou inferior a 0.

nome = input('Qual o seu nome? ')
horario = int(input('Que horas são? (Apenas horas) '))
if 4 <= horario <= 11:
   print(f'Bom dia, {nome}')
elif 12 <= horario <= 17:
   print(f'Bom tarde, {nome}')
elif 18 <= horario <= 23 or 0 <= horario <= 3:
   print(f'Bom noite, {nome}')
else:
   print('Horário inválido')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4 Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:
# Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
# Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
# Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'
# Opção inválida caso gênero não possua um dos 3 valores descritos acima.

nome = input('Qual o seu nome? ')
genero = input('Qual o seu Gênero? (F/M/Neutro/Outro)').upper()
if genero == 'M':
   print(f'Seja bem-vindo, {nome}')
elif genero == 'F':
   print(f'Seja bem-vinda, {nome}')
elif genero == 'NEUTRO' or genero == 'OUTRO':
   print(f'Seja bem-vind@, {nome}')
else:
   print('Opção inválida')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5 Faça um programa que deverá pedir as 2 notas de uma pessoa e calcular sua média. Considere que as notas serão de 0 a 100.
# O programa deverá informar a média da pessoa e seu status, obedecendo as regrinhas abaixo:
# Aprovada, caso a média seja pelo menos 70.
# Exame, caso a média seja pelo menos 30 e menor do que 70.
# Reprovada caso a média seja inferior a 30.

nota_1 = float(input('Informe a nota 1: (0 ~ 100) '))
nota_2 = float(input('Informe a nota 2: (0 ~ 100) '))
media = (nota_1 + nota_2) / 2
print(f'Média: {media}')
if media >= 70:
   print('Aprovada')
elif 30 <= media < 70:
   print('Exame')
else:
   print('Reprovada')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6 Modifique o programa das médias do exercício anterior da seguinte maneira:
# Caso a aluna tenha ficado de exame, pergunte a nota do exame.
# Uma nova média deve ser calculada entre a média original e a nota do exame:
# media_exame = (media + exame)/2
# O programa deve exibir essa nova média junto do novo status:
# Aprovada por exame caso a media_exame seja pelo menos 50.
# Reprovada caso a media_exame seja inferior a 50.

nota_1 = float(input('Informe a nota 1: (0 ~ 100) '))
nota_2 = float(input('Informe a nota 2: (0 ~ 100) '))
media = (nota_1 + nota_2) / 2
print(f'Média: {media}')
if media >= 70:
   print('Aprovada')
elif 30 <= media < 70:
   print('Exame')
   exame = float(input('Informe a nota do exame (0 ~ 100) '))
   media_exame = (media + exame) / 2
   print(f'Média final: {media_exame}')
   if media_exame >= 50:
       print('Aprovada')
   else:
       print('Reprovada')
else:
   print('Reprovada')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7 Faça um programa que pergunta o comprimento de cada um dos 3 lados de um triângulo.
# O programa deverá responder:
# É triângulo, caso nenhum dos lados possua comprimento superior à soma dos outros dos lados.
# Não é triângulo, caso um dos lados seja possua comprimento superior à soma dos outros dois lados.

l1, l2, l3 = input('Informe os 3 lados do triangulo: (separados por espaços) ').split(' ')
if (int(l1) < (int(l2) + int(l3))) and (int(l2) < (int(l1) + int(l3))) and (int(l3) < (int(l2) + int(l1))):
    print('É triângulo')
else:
   print('Não é triângulo')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8 Modifique o programa dos triângulos do exercício anterior da seguinte maneira:
# Caso o programa tenha determinado que o triângulo existe, informe também o seu tipo:
# Equilátero, caso os 3 lados sejam iguais
# Isósceles, caso apenas 2 lados sejam iguais
# Escaleno, caso todos os lados sejam diferentes entre si

l1, l2, l3 = input('Informe os 3 lados do triangulo: (separados por espaços) ').split(' ')
if (int(l1) < (int(l2) + int(l3))) and (int(l2) < (int(l1) + int(l3))) and (int(l3) < (int(l2) + int(l1))):
    print('É triângulo')
    if (l1 == l2) and (l1 == l3) and (l2 == l3):
        print('Equilátero')
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print('Isósceles')
    else:
        print('Escaleno')   
else:
   print('Não é triângulo')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 9 Faça um programa que pede para a usuária digitar, separadamente, os coeficientes a, b e c de uma equação de segundo grau.
# O programa deverá calcular o valor do discriminante (delta) e:
# Caso seja positivo, o programa deverá calcular e exibir na tela os valores de suas duas raizes reais e distintas.
# Caso seja zero, o programa deverá calcular e exibir na tela a sua única raiz.
# Caso seja negativo, o programa deverá exibir a mensagem Não possui raizes reais.

a = float(input('Digite o coeficiente A: '))
b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))
delta = ((b ** 2) - (4 * a * c))
if delta < 0:
    print('Não possui raízes reais')
elif delta == 0:
    r = - b / (2 * a)
    print(f'Sua única raíz é: {r}')
else:
    r1 = (- b + (delta ** (1/2))) / (2 * a)
    r2 = (- b - (delta ** (1/2))) / (2 * a)
    print(f'Suas duas raízes distintas são: {r1} e {r2}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 10 Faça um programa que pergunta um ano para a usuária e responde se ele é bissexto ou não.
#A regra geral para determinar se um ano é bissexto é: todo ano divisível por 4, a princípio, é bissexto: 2016, 2020, 2024...
#Porém existe uma exceção: anos divisíveis por 100 não são bissextos. O ano 2100, por exemplo, é divisível por 4, mas como também é 
# divisível por 100, ele não pode ser bissexto.
#A exceção possui uma exceção: anos divisíveis por 400 são bissextos. O ano 2000, por exemplo, é divisível por 100. Porém, como ele 
# também é divisível por 400, ele torna-se bissexto.

ano = int(input('Digite um ano: '))
if (ano % 400) == 0:
    print('O ano é bissexto')
elif (ano % 100) == 0:
    print('O ano não é bissexto')
elif (ano % 4) == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 11 Um banco oferece as seguintes opções de aplicação de renda fixa:
# Fundo A: aceita aplicações a partir de 50 reais, não possui tempo mínimo de aplicação e rende 10% ao ano.
# Fundo B: aceita aplicações a partir de 100 reais, possui tempo mínimo de aplicação de 1 ano e rende 12% ao ano.
# Fundo C: aceita aplicações a partir de 500 reais, possui tempo mínimo de aplicação de 2 anos e rende 13% ao ano.
# Fundo D: aceita aplicações a partir de 1000 reais, possui tempo mínimo de aplicação de 3 anos e rende 15% ao ano.
# Fundo E: aceita aplicações a partir de 3000 reais, possui tempo mínimo de aplicação de 5 anos e rende 18% ao ano.
# Faça um programa que pergunta para a usuária em qual fundo ela deseja aplicar seu dinheiro, quanto dinheiro ela possui e o tempo que 
# ela pretende deixar o dinheiro aplicado (em anos).
# Caso o valor e o tempo estejam adequados às regras do fundo selecionado, utilize a fórmula dos juros compostos para informar para ela 
# o valor total que ela irá sacar ao final do período informado por ela.
# Caso contrário, exiba a mensagem Não é possível realizar essa aplicação.

fundo = input('Informe o Fundo (A, B, C, D ou E) em que deseja fazer a aplicação: ').upper()
aplicacao = float(input('Informe quanto dinheiro será aplicado: '))
periodo = int(input('Informe a duração da aplicação (anos): '))
regras = False

if fundo == 'A' and aplicacao >= 50:
    taxa_juros = 10
    regras = True

elif fundo == 'B' and periodo >= 1 and aplicacao >= 100:
    taxa_juros = 12
    regras = True

elif fundo == 'C' and periodo >= 2 and aplicacao >= 500:
    taxa_juros = 13
    regras = True

elif fundo == 'D' and periodo >= 3 and aplicacao >= 1000:
    taxa_juros = 15
    regras = True

elif fundo == 'E' and periodo >= 5 and aplicacao >= 3000:
    taxa_juros = 18
    regras = True

if regras:
    total = aplicacao * (1 + (taxa_juros / 100)) ** periodo
    print(f'O valor total a ser sacado ao final da aplicação é de: {total:.2f}')

else:
    print('Não é possível realizar essa aplicação.')