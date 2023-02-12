# -----------------------------------------------------------------------------------------------------------------------------------#
# 1. Sobre filas

#    Escreva um programa que simule a distribuição de um grupo de pessoas em 2 filas de atendimento, prioritária ou regular, e
#    consequentemente o atendimento delas. O programa deve obedecer às seguintes regras:

#    O grupo deve conter 20 pessoas
#    Cada pessoa pode ser alocada em uma fila prioritária ou regular, com probabilidades de 30% e 70%, reespectivamente
#    1 pessoa da fila regular deve ser atendida a cada 3 pessoas da fila prioritária
#    Não havendo prioridades, as pessoas da fila regular podem ser atendidas
#    import random
#    random.choices(population=opções, weights=probabilidades, k=quantidades)

import random

class Fila:
    def __init__(self):
        self.__fila = []

    def enfileirar(self, valor):
        self.__fila.append(valor)

    def mostrar(self):
        print(self.__fila)

    def __repr__(self):
        return str(self.__fila)

    def esta_vazia(self):
        return not len(self.__fila)

    def desenfileirar(self):
        if self.esta_vazia():
            print('A fila está vazia!')
            return None

        return self.__fila.pop(0)

    def ver_inicio(self):
        if self.esta_vazia():
            print('A fila está vazia!')
            return None

        return self.__fila[0]


opcoes = ['Regular', 'Prioritario']
probabilidades = [0.7, 0.3]
quantidade = 20

random.seed(10)

pacientes = random.choices(
    population=opcoes, weights=probabilidades, k=quantidade)

regular = Fila()
prioritario = Fila()

for indice, tipo in enumerate(pacientes):
    if tipo == 'Regular':
        regular.enfileirar(indice)
    else:
        prioritario.enfileirar(indice)

print('Fila regular', end=' ')
regular.mostrar()
print('\nFila prioritaria', end=' ')
prioritario.mostrar()
print()
# print(regular.esta_vazia())

PRIORIDADE_MAX = 3

while (not regular.esta_vazia() or not prioritario.esta_vazia()):
    for i in range(PRIORIDADE_MAX):
        if prioritario.esta_vazia():
            break
        else:
            paciente_atendido = prioritario.desenfileirar()
            print('Paciente da fila prioritaria atendido: ', paciente_atendido)
    if regular.esta_vazia():
        break
    else:
        paciente_atendido = regular.desenfileirar()
        print('Paciente da fila regular atendido: ', paciente_atendido)

# -----------------------------------------------------------------------------------------------------------------------------------#
# 2. Sobre pilhas

#    Escreva um programa que gere 50 números inteiros randômicos entre 0 e 100. Para cada número gerado, verifique as seguintes
#    regras:

#    se o número for par, empilhe na pilha chamada par;
#    se o número for ímpar, empilhe na pilha chamada ímpar;
#    se o número for 0, 10, 50 ou 100, desempilhe um elemento de cada pilha. Caso a pilha esteja vazia, mostre uma mensagem de fila
#    vazia na tela.
#    Ao termino do programa, desempilhe todos os elementos das duas pilhas, imprimindo-os na tela.

import random

class Pilha:
    def __init__(self):
        self.__pilha = []

    def empilhar(self, valor):
        self.__pilha.append(valor)

    def mostrar(self):
        print(self.__pilha)

    def esta_vazia(self):
        return not len(self.__pilha)

    def desempilhar(self):
        if self.esta_vazia():
            print('A pilha está vazia!')
            return None

        return self.__pilha.pop()

    def ver_topo(self):
        if self.esta_vazia():
            print('A pilha está vazia!')
            return None

        return self.__pilha[-1]

quantidade = 50
numeros = random.sample(range(101), quantidade)

print('Numeros: ', numeros)

DESENPILHAR = [0, 10, 50, 100]

par = Pilha()
impar = Pilha()

for numero in numeros:
    if numero in DESENPILHAR:
        print('\nNumero: ', numero)

        print('Pilha de pares:', end=' ')
        par.mostrar()
        print('Pilha de impares:', end=' ')
        impar.mostrar()
        
        print('\nItem desempilhado de par: ' ,par.desempilhar())
        print('Item desempilhado de impar: ' ,impar.desempilhar())

    elif ((numero % 2) == 0):
        par.empilhar(numero)

    else:
        impar.empilhar(numero)

