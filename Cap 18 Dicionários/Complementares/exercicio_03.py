n = int(input("Quantos nomes serão informados? "))
lista_de_nomes = []

for e in range(n):
    nome = input("Informe um nome: ")
    lista_de_nomes.append(nome)

dicionario_de_nomes = {}
for nome in lista_de_nomes:
    dicionario_de_nomes[nome] = len(nome)

print(dicionario_de_nomes)