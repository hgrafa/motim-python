# faca um programa que receba codigo e quantidade do item
dados = input().split() # ['2', '3']

codigo = int(dados[0])
quantidade = int(dados[1])

# diga quando que a pessoa gastou em: item1 ou item2 ou item3 ou item4

if codigo == 1: 
  total = 4.0 * quantidade
elif codigo == 2: 
  total = 4.5 * quantidade
elif codigo == 3:
  total = 5.0 * quantidade
elif codigo == 4:
  total = 2.0 * quantidade
elif codigo == 5:
  total = 1.5 * quantidade

print(f'Total: R$ {total:.2f}')