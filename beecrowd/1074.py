# ler um valor inteiro n
testes = int(input())

# ler um numero e avaliar POSITIVE vs NEGATIVE + ODD vs EVEN + NULL
for _ in range(testes): 
  numero = int(input())

  if numero == 0:
    print('NULL')
    continue

  paridade = 'EVEN' if numero % 2 == 0 else 'ODD'
  sinal = 'POSITIVO' if numero > 0 else 'NEGATIVE'
  
  print(f'{paridade} {sinal}')