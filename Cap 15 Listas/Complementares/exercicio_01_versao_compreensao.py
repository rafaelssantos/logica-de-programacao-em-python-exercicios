n = int(input("Número de elementos da lista 1 e da lista 2: "))
lista1 = []
for e in range(n):
    num = int(input("Insira o próximo elemento da lista 1: "))
    lista1.append(num)


lista2 = []
for e in range(n):
    num = int(input("Insira o próximo elemento da lista 2: "))
    lista2.append(num)

# Criar a lista3 somando os elementos correspondentes
lista3 = [x + y for x, y in zip(lista1, lista2)]

print(lista3)