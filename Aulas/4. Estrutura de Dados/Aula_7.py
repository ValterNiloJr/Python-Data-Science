# -----------------------------------------------------------------------------------------------------------------------------------#
# 1. Implemente o grafo ilustrado pela figura abaixo utilizando networkx. Em seguida, responda as seguintes questões:
#    
#       quantos nós tem o grafo?
#       quantas arestas tem o grafo?
#       imprima sua matriz de adjacência
#       imprima sua lista de adjacência
#       qual o grau de cada nó?
#       qual a medida de centralidade por grau de cada nó?
#       qual a medida de centralidade por proximidade de cada nó?
#       qual a medida de centralidade por intermediação de cada nó?

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(1, 3)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 6)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(5, 2)

pos = nx.spring_layout(g, seed=65)

nx.draw_networkx(g, pos)

labels = nx.get_edge_attributes(g, 'weigh')

nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.show()

# 7 nós
print('Nós: ', len(g.nodes()))

# 7 arestas
print('Arestas: ', len(g.edges()))

# Matriz de adjacência
print(nx.adjacency_matrix(g).todense())

# Lista de adjacência
print(list(g.adjacency()))

# gaus de cada nó
print(g.degree())

# centralidade por grau
print(nx.degree_centrality(g))

# centralidade por proximidade
print(nx.closeness_centrality(g))

# centralidade por intermediação
print(nx.betweenness_centrality(g))



# -----------------------------------------------------------------------------------------------------------------------------------#
# 2. Implemente o grafo ilustrado pela figura abaixo utilizando networkx. Em seguida, responda as seguintes questões:

#       quantos nós tem o grafo?
#       quantas arestas tem o grafo?
#       imprima sua matriz de adjacência
#       imprima sua lista de adjacência
#       qual o grau de cada nó?
#       qual a medida de centralidade por grau de cada nó?
#       qual a medida de centralidade por proximidade de cada nó?
#       qual a medida de centralidade por intermediação de cada nó?

import matplotlib.pyplot as plt
import networkx as nx

g = nx.DiGraph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)

g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 2)
g.add_edge(4, 4)
g.add_edge(5, 2)

pos = nx.spring_layout(g, seed=40)

nx.draw_networkx(g, pos)

labels = nx.get_edge_attributes(g, 'weigh')

nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.show()

# 5 nós
print('Nós: ', len(g.nodes()))

# 7 arestas
print('Arestas: ', len(g.edges()))

# Matriz de adjacência
print(nx.adjacency_matrix(g).todense())

# Lista de adjacência
print(list(g.adjacency()))

# gaus de cada nó
print(g.degree())

# centralidade por grau
print(nx.degree_centrality(g))

# centralidade por proximidade
print(nx.closeness_centrality(g))

# centralidade por intermediação
print(nx.betweenness_centrality(g))

# -----------------------------------------------------------------------------------------------------------------------------------#
# 3. Implemente o grafo ilustrado pela figura abaixo utilizando networkx. Em seguida, responda as seguintes questões:

#       quantos nós tem o grafo?
#       quantas arestas tem o grafo?
#       imprima sua matriz de adjacência
#       imprima sua lista de adjacência
#       qual o grau de cada nó?
#       qual a medida de centralidade por grau de cada nó?
#       qual a medida de centralidade por proximidade de cada nó?
#       qual a medida de centralidade por intermediação de cada nó?
#       resolva o PCV com a melhor rota passando por todos nós

import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(0, 1, weigh=3)
g.add_edge(0, 3, weigh=7)
g.add_edge(0, 4, weigh=8)
g.add_edge(1, 3, weigh=4)
g.add_edge(1, 2, weigh=1)
g.add_edge(2, 3, weigh=2)
g.add_edge(3, 4, weigh=3)

pos = nx.spring_layout(g, seed=40)

nx.draw_networkx(g, pos)

labels = nx.get_edge_attributes(g, 'weigh')

nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.show()

# 5 nós
print('Nós: ', len(g.nodes()))

# 7 arestas
print('Arestas: ', len(g.edges()))

# Matriz de adjacência
print(nx.adjacency_matrix(g).todense())

# Lista de adjacência
print(list(g.adjacency()))

# gaus de cada nó
print(g.degree())

# centralidade por grau
print(nx.degree_centrality(g))

# centralidade por proximidade
print(nx.closeness_centrality(g))

# centralidade por intermediação
print(nx.betweenness_centrality(g))

# PCV com a melhor rota passando por todos nós
pcv = nx.approximation.traveling_salesman_problem
print('O caminho mais curto é: ', pcv(g))


# -----------------------------------------------------------------------------------------------------------------------------------#
# Desafio :  grafo dos estados do Brasil é definido da seguinte forma:

#   Cada vértice é um dos estados estados da República Federativa do Brasil
#   Dois estados são adjacentes se têm uma fronteira comum

#       Implemente o grafo no networkx e responda:
#       
#       quantos nós tem o grafo?
#       quantas arestas tem o grafo?
#       imprima sua matriz de adjacência
#       imprima sua lista de adjacência
#       qual o grau de cada nó?
#       qual a medida de centralidade por grau de cada nó?
#       qual a medida de centralidade por proximidade de cada nó?
#       qual a medida de centralidade por intermediação de cada nó?
#       qual a melhor rota entre Paraná e Pará?
#       qual a melhor rota entre RN e RS?
#       resolva o PCV, definindo a melhor rota se tiver que passar pelos pontos: ES, MS, BA, CE, AM, TO e SP
#       você consegue plotar o grafo de forma parecida com o real formato do Brasil?

# Ainda não tive tempo para implemetar :/