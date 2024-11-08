caminho = input("Informe o caminho do arquivo: ")

with open(caminho, "r") as arquivo:
   print(len(arquivo.readlines))