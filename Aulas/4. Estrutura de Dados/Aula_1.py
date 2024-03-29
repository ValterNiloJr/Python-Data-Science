#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Crie um algoritmo que imprime uma lista de números inteiros de 1 a 50.

def imprime_int():
    nums = [num for num in range(1, 51)]
    print(nums)
    for num in nums:
        print(num)


imprime_int()

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Crie um algoritmo que imprime uma lista de números inteiros palindromos de 1 a 121.


def imprime_palindromos():
    nums = [num for num in range(1, 122)]
    palindromos = []
    for num in nums:
        if str(num) == str(num)[::-1]:
            palindromos.append(num)

    print(palindromos)


imprime_palindromos()

#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Crie um algoritmo que dado um dicionario de 5 pacientes contendo peso e altura, calcula e retorna (adiciona) o IMC do paciente
#    no dicionario.


def imc(pacientes):
    for paciente in pacientes:
        imc_num = (pacientes[paciente]['Peso'] /
                   (pacientes[paciente]['Altura'] ** 2))
        if imc_num < 18.5:
            imc_paciente = 'Magreza'
        elif 18.5 <= imc_num < 25:
            imc_paciente = 'Normal'
        elif 25 <= imc_num < 30:
            imc_paciente = 'Sobrepeso'
        elif 30 <= imc_num < 40:
            imc_paciente = 'Obesidade'
        elif imc_num < 40:
            imc_paciente = 'Obesidade Grave'
        else:
            imc_paciente = 'Inválido'
        pacientes[paciente].update({'IMC': f'{imc_num:.2f} - {imc_paciente}'})


pacientes = {
    'Valter': {
        'Peso': 70,
        'Altura': 1.68,
    },
    'Byanca': {
        'Peso': 65,
        'Altura': 1.64
    },
    'João': {
        'Peso': 82,
        'Altura': 1.74
    },
    'Ana': {
        'Peso': 55,
        'Altura': 1.59
    },
    'José': {
        'Peso': 123,
        'Altura': 1.81
    },
}

imc(pacientes)
print(pacientes)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Crie um algoritmo que calcule o mínimo múltiplo comum de 2 números inteiros.


def mmc(num1, num2):
    max_num = max(num1, num2)

    div_num1 = set()
    div_num2 = set()

    for divisor in range(1, max_num+1):
        if (num1 % divisor == 0):
            div_num1.add(divisor)
        if (num2 % divisor == 0):
            div_num2.add(divisor)

    div_comum = div_num1.intersection(div_num2)
    div_comum.pop()
    return min(div_comum)


print(mmc(18, 36))
