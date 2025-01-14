nome = input("Insira seu nome completo: ")
caminho = input("Insira o nome do arquivo: ")

with open(caminho, "w") as arquivo:
    arquivo.write(nome)