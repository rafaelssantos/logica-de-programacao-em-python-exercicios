caminho = input("Informe o caminho do arquivo: ")

with open(caminho, "r") as arquivo:
    texto = arquivo.read()
    print(texto)