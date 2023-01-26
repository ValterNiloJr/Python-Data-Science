#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Dado um endereço IP válido (IPv4), retorne uma versão 'desativada' desse endereço IP.

#    Um endereço IP desativado substitui cada ponto "." com "[.]".

#    Exemplo 1:

#    Entrada: endereço = "1.1.1.1"
#    Saída: "1[.]1[.]1[.]1"
#    Exemplo 2:

#    Entrada: endereço = "255.100.50.0"
#    Saída: "255[.]100[.]50[.]0"

ip = "255.100.50.0"

lista = ip.split('.')
saida = '[.]'.join(lista)

print(saida)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Um pangrama é uma frase em que cada letra do alfabeto aparece pelo menos uma vez.

#    Dada uma frase de string contendo apenas letras minúsculas, retorne true se a frase for um pangrama ou false caso contrário.

#    Exemplo 1:

#    Entrada: frase = "thequickbrownfoxjumpsoverthelazydog"
#    Saída: verdadeiro
#    Explicação: a frase contém pelo menos uma de cada letra do alfabeto.

#    Exemplo 2:

#    Entrada: frase = "letscode"
#    Saída: falso

frase = "thequickbrownfoxjumpsoverthelazydog"

primeiro = ord('a')
ultimo = ord('z') + 1

contador = 0

for alfabeto in range(primeiro, ultimo):
    if (chr(alfabeto) in frase):
        contador += 1

if (contador == (ultimo-primeiro)):
    print(True)
else:
    print(False)
