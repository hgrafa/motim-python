with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Esta é uma segunda linha.\n")

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo completo do arquivo:")
    print(conteudo)    