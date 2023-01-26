#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Faça um programa em linguagem python que receba um valor em metros, e o converta para centímetros. Por fim, imprima na tela o 
#    resultado obtido. Dica: para converter metros em centímetros, basta multiplicar o valor por 100.

m = float(input('Digite um valor em metros: '))

cm = m * 100

print(f'O valor convertido é de: {cm:.2f} cm')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do empréstimo deve ser até dez vezes o valor 
#    da renda mensal do solicitante e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante. Escreva um 
#    programa que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado e o número de prestações que o 
#    solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.

renda_mensal = float(input('Informe sua renda mensal: '))
valor_total = float(input('Informe o valor total do Empréstimo: '))
n_prestacoes = int(input('Informe o número de prestações: '))

valor_prestacao = valor_total / n_prestacoes

if (valor_total <= (10 * renda_mensal)) and (valor_prestacao <= (0.3 * renda_mensal)):
    print('O impréstimo pode ser concedido!')
else:
    print('O impréstimo não pode ser concedido!')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Escreva um programa em python que receba o tamanho do lado de um quadrado, e calcule sua área e seu perímetro, e imprima o resultado na tela.

lado_quadrado = float(input('Informe o lado de um Quadrado: '))

area = lado_quadrado ** 2
perimetro = lado_quadrado * 4

print(f'A área do quadrado é de {area} unidades')
print(f'O perímetro do quadrado é de {perimetro} unidades')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Escreva um programa em python que receba dois números inteiros e exiba o quociente e o resto da divisão inteira entre eles.

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))

quociente = n1 / n2
resto = n1 % n2

print(f'O quociente da divisão entre {n1} e {n2} é: {quociente}')
print(f'O resto da divisão entre {n1} e {n2} é: {resto}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), escreva um programa em python que receba um
#    valor de temperatura em Fahrenheit e exibi-o em Celsius

fahrenheit = float(input('Informe a temperura em Fahrenheit: '))

celcius = (5/9) * (fahrenheit - 32)

print(f'A temperatura convertida em Graus Celsius é de: {celcius}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. Faça programa em python para calcular a nota semestral de um aluno. A nota semestral é obtida pela média aritmética entre a nota 
#    de 2 bimestres. Cada nota de bimestre é composta por 2 notas de provas.

n1 = float(input('Informe a 1ª nota do 1º bimestre: '))
n2 = float(input('Informe a 2ª nota do 1º bimestre: '))
n3 = float(input('Informe a 1ª nota do 2º bimestre: '))
n4 = float(input('Informe a 2ª nota do 2º bimestre: '))

primeiro_bi = (n1 + n2) / 2
segundo_bi = (n3 + n4) / 2
nota_semestral = (primeiro_bi + segundo_bi) / 2

print(f'A nota semestral foi: {nota_semestral}')