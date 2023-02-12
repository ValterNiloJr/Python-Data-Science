# -----------------------------------------------------------------------------------------------------------------------------------#
# 1. Implemente o método de busca de um elemento da árvore.

# cria a classe nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostrar_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes_esq = []
        self.ligacoes_dir = []

    def esta_vazia(self):
        if self.raiz == None:
            return True
        else:
            return False

    def inserir(self, valor):
        novo_no = No(valor)

        if self.esta_vazia():
            self.raiz = novo_no

        else:
            atual = self.raiz
            while True:
                # observar para a esquerda
                if valor < atual.valor:
                    if atual.esquerda == None:
                        atual.esquerda = novo_no
                        ligacao = str(atual.valor) + '->' + str(novo_no.valor)
                        self.ligacoes_esq.append(ligacao)
                        break
                    else:
                        atual = atual.esquerda

                # observar para direita
                elif valor > atual.valor:
                    if atual.direita == None:
                        atual.direita = novo_no
                        ligacao = str(atual.valor) + '->' + str(novo_no.valor)
                        self.ligacoes_dir.append(ligacao)
                        break
                    else:
                        atual = atual.direita

                else:
                    print('Nó com este valor já existe!')
                    break

    def visualizar(self):
        print(self.ligacoes_esq + self.ligacoes_dir)

    def buscar(self, valor):
        # se vazio, retorna None
        if self.esta_vazia():
            print('A árvore está vazia!')
            return None

        # a partir da raiz, verifica os nós enquanto
        # for diferente do valor procurado
        atual = self.raiz
        while atual.valor != valor:
            # observa se valor está para esquerda e atualiza o nó
            if valor < atual.valor:
                atual = atual.esquerda

            # observa se valor está para direita e atualiza o nó
            else:
                atual = atual.direita

            # ao chegar no fim e não encontrar o valor
            if atual == None:
                print('Valor não encontrado!')
                return None

        # ao encontrar, retorna o nó
        return atual


arvore = ArvoreBinariaBusca()

arvore.inserir(7)
arvore.inserir(3)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(2)
arvore.inserir(17)
arvore.inserir(13)
arvore.inserir(18)
arvore.inserir(15)
arvore.inserir(20)

arvore.visualizar()

# buscando um nó existente
print(vars(arvore.buscar(18)))

# buscando um nó não existente
arvore.buscar(30)

# -----------------------------------------------------------------------------------------------------------------------------------#
# 2. Implemente o método de remoção de um elemento da árvore para os seguintes cenários:

#    nó é uma folha
#    nó tem apenas 1 filho
#    nó com 2 filhos (não precisa implementar)

import graphviz as gz

