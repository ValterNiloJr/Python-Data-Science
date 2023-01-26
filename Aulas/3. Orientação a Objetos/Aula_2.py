"""
Crie uma modelagem de classes para uma agenda capaz de armazenas contatos. Através dessa agenda é possível:

incluir
remover
buscar
listar contatos já cadastrados
"""

class Contatos:
  def __init__(self, lista_contatos):
    self.lista_contatos = lista_contatos

  def inclui(self, contato):
    if contato not in self.lista_contatos:
      self.lista_contatos.append(contato)
  
  def remove(self, contato):
    if contato in self.lista_contatos:
      self.lista_contatos.remove(contato)

  def busca(self, contato):
    if contato in self.lista_contatos:
      print(f'{contato} encontrado!')
    else:
      print(f'{contato} não encontrado!')
      
  def lista(self):
    for contato in self.lista_contatos:
      print(contato)

"""
crie uma classe cliente cujos atributos são nome, idade e e-mail. construa um método que imprima as informações tal como abaixo:

nome : joao da silva
idade : 50
email: joao@gmail.com

"""
class Cliente:
  def __init__(self, nome, idade, email):
    self.nome = nome
    self.idade = idade
    self.email = email

  def imprimir(self):
    print(f'nome: {self.nome}')
    print(f'idade: {self.idade}')
    print(f'email: {self.email}')

