#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Criar função de busca binária e comparar com os outros metodos de busca.

#    Essa função vai olhar para nossa lista ordenada e comparar nosso item com o meio da lista, a depender do resultado da comparação,
#    a busca será feito na metade superior ou inferior.

#    E se o item não estiver na lista e a lista for imensa?

import random
lista = [i for i in range(50000000)]

encontrar = 3500000


def busca_binaria(lista, item):
    if item > lista[-1] or item < 0:
        return False

    inf = 0     # Limite inferior
    sup = len(lista) - 1    # Limite superior

    # Condição apenas para garantir a parada do while, pois com a condição (linha 15) já retorna caso o 'item' esteja fora dos limites
    while inf <= item <= sup:

        meio = (sup + inf) // 2

        if item == lista[inf] or item == lista[sup]:
            return True
        elif item < lista[meio]:
            sup = meio
        else:
            inf = meio


print(busca_binaria(lista, encontrar))


#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Criar uma função no python para implementar o Shell sort:

def shell_sort(lista):

    n = len(lista)

    #gaps = [701, 301, 132, 57, 23, 10, 4, 1] # Sequência de intervalo Ciura
    gaps = [i for i in range(n//2, 0, -1)]

    for gap in gaps:
        for i in range(gap, n):
            j = i
            while j < n:
                k = j - gap
                while k >= 0:
                    if lista[k+gap] >= lista[k]:
                        break
                    else:
                        lista[k+gap], lista[k] = lista[k], lista[k+gap]
                    k -= gap
                j += 1
            
    return lista


def criar_lista_no_order(size: int):
    randomlist = random.sample(range(1, size+1), size)
    print("Lista sem ordem:", randomlist)
    return randomlist


print("Lista com ordem:",shell_sort(criar_lista_no_order(10)))
