# menor elemento de uma lista

lista = [22, 33, 44, 19, 25, 34, 15, 40]

menor = lista[0]

for i in range(len(lista)):
  # print(f'passando por {lista[i]}, menor = {menor}')
  if(lista[i] < menor):
    menor = lista[i]
    # print(f'trocou, novo menor = {menor}')

print(menor)