def ehprimo(numero):
  for teste in range(2, numero):
    if numero % teste == 0: 
      return False
  
  return True


n = int(input())

for _ in range(n):
  numero = int(input())

  if ehprimo(numero):
    print(f'{numero} eh primo')
  else:
    print(f'{numero} nao eh primo')