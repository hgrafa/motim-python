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

# Strings

> lista de caracteres

> strings sao tipos complexos, isto é, possuem métodos

```py
palavra = 'teste'

print(palavra[0]) # t
print(palavra[2]) # s
```
