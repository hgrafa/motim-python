# quero o indice um elemento na lista
# se nao existir mostro -1

def busca_sequencial(alvo, lista):
  for i in range(len(lista)):
    if lista[i] == alvo:
      return i
    
  return -1

alvo = int(input('digite um numero para buscar: '))
numeros = [1, 2, 3, 4, 5]
resultado_busca = busca_sequencial(alvo, numeros)

if resultado_busca != -1:
  print(f'encontrado na posicao: {resultado_busca}')
else: 
  print('nao encontrado')

numeros.index()