# cria a classe nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostrar_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes_esq = []
        self.ligacoes_dir = []
        self.ligacoes = []

    def esta_vazia(self):
        if self.raiz == None:
            return True
        else:
            return False

    def inserir(self, valor):
        novo_no = No(valor)

        if self.esta_vazia():
            self.raiz = novo_no

        else:
            atual = self.raiz
            while True:
                # observar para a esquerda
                if valor < atual.valor:
                    if atual.esquerda == None:
                        atual.esquerda = novo_no
                        ligacao = str(atual.valor) + '->' + str(novo_no.valor)
                        self.ligacoes_esq.append(ligacao)
                        break
                    else:
                        atual = atual.esquerda

                # observar para direita
                elif valor > atual.valor:
                    if atual.direita == None:
                        atual.direita = novo_no
                        ligacao = str(atual.valor) + '->' + str(novo_no.valor)
                        self.ligacoes_dir.append(ligacao)
                        break
                    else:
                        atual = atual.direita

                else:
                    print('Nó com este valor já existe!')
                    break

    def visualizar(self):
        g = gz.Digraph('G', filename='Aula_5 - Arvore.gv')

        ligacao_esq = [i.split('->') for i in self.ligacoes_esq]
        ligacao_dir = [i.split('->') for i in self.ligacoes_dir]

        for esq in ligacao_esq:
            g.edge(*esq)
        for dir in ligacao_dir:
            g.edge(*dir)

        g.format = 'png'
        g.render(directory='Aulas/4. Estrutura de dados/', view=True)
        #g.view()

    def buscar(self, valor):
        # se vazio, retorna None
        if self.esta_vazia():
            print('A árvore está vazia!')
            return None

        # a partir da raiz, verifica os nós enquanto
        # for diferente do valor procurado
        atual = self.raiz
        while atual.valor != valor:
            # observa se valor está para esquerda e atualiza o nó
            if valor < atual.valor:
                atual = atual.esquerda

            # caso contrário está para direita
            else:
                atual = atual.direita

            # ao chegar no fim e não encontrar o valor
            if atual == None:
                print('Valor não encontrado!')
                return None

        # ao encontrar, retorna o nó
        return atual

    def remover(self, valor):
        # se vazio, retorna None
        if self.esta_vazia():
            print('A árvore está vazia!')
            return None

        atual = self.raiz  # irá receber o nó que desejamos remover
        pai = self.raiz  # irá receber o nó pai do que iremos remover
        # verifica se viemos do nó pai pela esquerda (True) ou
        bool_esquerda = True
        # pela direita (False)

        # a partir da raiz, verifica os nós enquanto
        # for diferente do valor procurado
        while atual.valor != valor:
            pai = atual  # pai recebe valor do atual

            # observamos se o valor está à esquerda
            if valor < atual.valor:
                atual = atual.esquerda
                bool_esquerda = True

            # caso contrário está para direta
            else:
                atual = atual.direita
                bool_esquerda = False

            # se o valor não existir retorna None
            if atual == None:
                print('Valor não encontrado!')
                return None

        # Verfifica se o nó a ser apagado é uma folha
        if atual.esquerda == None and atual.direita == None:
            # se a folha é a raiz
            if atual == self.raiz:
                self.raiz = None

            # se não for raiz e veio da esquerda
            elif bool_esquerda:
                self.ligacoes_esq.remove(
                    str(pai.valor) + '->' + str(atual.valor))
                pai.esquerda = None

            # se não for raiz e veio da direita
            else:
                self.ligacoes_dir.remove(
                    str(pai.valor) + '->' + str(atual.valor))
                pai.direita = None

        # Verifica se o nó a ser apagado não possui filho na direita
        elif atual.direita == None:

            # verfica se o nó a ser apagado é a raiz
            if atual == self.raiz:
                self.raiz = atual.esquerda
                self.ligacoes_esq.remove(
                    str(atual.valor) + '->' + str(atual.esquerda.valor))

            # verfica se o nó a ser apagado veio da esquerda do pai
            elif bool_esquerda:
                self.ligacoes_esq.remove(
                    str(pai.valor) + '->' + str(atual.valor))
                self.ligacoes_esq.remove(
                    str(atual.valor) + '->' + str(atual.esquerda.valor))
                pai.esquerda = atual.esquerda
                self.ligacoes_esq.append(
                    str(pai.valor) + '->' + str(atual.esquerda.valor))

            # verfica se o nó a ser apagado veio da direita do pai
            else:
                self.ligacoes_dir.remove(
                    str(pai.valor) + '->' + str(atual.valor))
                self.ligacoes_esq.remove(
                    str(atual.valor) + '->' + str(atual.esquerda.valor))
                pai.direita = atual.esquerda
                self.ligacoes_dir.append(
                    str(pai.valor) + '->' + str(atual.esquerda.valor))

        # Verifica se o nó a ser apagado não possui filho na esquerda
        elif atual.esquerda == None:

            # verfica se o nó a ser apagado é a raiz
            if atual == self.raiz:
                self.raiz = atual.direita
                self.ligacoes_dir.remove(
                    str(atual.valor) + '->' + str(atual.direita.valor))

            # verfica se o nó a ser apagado veio da esquerda do pai
            elif bool_esquerda:
                self.ligacoes_esq.remove(
                    str(pai.valor) + '->' + str(atual.valor))
                self.ligacoes_dir.remove(
                    str(atual.valor) + '->' + str(atual.direita.valor))
                pai.esquerda = atual.direita
                self.ligacoes_esq.append(
                    str(pai.valor) + '->' + str(atual.direita.valor))

            # verfica se o nó a ser apagado veio da direita do pai
            else:
                self.ligacoes_dir.remove(
                    str(pai.valor) + '->' + str(atual.valor))
                self.ligacoes_dir.remove(
                    str(atual.valor) + '->' + str(atual.direita.valor))
                pai.direita = atual.direita
                self.ligacoes_dir.append(
                    str(pai.valor) + '->' + str(atual.direita.valor))


arvore = ArvoreBinariaBusca()

arvore.inserir(7)
arvore.inserir(3)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(2)
arvore.inserir(17)
arvore.inserir(13)
arvore.inserir(18)
arvore.inserir(15)

arvore.visualizar()

# removendo uma folha
arvore.remover(15)

arvore.visualizar()

# removendo un nó com um filho
arvore.remover(4)

arvore.visualizar()

# Desafio: Utilizando a biblioteca graphviz, refatore o método de visualização plotando a estrutura da árvore criada.

# Desafio concluido!