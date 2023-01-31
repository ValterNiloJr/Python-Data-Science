#-----------------------------------------------------------------------------------------------------------------------------------#
# 1.  Sobre listas:

#    crie uma lista com seus top 5 filmes/séries/animações
#    imprima a quantidade de itens tem em sua lista
#    adicione um item no final
#    adicione um item na segunda posição da lista
#    remova um item pelo nome
#    remova algum item pela posição
#    ordene a lista em ordem alfabética

top = ['Interestelar', 'Diário de uma paixão',
       'Blacklist', 'La Casa de Papel', 'One Piece']

print(f'A quantidade de itens é: {len(top)}')

top.append('Star Wars')
print(f'Incrementando \'Star Wars\' no final: {top}')

top.insert(1, 'Homem de Ferro')
print(f'Incrementando \'Homem de ferro\' na 2ª posição: {top}')

top.remove('La Casa de Papel')
print(f'Removendo \'La Casa de Papel\' pelo nome: {top}')

top.pop(3)
print(f'Removendo \'Blacklist\' da 3ª posição: {top}')

top.sort()
print(f'Ordenando por ordem alfabética: {top}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Sobre tuplas:

#    Crie uma lista de compras com 5 elementos do tipo string
#    Transforme a lista em tupla
#    Imprima os 3 elementos centrais utilizando slice
#    Itere sobre os itens da tupla e imprima: o nome do item e quantas letras ele possui

compras = ['Café', 'Pão de Queijo', 'Leite', 'Kiwi', 'Chocolate']

compras = tuple(compras)

print(compras[1:4])

for item in compras:
    print(f'{item} possuí {len(item)} letras')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Sobre conjuntos:

#    Gere um conjunto com 50 números aleatórios entre 1 e 25

#    Gere um segundo conjunto com 50 números aleatórios entre 5 e 30

#    Calcule:

#       se são conjuntos disjuntos
#       a interseção
#       a união
#       a diferença simétrica

#    Para geração dos números aleatórios, utilize a lib nativa do python:

#       import random
#       random.randint(inicio, fim)

import random as rd

conj = [rd.randint(1, 26) for num in range(50)]

conj_1 = set(conj)
print(conj_1)

conj = [rd.randint(5, 30) for num in range(50)]

conj_2 = set(conj)
print(conj_2)

if (conj_1 & conj_2) != {}:
    print('Os conjuntos não são disjuntos!')
else:
    print('Os conjuntos são disjuntos!')

print(f'A interseção é: {conj_1 & conj_2}')

print(f'A união é: {conj_1 | conj_2}')

print(f'A diferença simétrica é: {conj_1 ^ conj_2}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Sobre dicionários:

#    Crie uma agenda utilizando um dicionário conforme estrutura abaixo, a agenda deve ter uma lista de 3 contatos.
#    Os contatos, além do nome, devem possuir telefone e email
#    Verifique se há algum contato com o nome 'marcos'
#    altere o telefone do primeiro contato
#    calcule quanto contatos possuem na lista

#    Estrutura do dicionário:

#    agenda = {
#        'contatos': [
#            {
#                'nome': string,
#                'tel': string,
#                'email': string
#            }
#        ]
#    }


agenda = {
    'contatos': [
        {
            'nome': 'Valter',
            'tel': '+55 (12) 34567-8910',
            'email': 'valter@email.com'
        },
        {
            'nome': 'Byanca',
            'tel': '+55 (10) 98765-4321',
            'email': 'byanca@email.com'
        },
        {
            'nome': 'Marcos',
            'tel': '+13 (55) 12345-6789',
            'email': 'marcos@email.com'
        }
    ]
}


if bool(list(filter(lambda item: item['nome'] == 'Marcos', agenda['contatos']))):
    print('Uma pessoa com o nome \'Marcos\' foi encontrado na agenda!')
else:
    print('Nenhuma pessoa com o nome \'Marcos\' foi encontrado na agenda!')

agenda['contatos'][0]['tel'] = '+00 (00) 00000-0000'
print(agenda)

print(f"Existem {len(agenda['contatos'])} contatos na agenda!")
