#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Adicionando valores em um array

import numpy as np

array = np.array([])

for i in range(10):
    array = np.append(array, i)
    
array

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Uma das primeiras obras muldialmente publicadas de Dan Brown, autor do famoso Código Da Vinci, é o livro Fortaleza Digital. 
#    Neste livro, a personagem principal, Suzan Fletcher, é uma criptógrafa da NSA (National Security Agency). No livro, a personagem 
#    descreve como criar uma criptografia de forma simples :

#    Substitua cada letra do alfabeto por um número. Assim, A = 1, B = 2, C = 3 e assim por diante. Logo a palavra ADA pode ser 
#    representada por 121.
#    ADA => A = 1
#       D = 4
#       A = 1
#    Para cada letra da palavra que deseja encriptar adicione 1.
#    ADA => A = 1 + 1 = 2 --> B
#      D = 4 + 1 = 5 --> E
#      A = 1 + 1 = 2 --> B
#    Assim, a palavra ADA, codificada seria BEB.
#    Para decriptar, basta fazer o processo inverso. Representando cada letra da palavra codificada como número, subtraindo 1 e 
#    mapeando para a letra correspondente.
#    Faça um programa que receba uma entrada e aplique a criptografia como mostrada acima.
#    
#    Obs.: Considere os valores de cada letra como os valores da tabela ascii.

import numpy as np

CODE_HASH = 5

def criptografar(string):
    lista_caracteres = [ord(caracter) + CODE_HASH for caracter in string]
    array_caracteres = np.array(lista_caracteres)
    return array_caracteres

def descriptografar(string):
    lista_caracteres = [chr(numero - CODE_HASH) for numero in string]
    return ''.join(lista_caracteres)

string = "Let's Code from ADA"

array_criptografado = criptografar(string)
print(array_criptografado)

string_descriptografada = descriptografar(array_criptografado)
print(string_descriptografada)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Modificar uma imagem para sua visualização em camadas individuais (R, G, B) -> (Red, Green, Blue) -> (Vermelho, Verde, Azul)

from matplotlib import pyplot as plt
from matplotlib import image as img

image = img.imread('./Aulas/5. Técnicas de Programação/Images/python.png')

plt.figure(figsize=(10,5))

# R -> Red -> Vermelho
plt.subplot(1, 3, 1)
plt.imshow(image[:,:,0], cmap='Reds')

# G -> Green -> Verde
plt.subplot(1, 3, 2)
plt.imshow(image[:,:,1], cmap='Greens')

# B -> Blue -> Azul
plt.subplot(1, 3, 3)
plt.imshow(image[:,:,2], cmap='Blues')

plt.show()