#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Existe uma linguagem de programação com apenas quatro operações e uma variável X:

#    ++X e X++ incrementam o valor da variável X em 1.
#    --X e X-- decrementa o valor da variável X em 1.
#    Inicialmente, o valor de X é 0.

#    Dado um array de strings de operações contendo uma lista de operações, retorne o valor final de X após realizar todas as operações.

#    Exemplo 1:
#    Entrada: operações = ["--X","X++","X++"]
#    Saída: 1
#    Explicação: As operações são executadas da seguinte forma:

#    Inicialmente, X = 0.
#    --X: X é decrementado em 1, X = 0 - 1 = -1.
#    X++: X é incrementado em 1, X = -1 + 1 = 0.
#    X++: X é incrementado em 1, X = 0 + 1 = 1.
#    Exemplo 2:
#    Entrada: operações = ["++X","++X","X++"]

#    Saída: 3

#    Explicação: As operações são executadas da seguinte forma:

#    Inicialmente, X = 0.
#    ++X: X é incrementado em 1, X = 0 + 1 = 1.
#    ++X: X é incrementado em 1, X = 1 + 1 = 2.
#    X++: X é incrementado em 1, X = 2 + 1 = 3.

operacoes = ["++X","++X","X++"]

X = 0

for operacao in operacoes:
    if operacao == '++X' or operacao == 'X++':
        X += 1
        print(f'{operacao}: X é incrementado em 1, X = {X-1} + 1 = {X}')
    elif operacao == '--X' or operacao == 'X--':
        X -= 1
        print(f'{operacao}: X é decrementado em 1, X = {X+1} - 1 = {X}')
    else:
        print(f'Operação \"{operacao}\" inválida!')
        break


#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Dada uma lista de inteiros 'nums', retorne o número de pares bons.

#    Um par (i, j) é considerado bom se nums[i] == nums[j] e i < j.

#    Exemplo 1:
#    Entrada: nums = [1,2,3,1,1,3]
#    Saída: 4
#    Explicação: Existem 4 pares bons (0,3), (0,4), (3,4), (2,5).

#    Exemplo 2:
#    Entrada: nums = [1,1,1,1]
#    Saída: 6
#    Explicação: Cada par na matriz é bom.


# lista = [(j, i) for i in range(n) for j in range(i)]

nums = [1,2,3,1,1,3]
pares_bons = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if (nums[i] == nums[j]):
            pares_bons.append((i, j))

print(f'Existem {len(pares_bons)} pares bons', end=' ')
for i in pares_bons:
    print(i, end=', ') if i != pares_bons[-1] else print(i, end='.')