#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Dado um número inteiro, retorne o número de etapas para reduzi-lo a zero.

#    Em uma etapa, se o número atual for par, você deve dividi-lo por 2, caso contrário, deve subtrair 1 dele. Exemplo:

#    Entrada: num = 14

#    Saída: 6

#    Explicação:

#    Etapa 1) 14 é par; divida por 2 e obtenha 7.
#    Etapa 2) 7 é ímpar; subtraia 1 e obtenha 6.
#    Etapa 3) 6 é par; divida por 2 e obtenha 3.
#    Etapa 4) 3 é ímpar; subtraia 1 e obtenha 2.
#    Etapa 5) 2 é par; divida por 2 e obtenha 1.
#    Etapa 6) 1 é ímpar; subtraia 1 e obtenha 0.

num = int(input("Informe um número inteiro: "))
saida = num
etapa = 0

while saida != 0:
    etapa += 1
    if (saida % 2) == 0:
        saida //= 2
        print(f'Etapa {etapa}) {num} é par; divida por 2 e obtenha {saida}.')
    else:
        saida -= 1
        print(f'Etapa {etapa}) {num} é ímpar; subtraia 1 e obtenha {saida}.')
    if saida < 0:
        print('Número menor que zero!')
        break
    num = saida

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Você tem 'n' moedas e deseja construir uma escada com essas moedas. A escada consiste em k fileiras onde a iésima fileira tem exatamente i moedas. A última fila da escada pode estar incompleta.

#    Dado o inteiro n, retorne o número de linhas completas da escada que você construirá.

n_moedas = int(input('Informe o número de moedas: '))
n_filas = 0

while n_moedas >= 0:
    n_filas += 1
    n_moedas -= n_filas

print(f'O número de filas completas é de: {n_filas - 1}')

# x^2 + 1x -2(num) = 0
# não faço ideia do porque isso funciona
num = int(input('Informe o numero de moedas: '))
a = 1
b = 1
c = -2
delta = (b**2)-(4*a*c*num)
x = (-b + (delta**(1/2)))/2*a
print(x)

#-----------------------------------------------------------------------------------------------------------------------------------#
# (casa) 
# 3. Dadas as coordenadas de dois retângulos retilíneos em um plano 2D, retorne a área total coberta pelos dois retângulos.

#    O primeiro retângulo é definido por seu canto inferior esquerdo (ax1, ay1) e seu canto superior direito (ax2, ay2).

#    O segundo retângulo é definido por seu canto inferior esquerdo (bx1, by1) e seu canto superior direito (bx2, by2).

# ax1 = -5
# ay1 = -2

# ax2 = -1
# ay2 = 1

# bx1 = -2
# by1 = 0

# bx2 = 3
# by2 = 2

ax1 = int(input('Digite o valor de ax1: '))
ay1 = int(input('Digite o valor de ay1: '))
ax2 = int(input('Digite o valor de ax2: '))
ay2 = int(input('Digite o valor de ay2: '))
bx1 = int(input('Digite o valor de bx1: '))
by1 = int(input('Digite o valor de by1: '))
bx2 = int(input('Digite o valor de bx2: '))
by2 = int(input('Digite o valor de by2: '))

area1 = abs(ax2 - ax1) * abs(ay2 - ay1)
area2 = abs(bx2 - bx1) * abs(by2 - by1)

inter_x = 0
inter_y = 0

for x1 in range(ax1, ax2+1):
    for x2 in range(bx1, bx2+1):
        if x1 == x2:
            inter_x += 1


for y1 in range(ay1, ay2+1):
    for y2 in range(by1, by2+1):
        if y1 == y2:
            inter_y += 1


if (inter_x <= 0) or (inter_y <= 0):
    area_intercessao = (inter_x) * (inter_y) # = 0
else:
    area_intercessao = (inter_x - 1) * (inter_y - 1)

area_total = (area1 + area2) - area_intercessao

print(area_total)