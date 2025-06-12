numeros = [22, 33, 44, 19, 25, 34, 15, 40]

maior = numeros[0]

for numero in numeros:
  # print(f'passando por {numero}, maior = {maior}')
  maior = max(maior, numero)

print(maior)