print('\nRestantes:')
print('Pilha de pares:', end=' ')
par.mostrar()
print('Pilha de impares:', end=' ')
impar.mostrar()

while (not par.esta_vazia() and not impar.esta_vazia()):
    if not par.esta_vazia():
        item = par.desempilhar()
        print(f'Desempilhando o item: {item} de par')
    
    if not impar.esta_vazia():
        item = impar.desempilhar()
        print(f'Desempilhando o item: {item} de impar')


# -----------------------------------------------------------------------------------------------------------------------------------#
# 3. Sobre listas encadeadas e pilhas

#    Refatore a implementação de pilhas, utilizando listas encadeadas como estrutura de dados, ao invés de listas ou arrays.

import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __repr__(self):
        return str(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def esta_vazia(self):
        return self.primeiro == None

    def mostrar(self):
        if self.esta_vazia():
            print('A lista está vazia!')

        no_atual = self.primeiro
        while no_atual != None:
            print(no_atual)
            no_atual = no_atual.proximo

    def mostrar_cadeia(self):
        if self.esta_vazia():
            print('A lista está vazia!')

        s = ''
        no_atual = self.primeiro
        while no_atual:
            s += str(no_atual.valor) + '-> '
            no_atual = no_atual.proximo
        return s

    def pesquisar(self, valor):
        if self.esta_vazia():
            print("A lista está vazia!")
            return None

        no_atual = self.primeiro
        while no_atual.valor != valor:
            if no_atual.proximo == None:
                return None
            else:
                no_atual = no_atual.proximo

        return no_atual

    def pesquisar_primeiro(self):
        if self.esta_vazia():
            print("A lista está vazia!")
            return None

        return self.primeiro

    def remover(self, valor):
        if self.esta_vazia():
            print('A lista está vazia!')
            return None

        no_atual = self.primeiro
        no_anterior = self.primeiro
        while no_atual.valor != valor:
            if no_atual.proximo == None:
                return None
            else:
                no_anterior = no_atual
                no_atual = no_atual.proximo

        if no_atual == self.primeiro:
            self.primeiro = no_atual.proximo
        else:
            no_anterior.proximo = no_atual.proximo

        return no_atual

    def remover_primeiro(self):
        if self.esta_vazia():
            print('A lista está vazia!')
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp


class Pilha:
    def __init__(self):
        self.__pilha = ListaEncadeada()

    def empilhar(self, valor):
        self.__pilha.inserir(valor)

    def mostrar(self):
        print(self.__pilha.mostrar())

    def esta_vazia(self):
        if self.__pilha.esta_vazia():
            return True
        else:
            return False

    def desempilhar(self):
        if self.esta_vazia():
            print('A pilha está vazia!')
            return None

        return self.__pilha.remover_primeiro().valor

    def ver_topo(self):
        if self.esta_vazia():
            print('A pilha está vazia!')
            return None

        return self.__pilha.pesquisar_primeiro().valor


nova_pilha = Pilha()

for i in range(5):
    valor = random.randint(1, 10)
    nova_pilha.empilhar(valor)

nova_pilha.mostrar()

print(nova_pilha.desempilhar())

# -----------------------------------------------------------------------------------------------------------------------------------#
# 4. Sobre deques

#    Com base na teoria de deques e nas implementações de filas e pilhas, faça a implementação da estrutura de deques.

import random

class Deque:
    def __init__(self):
        self.__deque = []

    def inserir_inicio(self, valor):
        self.__deque.insert(0, valor)

    def inserir_fim(self, valor):
        self.__deque.append(valor)

    def mostrar(self):
        print(self.__deque)

    def __repr__(self):
        return str(self.__deque)

    def esta_vazia(self):
        return not len(self.__deque)

    def remover_inicio(self):
        if self.esta_vazia():
            print('A deque está vazia!')
            return None

        return self.__deque.pop(0)

    def remover_fim(self):
        if self.esta_vazia():
            print('A deque está vazia!')
            return None

        return self.__deque.pop()

    def ver_inicio(self):
        if self.esta_vazia():
            print('A deque está vazia!')
            return None

        return self.__deque[0]

    def ver_fim(self):
        if self.esta_vazia():
            print('A deque está vazia!')
            return None

        return self.__deque[-1]



deque = Deque()

for i in range(4):
    valor = random.randint(1, 10)
    deque.inserir_inicio(valor)

deque.mostrar()
