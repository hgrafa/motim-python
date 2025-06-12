n = int(input())

# ler n elementos inteiros na mesma linha

# dados = input().split() # ['1', '2', '3', '4', '-5']
# numeros = []

# for info in dados:
#   numeros.append(int(info))

numeros = list(map(int, input().split()))

menor = None
pos_menor = None

for i in range(len(numeros)):
  if menor == None or numeros[i] < menor:
    menor = numeros[i]
    pos_menor = i

print(f'Menor valor: {menor}')
print(f'Posicao: {pos_menor}')