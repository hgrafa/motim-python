maior = None
pos_maior = None
FIX_INDEX_FROM_ONE = 1

for pos in range(100):
  numero = int(input())

  if maior == None or numero > maior:
    maior = numero
    pos_maior = pos

print(maior)
print(pos_maior + FIX_INDEX_FROM_ONE)
