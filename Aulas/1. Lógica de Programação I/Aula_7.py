#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Dada uma lista de inteiros ('nums') de comprimento n, você deseja criar uma lista 'ans' de comprimento 2n onde:

#    ans[i] == nums[i] e
#    ans[i + n] == nums[i]
#    para 0 <= i < n (0-index).

#    Especificamente, ans é a concatenação de duas listas 'nums'.

#    Retorne a lista ans.

#    Exemplo 1:
#    Entrada: nums = [1,2,1]

#    Saída: [1,2,1,1,2,1]

#    Explicação: A lista ans é formada da seguinte forma:

#    ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
#    ans = [1,2,1,1,2,1]
#    Exemplo 2:
#    Entrada: nums = [1,3,2,1]

#    Saída: [1,3,2,1,1,3,2,1]

#    Explicação: A lista ans é formada da seguinte forma:

#    ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
#    ans = [1,3,2,1,1,3,2,1]

nums = [1, 2, 3]
ans = []
n = len(nums) * 2

for i in range(n):
    ans.append(nums[i%len(nums)])

print(ans)

# ans = nums * 2
# print(ans)

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Dada uma lista nums. Definimos uma soma acumulada de uma lista como runningSum[i] = sum(nums[0]…nums[i]).

#    Retorne a soma acumulada de nums.

#    Exemplo 1:
#    Entrada: nums = [1,2,3,4]

#    Saída: [1,3,6,10]

#    Explicação: A soma acumulada é obtida da seguinte forma: [1, 1+2, 1+2+3, 1+2+3+4].

#    Exemplo 2:
#    Entrada: nums = [1,1,1,1,1]
#    Saída: [1,2,3,4,5]
#    Explicação: A soma acumulada é obtida da seguinte forma: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

#n = input('Digite os valores separados por ( , )').split(',')
#for i in range(len(n)):
#    n[i] = int(n[i])

nums = [1, 1, 1, 1]
sum = []
sum_aux = 0
for num in nums:
    sum_aux = sum_aux + num
    sum.append(sum_aux)
    
print(sum)
