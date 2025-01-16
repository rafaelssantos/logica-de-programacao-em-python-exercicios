n = int(input("Qual é quantidade de nomes? "))

lista = []

for e in range(n):
    nome = input("Informe um nome: ")
    lista.append(nome)

lista.sort()

print("Lista de nomes em ordem alfabética")
print(lista)