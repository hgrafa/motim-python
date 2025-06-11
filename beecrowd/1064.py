# ler 6 valores

soma_positivos = 0
quant_positivos = 0
count = 1

while count <= 6: 
  numero = float(input())
  count += 1

  if numero > 0: 
    soma_positivos += numero
    quant_positivos += 1

# quantidade de positivos
# soma dos positivos

media = soma_positivos / quant_positivos

print(f'{quant_positivos} valores positivos')
print(f'{media:.1f}')