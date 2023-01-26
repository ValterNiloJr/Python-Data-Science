from sys import path_hooks
import string, random
from random import randint

texto = 'texto 123 ## TEXTO UM DOIS TRES @@'
cripto_lista = []
contador_chave = 0
chave = ''
cripto = ''
quebra = 'abcdefghijklmnopqrstuvwxyz#%'
sum = 0

##CRIPTOGRAFANDO
while contador_chave < 10:
  num = (randint(0,9))
  chave = chave + chr(random.randint(ord('a'), ord('z'))) + str(num)
  contador_chave += 1
chave += '#%'

print(f'A chave para descriptografar é: {chave}')

for letra in quebra:
  chave = chave.replace(letra, '')


for digit in str(chave):   
  sum += int(digit)        
  

for letra in texto:
    cripto_lista.append(str(ord(letra)*sum))
    cripto_lista.append(chr(random.randint(ord('a'), ord('z'))))

cripto = "".join(cripto_lista)
print(f'A mensagem criptografada é: \n {cripto}')