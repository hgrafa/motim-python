## Operadores

### Operadores binários

| Operador |         o que faz          |    exemplo     |
| :------: | :------------------------: | :------------: |
|    +     |            soma            |  `2 + 3 => 5`  |
|    -     |         subtracao          | ` 2 - 3 => -1` |
|    \*    |       multiplicacao        |  `2 * 3 => 6`  |
|    /     |          divisao           | `3 / 2 => 1.5` |
|    %     |       modulo (resto)       | `10 % 4 => 2`  |
|    //    | divisao inteira(quociente) | `3 // 2 => 1`  |
|   \*\*   |     potencia (elevado)     | `2 ** 3 => 8`  |

### Operador Ternario

(...)

### Operador reflexivo

```py
count = int(input())

# count recebe o valor atual de count + 1
count = count + 1
count = count - 5
variavel = variavel / 2
outra_variavel = outra_variavel * 3

count += 1 # incrementa 1 no count -> count = count + 1
count -= 5 # decrementa 1 no count

# menos usual
numero *= 2
```

### Expressoes Booleanas

```py
estaChovendo = False
estaDeTarde = True
```

```py
resultado1 = 2 > 3 # False
resultado2 = 5 >= 2 # True
resultado3 = 2 == 2 # True
```

| Operador |   o que faz    |      exemplo       |
| :------: | :------------: | :----------------: |
|    >     |     maior      |   `5 > 3` (True)   |
|    >=    | maior ou igual |  `5 >= 3` (True)   |
|    <     |     menor      |  `5 < 3` (False)   |
|    <=    | menor ou igual |  `5 <= 3` (False)  |
|    <=    | menor ou igual |  `5 <= 3` (False)  |
|    ==    |     igual      |  `5 == 5` (True)   |
|    !=    |   diferente    |  `5 != 5` (False)  |
|   not    |    negação     | `not True` (False) |

### '=' vs. '=='

- `=` atribui um valor para uma variavel
- `==` compara se duas informacoes sao iguais

### Conectivos

- `and`: significa 'e' em inglês e precisa que ambos os lados sejam verdade

```py
temAgua = True
temCafe = False

consigoFazerCafe = temCafe and temAgua
```

|  `a`  |  `b`  | `a and b` |
| :---: | :---: | :-------: |
| True  | True  |   True    |
| True  | False |   False   |
| False | True  |   False   |
| False | False |   False   |

- `or`: significa 'ou' em inglês e precisa que pelo menos um seja verdade

```py
temAgua = False
temSuco = True

consigoMatarSede = temAgua or temSuco
```

|  `a`  |  `b`  | `a or b` |
| :---: | :---: | :------: |
| True  | True  |   True   |
| True  | False |   True   |
| False | True  |   True   |
| False | False |  False   |

# Seleção / Estruturas condicionais

> Se tirou nota maior ou igual que 6 digo que esta aprovado, senao recuperacao.

## Estrutura `if` ('se')

```
if [CONDICAO] :
  [EXECUTE_SE_CONDICAO_FOR_VERDADEIRA]
```

```py
temAgua = True
temCafe = False

if temAgua and temCafe:
  print('consigo fazer cafe')

```

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
