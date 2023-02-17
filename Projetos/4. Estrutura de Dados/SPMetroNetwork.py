import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# python library to handle input strings
from unidecode import unidecode

COLORS = {
    'AMARELA': 'yellow',
    'AZUL': 'blue',
    'CORAL': 'orange',
    'DIAMANTE': 'gray',
    'ESMERALDA': 'lightgreen',
    'JADE': 'green',
    'LILAS': 'blueviolet',
    'PRATA': 'darkgray',
    'RUBI': 'purple',
    'SAFIRA': 'darkblue',
    'TURQUESA': 'lightblue',
    'VERDE': 'darkgreen',
    'VERMELHA': 'red',
}

class Grafo:
    def __init__(self, V, E):
        self.G = nx.Graph()
        self.G.add_nodes_from(V)
        self.G.add_edges_from(E)
    
    # Private function
    def __find_best_path(self, node1, node2):
        node1_exists = self.G.has_node(node1)
        node2_exists = self.G.has_node(node2)
       
        if node1_exists and node2_exists:
            possible_path = nx.has_path(self.G, node1, node2)
            if possible_path:
                return nx.shortest_path(self.G, node1, node2)
        else:
            if not node1_exists:
                print('\n> A estação de partida não foi encontrada!')
            if not node2_exists:
                print('\n> A estação de chegada não foi encontrada!')
            return None
        
    def show_best_path(self, node1, node2, in_list=False, in_graph=False):
        self.best_path = self.__find_best_path(node1, node2)
        if self.best_path != None:
            if in_list:
                print('> O melhor caminho encontrado entre as estações foi:\n')
                for num, station in enumerate(self.best_path):
                    print(f'{num+1:2}. {station}')
            if in_graph:
                self.plot(is_best_path=True)
        else:
            print('\n> Infelizmente nenhum caminho foi encontrado!')

    def show_lists(self, lines=False, stations=False):
        if lines:
            line_names = list(set([node[1]['line_name'] for node in list(self.G.nodes.data())]))
            line_names.sort()
            print('\n> Nomes das linhas:')
            for index, name in enumerate(line_names):
                print(f'{index+1:>2}. {name}')

        if stations:
            print('\n> Nomes das estações:')
            for index, name in enumerate(self.G.nodes):
                print(f'{index+1:>3}. {name}')

    def plot(self, is_best_path=False):
        pos = nx.get_node_attributes(self.G, 'pos')

        for node in self.G.nodes.items():
            if is_best_path:
                if node[0] in self.best_path:
                    nx.draw_networkx_nodes(self.G, pos, nodelist=[node[0]], node_shape='v', node_color='red', node_size=80)
                else:
                    nx.draw_networkx_nodes(self.G, pos, nodelist=[node[0]], node_color='black', node_size=20, alpha=0.5)
            else:
                color = node[1]['line_name']
                nx.draw_networkx_nodes(self.G, pos, nodelist=[node[0]], node_color=COLORS[color], node_size=20)

        for edge in self.G.edges.items():
            # Removing final termination to evitate circules
            if edge[0][0] != edge[0][1]:
                if is_best_path:
                    if edge[0][0] in self.best_path:
                        nx.draw_networkx_edges(self.G, pos, edgelist=[edge[0]], edge_color='red')
                    else:
                        nx.draw_networkx_edges(self.G, pos, edgelist=[edge[0]], edge_color='black')
                else:
                    color = edge[1]['line_name']
                    nx.draw_networkx_edges(self.G, pos, edgelist=[edge[0]], edge_color=COLORS[color])
        if is_best_path:
            plt.title('Melhor caminho encontrado')
        else:
            plt.title('Mapa metropolitano - SP')
        plt.show()


class File:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.v = []
        self.e = []

    def get_V(self):
        for index, line in self.df.iterrows():
            station_name = line['estacao_upp']
            station_attribuits = {
                'line_name': line['nome_lin'],
                'pos': (line['long'], line['lat'])
            }
            self.v.append((station_name, station_attribuits))
        return self.v

    def get_E(self):
        for index, line in self.df.iterrows():
            self.e.append((line['estacao_upp'], line['link'],{'line_name': line['nome_lin'],}))
        return self.e

if __name__ == '__main__':

    file = File('./Projetos/4. Estrutura de Dados/metroetrem_sp_comlinks.csv')

    V = file.get_V()
    E = file.get_E()

    g = Grafo(V, E)

    while True:
        print('\nSistema Metropolitano de São Paulo:')
        print('1. Exibir mapa da linhas')
        print('2. Exibir lista linhas')
        print('3. Exibir lista estações')
        print('4. Exibir mapa do melhor caminho entre duas estações')
        print('5. Exibir lista do melhor caminho entre duas estações')
        print('6. Sair')

        try:
            user_option = int(input('\nEscolha uma das opções: '))
            if user_option == 6:
                print('\n> Até a próxima!')
                break
            elif user_option <= 0:
                print('> A opção precisa ser um valor numérico (Inteiro positivo)!')
        except ValueError:
            print('> A opção precisa ser um valor numérico!')
            continue
        
        if user_option == 1:
            g.plot()

        elif user_option == 2:
            g.show_lists(lines=True)

        elif user_option == 3:
            g.show_lists(stations=True)

        elif user_option == 4:
            node1 = unidecode(input('> Informe a estação de partida: ').strip().upper())
            node2 = unidecode(input('> Informe a estação de chegada: ').strip().upper())
            g.show_best_path(node1, node2, in_graph=True)
        
        elif user_option == 5:
            node1 = unidecode(input('> Informe a estação de partida: ').strip().upper())
            node2 = unidecode(input('> Informe a estação de chegada: ').strip().upper())
            g.show_best_path(node1, node2, in_list=True)

        else:
            continue
