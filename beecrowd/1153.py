# tenho que caminhar de 1 ate n
# multiplicar todos esses numeros

def fatorial(n):
  produto = 1

  for i in range(1, n+1):
    produto *= i

  return produto

n = int(input())
print(fatorial(n))

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