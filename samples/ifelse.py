nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))

if idade >= 18:
  print(f'{nome} pode dirigir!')
else:
  print(f'{nome} ainda não pode dirigir')