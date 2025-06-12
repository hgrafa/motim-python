linha = 'Hugo,24,1.8'
acumulador = ''
infos = []

# para cada caracter da linha
for char in linha:
  # se for , => hora de separar a info e salvar
  if char == ',':
    infos.append(acumulador)
    acumulador = ''
  else: # senao => continuo acumulando
    acumulador += char

# salvo o que sobrou de info no fim da linha
infos.append(acumulador)

nome, idade, altura = infos