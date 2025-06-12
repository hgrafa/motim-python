# Unindo for, listas e strings

## Estrutura `for`

```py
for number in range(1, 11):
  print(number)
```

## Listas em python

> Se minha lista tem `n` elementos, os indices vao de zero ate `n-1`

0 -> 5 = 6 elementos

```py
frutas = ['morango', 'abacaxi', 'banana', 'uva']

# total de elementos: 4
# indices: 0, 1, 2, 3

print(frutas[0]) # morango
print(frutas[1]) # abacaxi
print(frutas[2]) # banana
print(frutas[3]) # uva

# saber a quantidade de elementos de uma lista
print(len(frutas))
```

## Percorrendo uma lista com o `for`

> o `i` é importante para indicarmos os indices/posicoes que queremos percorrer na lista

```py
frutas = ['morango', 'abacaxi', 'banana', 'uva']
tamanho = len(frutas)

for i in range(tamanho): # i => 0, 1, 2, 3
  print(frutas[i])
```

- for each : para cada

```py
for fruta in frutas:
  print(fruta)
```

## for com `strings`

```py
palavra = 'paralelepipedo'

for letra in palavra:
  print(letra)
```

## Funcoes uteis

- `len(lista)` : diz o tamanho da lista
- `sum(lista)`: diz a soma dos elementos (numericos) da lista
- `max(a, b)`: diz qual é o maior entre dois valores
- `min(a, b)`: diz qual é o menor entre dois valores

# Função

- passo a passo
- sequencia de passos bem definidos
- subprogramação
- pode ter entrada
- pode ter retorno
  - com retorno = geralmente trabalhar a entrada
  - sem retorno = geralmente orquestrar um processo

> Por que fazemos funcoes?

- Reuso
- Legibilidade

```py
def soma(a, b):
  return a + b

def darBoasVindas(nome):
  print(f'ola, seja bem-vindo(a) {nome}!')

resultado = soma(2, 3)
darBoasVindas('Joao')
darBoasVindas('Bia')
```

# Dicionarios

> Estruturas de chave e valor

```py
idades = {
  'joao': 24,
  'maria': 35,
  'pedro': 40,
  'lucas': 16
}

usuario = {
  'email': 'email@test.com',
  'password': '12345',
  'age': 40
}

print(idades['joao'])
```

## percorrendo elementos do dicionario

```py
for nome, idade in idades.items():
  print(f'chave: {nome}, valor: {idade}')
```

# Arquivo

- `open`: recebe o arquivo e recebe o modo que vamos operar nesse arquivo

escreve em um arquivo

```py
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Esta é uma segunda linha.\n")
```

lendo um arquivo

```py
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo completo do arquivo:")
    print(conteudo)
```
