# Estrutura de Seleção

## Estrutura `if...else` ('se...senao')

```
if [CONDICAO] :
  [EXECUTE_SE_CONDICAO_FOR_VERDADEIRA]
else:
  [EXECUTE_SE_CONDICAO_FOR_FALSA]
```

```py
temAgua = True
temCafe = False

if temAgua and temCafe:
  print('consigo fazer cafe')

```

## Estrutura `if...elif...else` ('se...senao se...senao')

```
if [CONDICAO1] :
  [EXECUTA_SE_CONDICAO1_FOR_TRUE]
elif [CONDICAO2] :
  [EXECUTA_SE_CONDICAO2_FOR_TRUE]
...
else:
  [EXECUTE_SE_TODAS_AS_CONDICOES_FOREM_FALSE]
```

```py
if codigo == 1:
  total = 4.0 * quantidade
elif codigo == 2:
  total = 4.5 * quantidade
elif codigo == 3:
  total = 5.0 * quantidade
```

# Arrays / Listas / Vetor

Bloco contiguo/continuo de memoria.

> Arrays sao indexados em 0 (começam a partir da posição zero)

```py
# como declarar um array em python
notas = [7.0, 5.0, 7.5]

# como mostrar os elementos do array
print(notas)

# mudar o primeiro elemento
notas[0] = 9.0

# como mostrar o primeiro elemento do array
print(notas[0])
```

## desestruturação

```py
nomes = ['Alice', 'Pedro']

primeiro, segundo = nomes
```

# Strings

> lista de caracteres

> strings sao tipos complexos, isto é, possuem métodos

```py
palavra = 'teste'

print(palavra[0]) # t
print(palavra[2]) # s
```

# Estrutura de repetição / loop

- inicializacao
- verificacao
- atualizacao

## Estrutura `while` (Enquanto)

> `if` que dura mais de uma vez

```py
count = 0 # inicializacao

while count < 5: # verificacao
  print('oi')
  count += 1 # atualizacao

print('fim do programa')
```

- objetivo: contar de 1 a 10

```py
count = 1 # inicializacao

while count <= 10: # verificacao
  print(count)
  count += 1 # atualizacao

print('fim do programa')
```

## Estrutura for (`para`)

- range(stop) -> vou de zero (inclusive) ate o stop(exclusive) de um em um
- ex: `range(5)` : `0, 1, 2, 3, 4`

- range(start, stop) -> vou do start(inclusive) ate o stop(exclusive) de um em um
- `range(2, 7)`: `2, 3, 4, 5, 6`

- range(start, stop, step) -> vou do start(inclusive) ate o stop(exclusive) de step em step
- `range(2, 11, 2)`: `2, 4, 6, 8, 10`

```py
for count in range(5, 0, -1):
  print(count) # 5, 4, 3, 2, 1
```

## Palavras-chave

- `break`: interrompe o loop por completo
- `continue`: pula o restante do loop

# Expandindo o `print`

- sep: separa os elementos passados
- end: diz qual é o conteúdo a ser mostrado no final da linha

```py
print('texto', 'de', 'varias', 'palavras', sep=' ', end='\n')
```

### Operador Ternario

```py
  paridade = 'EVEN' if numero % 2 == 0 else 'ODD'
  sinal = 'POSITIVO' if numero > 0 else 'NEGATIVE'
```
