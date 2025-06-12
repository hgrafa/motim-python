# for number in range(1, 11):
#   print(number)

# for i in range(5): # 0 1 2 3 4
#   print('oi')

frutas = ['morango', 'abacaxi', 'banana', 'uva', 'kiwi', 'mamao']
tamanho = len(frutas)

for i in range(tamanho): # 0, 1, 2, 3
  print(frutas[i])

for i in range(tamanho): # 0, 1, 2, 3
  print(f'frutas[{i}] = {frutas[i]}')