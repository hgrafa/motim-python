# este programa vai receber um valor n
# depois vai receber na linha seguinte n numeros
# para cada numero vc deve dizer 'é par' ou 'é impar'
# você deve usar uma função para validar se o número é par ou não

# exemplo de entrada:
# 5
# 1 2 3 4 5

# saida esperada:
# 1 é impar
# 2 é par
# 3 é impar
# 4 é par
# 5 é impar
 
def ehpar(numero):
  return numero % 2 == 0

n = int(input())
numeros = list(map(int, input().split()))

for numero in numeros:
  if ehpar(numero):
    print(f'{numero} é par')
  else:
    print(f'{numero} é impar')
