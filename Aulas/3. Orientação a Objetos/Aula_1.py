#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Crie uma classe Bola cujos atributos são cor e raio.

#    Crie um método que imprime a cor da bola.
#    Crie um método para calcular a área dessa bola.
#    Crie um método para calcular o volume da bola.
#    Agora crie um objeto dessa classe e calcule a área e o volume.
#    Exiba os valores para sua área e seu volume
     
#    fórmulas:
#    Área da esfera = 4 * 3.14 * raio **2
#    Volume da esfera = 4 * 3.14 * raio ** 3 / 3

class Bola:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
    
    def imprime_cor(self):
        print(self.cor)
    
    def calcula_area(self):
        area = 4 * 3.14 * self.raio ** 2
        print(f'A área é: {area}')
    
    def calcula_volume(self):
        volume = 4 * 3.14 * self.raio ** 3 / 3
        print(f'O volume é: {volume}')


#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Crie uma classe retângulo cujos atributos são lado_a e lado_b
#    crie um método para calcular a área desse retângulo
#    crie um objeto dessa classe e calcule a área e exiba o valor em seguida

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def calcula_area(self):
        area = self.lado_a * self.lado_b
        return area
    
r1 = Retangulo(10, 2)
print(r1.calcula_area())

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Crie uma classe funcionário cujos atributos sao nome e e-mail. Guarde as horas trabalhas mencionadas abaixo em um dicionário 
#    cujas chaves são o mês em questão e, em outro dicionário, guarde o salário por hora relativo ao mês em questão.

# {
#   "janeiro" : 168, 
#   "fevereiro" : 160, 
#   "março" : 184, 
#   "abril" : 168, 
#   "maio" : 176, 
#   "junho" : 176, 
#   "julho" : 168, 
#   "agosto" : 184, 
#   "setembro" : 176, 
#   "outubro" : 168, 
#   "novembro": 176, 
#   "dezembro" : 176
# }

#    hora salario:

# {
#   "janeiro": 20 , 
#   "fevereiro" : 25, 
#   "março" : 30, 
#   "abril" : 28, 
#   "maio" : 26, 
#   "junho" : 35, 
#   "julho" : 19, 
#   "agosto" : 24, 
#   "setembro" : 22, 
#   "outubro" : 20, 
#   "novembro": 21, 
#   "dezembro" : 23
# }

#    crie um método que retorna o salário mensal do funcionário
#    depois crie um objeto e aplique o método de calcular salário, retornando o valor do salário mensal

class Funcionarios:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

        self.horas_trabalhadas = {"janeiro": 168, "fevereiro" : 160, "março" : 184, "abril" : 168, "maio" : 176, "junho" : 176, 
                                  "julho" : 168, "agosto" : 184, "setembro" : 176, "outubro" : 168, "novembro": 176, "dezembro" : 176}


        self.hora_salario = {"janeiro": 20 , "fevereiro" : 25, "março" : 30, "abril" : 28, "maio" : 26, "junho" : 35, 
                             "julho" : 19, "agosto" : 24, "setembro" : 22, "outubro" : 20, "novembro": 21, "dezembro" : 23}
    
    def salario_mensal(self, mes):
        if mes.lower() in list(self.hora_salario.keys()):
            return self.horas_trabalhadas[mes.lower()] * self.hora_salario[mes.lower()]

f1 = Funcionarios('Valter', 'valter@email.com')
print(f1.salario_mensal('junho'))

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Crie uma classe televisor cujos atributos são:

#    fabricante
#    modelo
#    canal atual
#    lista de canais: No atributo lista de canais, devem estar armazenados todos os canais já registrados dessa TV.
#    volume

#    faça métodos para:
     
#    aumentar/diminuir volume
#       o volume não pode ser menor que zero e maior que cem

#    trocar o canal
#       só se pode trocar para um canal que já esteja na lista de canais

#    sintonizar um novo canal
#       adiciona um novo canal à lista de canais somente se esse canal não estiver nessa lista.

class Televisor:
    def __init__(self, fabricante, modelo, canal_atual, lista_canais, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_canais = lista_canais
        self.volume = volume

    def aumentar_diminuir_volume(self, novo_volume):
        if 0 <= novo_volume > 100:
            return
        else:
            self.volume = novo_volume
        
    def trocar_canal(self, canal):
        if canal not in self.lista_canais:
            return
        else:
            self.canal_atual = canal
    
    def sintonizar_novo_canal(self, novo_canal):
        if novo_canal in self.lista_canais:
            return
        else:
            self.lista_canais.append(novo_canal)


#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. Crie uma classe controle remoto cujo atributo é televisão, isso é, recebe um objeto da classe do exercício 4.
#    Crie métodos para:
#       aumentar/diminuir volume;
#       trocar o canal;
#       sintonizar um novo canal, que adiciona um novo canal à lista de canais - somente se esse canal não estiver nessa lista

class ControleRemoto:
    def __init__(self, Televisor):
        self.Televisor = Televisor

    def aumentar_diminuir_volume(self, novo_volume):
        self.Televisor.aumentar_diminuir_volume(novo_volume)
        
    def trocar_canal(self, canal):
        if canal not in self.lista_canais:
            return
        else:
            self.Televisor.trocar_canal(canal)
    
    def sintonizar_novo_canal(self, novo_canal):
        if novo_canal in self.Televisor.lista_canais:
            return
        else:
            self.Televisor.sintonizar_novo_canal(novo_canal)


#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. O módulo time possui a função time.sleep(x), que faz seu programa "dormir" por x segundos. utilizando essa função, crie uma 
#    classe contagem e faça um objeto que conte o tempo

from time import sleep

class Contagem:
    def __init__(self, contador):
        sleep(contador)