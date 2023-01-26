#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Dada a seguinte lista:

#    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#    Mostre-me as seguintes listas:

#    Intervalo de 1 a 9
#    Intervalo de 8 a 13
#    Números pares
#    Números ímpares
#    Todos os múltiplos de 2, 3 e 4
#    Lista reversa
#    Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float.

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(lista[1:10])
print(lista[8:14])
print(lista[::2])
print(lista[1::2])
print(lista[2::2])
print(lista[::-1])
print(f'{sum(lista[10:16])/sum(lista[3:10]):.2f}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

# Exemplo
#lista = [9, 15, 2, 33, 1]

lista = []

for i in range(5):
   lista.append(input(f'Digite um número inteiro (posição {i+1}): '))

for i in lista:
    print(f'Elemento: {i} - Posição: {lista.index(i)}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Ler uma lista de 10 números reais e mostre-os na ordem inversa.

# Exemplo
# lista = [-1, 45.2, 3, (1/3), -0.5, 41.0, 2, (2**(1/2)), 39, -10]

lista = []
for i in range(10):
   lista.append(input('Digite um número real: '))

print(lista[::-1])


#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

# Exemplo
# notas = [7.2, 4.4, 9.1, 3]

notas = []

for i in range(4):
   notas.append(input(f'Digite a nota {i+1}: '))

print(f'Média: {sum(notas)/len(notas):.2f}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. Ler uma lista com 20 idades e exibir a maior e menor.

# Exemplo
# idades = [8, 7, 97, 100, 14, 32, 35, 84, 12, 73, 20, 55, 27, 17, 67, 45, 15, 91, 52, 66]

idades = []
for i in range(20):
   idades.append(input(f'Digite a idade (i+1): '))

print(f'Menor: {min(idades)}')
print(f'Maior: {max(idades)}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma
#    lista IMPAR. Imprima as listas PAR e IMPAR.

lista = [96, 97, 15, 24, 1, 78, 54, 44, 101, 50, 2, 30, 79, 44, 76, 38, 68, 63, 3, 0]

par = [par for par in lista if ((par % 2) == 0)]
impar = [impar for impar in lista if ((impar % 2) != 0)]

print(par)
print(impar)


#-----------------------------------------------------------------------------------------------------------------------------------#
# 7. Faça um programa que leia um número indeterminado de notas. Após esta entrada de dados, faça o seguinte:

#    Mostre a quantidade de notas que foram lidas.
#    Exiba todas as notas na ordem em que foram informadas.
#    Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
#    Calcule e mostre a soma das notas.
#    Calcule e mostre a média das notas.
#    Calcule e mostre a quantidade de notas acima da média calculada.

contador_notas = 0
notas = []
nota = 0

while(nota >= 0):
    contador_notas += 1
    nota = int(input(f'Informe a nota {contador_notas}: '))
    notas.append(nota)

notas.pop()

media = sum(notas) / len(notas)

print(f'Quantidade de notas: {len(notas)}')

print(f'Notas: {notas}')

for nota in notas[::-1]:
    print(f'Nota: {nota}')

print(f'A soma das notas é: {sum(notas)}')

print(media)

print(
    f'As notas acima da média são: {[nota_acima_media for nota_acima_media in notas if (nota_acima_media > media)]}')
