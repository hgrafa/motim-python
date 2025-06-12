idades = {
  'joao': 24,
  'maria': 35,
  'pedro': 40,
  'lucas': 16
}

idades.get('joao')

print(idades.keys())
print(idades.values())

media_idades = sum(idades.values()) / len(idades)
print(f'media da idades: {media_idades}')

for nome, idade in idades.items():
  print(f'chave: {nome}, valor: {idade}')