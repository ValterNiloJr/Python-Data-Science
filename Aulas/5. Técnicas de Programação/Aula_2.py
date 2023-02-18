#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Considere um sistema simples de notas de uma escola. Neste sistema, para cada aluno, há um registro de nome e uma nota. 
#    Crie uma lista que contenha os nomes de pelo menos 5 alunos e um array numpy com suas respectivas notas. O sistema de exibir 
#    o nome e nota dos alunos com nota maior ou igual a 7.
'''
import numpy as np

alunos = ['Valter', 'Byanca', 'Lucas', 'Eduardo', 'Vivian']
notas = np.array([7.0, 8.2, 6.0, 6.7, 7.4])

# imprimindo os alunos com nota maior ou igual a 7
print('Notas maiores ou iguais a 7:')
for index in np.nonzero(np.select([notas>=7], [notas]))[0]:
    print(f'Aluno: {alunos[index]} | Nota: {notas[index]}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Faça um programa que crie dois arrays numpy com valores numéricos. O programa deve verificar e criar um terceiro array com os 
#    valores em comum entre os dois anteriores.

import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
print(f'A1: {a1}')

a2 = np.array([6, 7, 5, 3, 1])
print(f'A2: {a2}')

a3 = np.intersect1d(a1, a2)
print(f'Valores em comum entre A1 e A2: {a3}')

#-----------------------------------------------------------------------------------------------------------------------------------#
# 5. Faça um programa que calcule a matriz transposta de uma dada matriz numpy

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Matriz:\n', matriz)
print('\nTransposta:\n', matriz.T)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 6. Faça um programa que plot uma elipse utilizando numpy e matplotlib.

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)

a = 4
b = 3

x = a*np.cos(t)
y = b*np.sin(t)
x = a*np.cos(t)
y = b*np.sin(t)

plt.axis([-5, 5, -5, 5])
plt.plot(x, y)
plt.show()
'''
#-----------------------------------------------------------------------------------------------------------------------------------#
# Desafio: Utilize o trecho de código dado e um arquivo de áudio no formato wav para ler, visualizar e criar edições desse arquivo 
#          de áudio. Voce pode remover partes, criar repetições, trocar partes de lugar ou alterar valores.


from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("./Aulas/5. Técnicas de Programação/Músicas/Guns-N-Roses-Estranged.wav")
input_data

audio = input_data[1]
print(audio.shape)
print(type(audio))

# plot the first 1024 samples
plt.plot(audio[0:44100*10])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()

# Ainda não tive tempo para implemetar :/
