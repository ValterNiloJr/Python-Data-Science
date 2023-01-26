#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Escreva uma programa que imprima um dicionário onde as chaves são números de 1 a 16 e os valores são os quadrados das
#    respectivas chaves

dicionario = {i:i**2 for i in range(1,17)}

for chave, valor in zip(dicionario.keys(), dicionario.values()):
    print(f'Chave: {chave} --> Valor: {valor}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Escreva uma programa que ordene os valores dos elementos de um dicionário:
#    Exemplo:

#    Entrada: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
#    Saída: num = {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

for key, list2sort in zip(num.keys(), num.values()):
    num[key] = sorted(list2sort)

print(num)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Faça um programa que filtre um dicionário com base em seus valores. Exemplo:
#    Dicionario original:
#    {'Pessoa 01': 175, 'Pessoa 02': 180, 'Pessoa 03': 165, 'Pessoa 04': 190}
#    Pessoas com mais de 170:
#    {'Pessoa 01': 175, 'Pessoa 02': 180, 'Pessoa 04': 190}

dicionario_original = {'Pessoa 01': 175,
                       'Pessoa 02': 180, 'Pessoa 03': 165, 'Pessoa 04': 190}

print(dict(filter(lambda items: (items[1] > 170), dicionario_original.items())))

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Crie um dicionário de relatório de pagamento, cujas chaves sejam os nomes dos funcionários e os valores seus respectivos
#    salários. Faça um programa que mostre a folha de pagamento e o valor total dos salários.

import random

nomes = ['Valter', 'Nilo', 'Alcantara', 'Oliveira', 'Junior']

relatorio_pagamento = {}

for nome in nomes:
    relatorio_pagamento[nome] = random.randint(100, 10000)

for key in relatorio_pagamento:
    print(f'{key} --> R$ {relatorio_pagamento[key]}.00')