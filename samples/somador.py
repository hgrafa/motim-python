numeros = [1, 2, 3, 44, 55, 66, 7, 8, 99, 101, 105, 17, 12]

# ---------------------------
# maneira 1
# sum = 0 # acumulador

# for i in range(len(numeros)):
#   sum += numeros[i]

# ---------------------------
# maneira 2

# sum = 0 # acumulador

# for numero in numeros:
#   sum += numero
# ---------------------------

soma = sum(numeros)

print(f'soma = {soma}')
