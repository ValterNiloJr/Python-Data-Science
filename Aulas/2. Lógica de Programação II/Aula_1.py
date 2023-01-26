#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Defina duas tuplas: uma com nomes de comida (pelo menos 5 nomes) e outra com os preços das comidas - preservando a ordem. 
#    Mostre no standard output a relação de comida-preço.

tupla_nomes = ('Kiwi', 'Manga', 'Atemoia', 'Goiaba', 'Ameixa')
tupla_precos = (3.6, 2, 7.7, 3.8, 4.2)

for nome, preco in zip(tupla_nomes, tupla_precos):
    print(f'Nome: {nome} | Preço: R${preco}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Agora, ainda com as tuplas acima, pegue apenas o nome e o preço das três comidas no meio da tupla. (considere "meio da lista" 
#    como sendo, por exemplo: ('A', 'B', 'C', 'D', 'E') --> ('B', 'C', 'D').

tupla_nomes = ('Kiwi', 'Manga', 'Atemoia', 'Goiaba', 'Ameixa')
tupla_precos = (3.6, 2, 7.7, 3.8, 4.2)

for nome, preco in zip(tupla_nomes[1:-1], tupla_precos[1:-1]):
    print(f'Nome: {nome} | Preço: {preco}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Defina uma tupla com pelo menos cinco valores e mostre no standar output esta tupla invertida. (exemplo, (1, 2, 3, 4) --> (4, 3, 2, 1)

tupla_valores = (1, 2, 3, 4, 5)

print(tupla_valores[::-1])

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Dada a seguinte tupla: (('a', 23),('b', 37),('c', 11), ('d',29)). Ordene esta tupla de acordo com o segundo item.

# tupla_entrada = (('a', 23),('b', 37),('c', 11), ('d', 29))

# tupla_entrada = list(tupla_entrada)

# for indice, tupla in enumerate(tupla_entrada):
#     tupla_entrada[indice] = list(tupla_entrada[indice])


# tupla= list((('a', 23),('b', 37),('c', 11), ('d',29)))
# tupla_ordenada = tuple(sorted(tupla, key=lambda item: item[1]))
# print(tupla_ordenada)

# tupla_input = (('a', 23),('b', 37),('c', 11), ('d',29))
# lista_input = []

# for tupla in tupla_input:
#   lista_input.append(list(tupla[::-1]))

# lista_input = sorted(lista_input)

# # print(lista_input)

# lista_output = []
# for lista in lista_input:
#   lista_output.append(tuple(lista[::-1]))

# tupla_output = tuple(lista_output)

# print(lista_output)


#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. Defina uma tupla com pelo menos dez itens e crie uma nova tupla com apenas os itens de índice PAR da tupla original.

tupla_dez_itens = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
tupla_nova = tupla_dez_itens[::2]
print(tupla_nova)


#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. Defina uma tupla com pelo menos cinco valores e mostre quantas vezes cada elemento se repete.

tupla_valores = (1, 2, 3, 1, 4, 5)

for valor in set(tupla_valores):
    print(f'O valor {valor} se repete {tupla_valores.count(valor)} vez(es) na tupla')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 7. Defina uma tupla e calcule a soma de seus elementos.

tupla_valores = (1, 2, 3, 4, 5)

print(sum(tupla_valores))

#-----------------------------------------------------------------------------------------------------------------------------------#
# 8. Considere a lista [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]. Faça um programa que remova as tuplas de tamanho K.

def remove_items_by_len(tuple_list, k):
    tuple_list = [not_remove for not_remove in tuple_list if len(not_remove) != k]
    return tuple_list
        
lista_tuplas = [(4, 5), (4, ), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

lista_tuplas_removidas = remove_items_by_len(lista_tuplas, 1)

print(lista_tuplas_removidas)
