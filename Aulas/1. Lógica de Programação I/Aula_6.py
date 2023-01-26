#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Dado um número inteiro positivo, retorne o número de inteiros positivos menor ou igual a num cujas somas de dígitos são pares.

# A soma dos dígitos de um inteiro positivo é a soma de todos os seus dígitos.

# Exemplo 1:

# Entrada: num = 4

# Saída: 2

# Explicação: Os únicos inteiros menores ou iguais a 4 cujas somas de dígitos são pares são 2 e 4.

# Exemplo 2:

# Entrada: num = 30

# Saída: 14

# Explicação: Os 14 inteiros menores ou iguais a 30 cujas somas de dígitos são pares são 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26 e 28.

num = int(input('Digite um número inteiro positivo: '))
soma = 0
for i in range(num):
    if (((i % 2) == 0) and (i != 0)):
        soma += 1
        print(i, end=' ')
print(f'\nA soma é de {soma}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Dado um inteiro x com sinal, retorne x com seus dígitos invertidos.

# Exemplo 1:

# Entrada: x = 123

# Saída: 321

# Exemplo 2:

# Entrada: x = -123

# Saída: -321

num = int(input('Digite um número inteiro: '))
num_inverso = 0

if num < 0:
    num_inverso = int(str(abs(num))[::-1]) * -1
else:
    num_inverso = int(str(num)[::-1])

print(num_inverso)
