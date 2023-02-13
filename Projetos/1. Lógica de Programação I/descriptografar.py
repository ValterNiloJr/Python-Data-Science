from sys import path_hooks
import string, random
from random import randint

texto = 'meu texto é 1'
chave_informada = 'b5h5e9q2t3t5b7a4o2w3#%'
cripto_informada = '5220i4545q5400u5220b4995t1440v2205c2250d2295b1440p1575u1575s1440z3780e3105h3960y3780n3555v1440x3825w3465g1440j3060v3555z3285d3735w1440j3780t3690u3105o3735u1440c2880q2880r'
quebra = 'abcdefghijklmnopqrstuvwxyz#%'
decrip_lista = []
lista_texto = []
sum = 0
descripto = ''

##DESCRIPTOGRAFAR
for letra in quebra:
    cripto_informada = cripto_informada.replace(letra, '/')

decrip_lista = cripto_informada.split('/')
decrip_lista.pop(-1)


for letra in quebra:
  chave_informada = chave_informada.replace(letra, '')



for digit in str(chave_informada):   
  sum += int(digit)        

for numero in decrip_lista:
    lista_texto.append(chr(int(int(numero)/int(sum))))


descripto = "".join(lista_texto)
print(f'O texto descriptografado é: "{descripto}"')
