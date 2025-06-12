# Faça um programa que receba uma lista com mais que 10 numeros
# descubra o produto de todos os numeros da lista

numeros = [1, 2, 3, 4, 5]

prod = 1 # acumulador

for i in range(len(numeros)):
  prod *= numeros[i]

print(f'produto = {prod}')
