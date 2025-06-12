lista = []

lista.append(1)
lista.append(2)
lista.append(3)

lista2 = lista.copy()

lista2.append(4)

lista3 = [9, 10]

lista2.extend(lista3)
lista2.extend([5, 6, 7, 8])

lista2.sort(reverse = True) 

print(lista)
print(lista2)