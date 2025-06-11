# Introdução a Python

## Dicas de terminal

- `ctrl + '`: abrir terminal
- `ls`: lista arquivos e pastas dentro de um diretorio
- `python nomeDoArquivo.py`: executa programa python
- `cls`, `clear` ou `ctrl + L`: limpar terminal
- seta pra cima ou seta pra baixo: navega entre os comandos ja utilizados
- `cd`: navega entre as pastas via terminal

## Comentários

```py
  # isto é um comentário
```

## Função Print

O print exibe um conteúdo na saída padrão do sistema (terminal).

```py
print('Hello, World!')
```

### Concatenação

junta textos em uma saída

```py
idade = 25
primeiro_nome = 'Hugo'
segundo_nome = 'Rafael'

print('Nome completo ' + primeiro_nome + ' ' + segundo_nome)
print('minha idade é', idade) # minha idade é 25
print('hello', 'world') # hello world
```

### Interpolação

Alterna na saída entre textos fixos e variáveis.

```py
nome = 'Pedro'
sobrenome = 'Silva'
altura = 1.82

print(f'Meu nome é {nome} {sobrenome}')
print(f'minha altura é {altura}m')
```

## Tipos primitivos em python

como checar tipos: `type(variavel)`

- `int`: armazena inteiros
- `float`: armazena numeros com virgula
- `str`: (String) armazena textos
- `bool`: (`True` ou `False`) verdadeiro ou falso

```py
nome = 'Teste'

print(type(nome)) # <class 'str'>
```

## input

funcao input le o que usuario digita e salva como string

```py
nome = input()

print(f'meu nome é {nome}')
```

## Converter Input para outros tipos

```py
a = int(input())
b = int(input())
soma = a + b

print(f'X = {soma}')
```
