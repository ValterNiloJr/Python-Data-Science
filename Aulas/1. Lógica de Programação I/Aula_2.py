#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Suponha que o preço de capa de um livro seja R\$ 24,95, mas as livrarias recebem um desconto de 40%. 
#    O transporte custa R\$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. 
#    Qual é o custo total de atacado para 60 cópias?

desconto = 24.95 * 0.4

preco_unit = 24.95 - desconto

preco_total = preco_unit * 60

preco_transporte = 3 + (0.75 * 59)

preco_final = preco_total + preco_transporte

print(f'{preco_final:.2f}')

#945.45

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 
#    3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro 
#    lugar, que horas chego em casa para o café da manhã?

tempo1 = (8 * 60 + 15) * 2
tempo2 = (7 * 60 + 12) * 3
tempo_total = tempo1 + tempo2

print(tempo_total)

hora_inicial = (6 * 3600) + (52 * 60)

hora_final = hora_inicial + tempo_total

horas = hora_final // 3600
minutos = (hora_final % 3600) // 60
segundos = ((hora_final % 3600) % 60)

print(f'{horas}:{minutos}:{segundos}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Escreva um programa que realize transformações de graus celsius a fahrenheit. O programa deve solicitar por 
#    teclado os graus celsius, e deve mostrar uma mensagem mostrando o valor equivalente em graus fahrenheit. A fórmula é:
#    F = C * 1,8 + 32

graus = float(input('Informe a temperatura em graus celsius (ºC): '))

fahrenheit = graus * 1.8 + 32

print(f'A temperatura em Fahrenheit vale: {fahrenheit} ºF')