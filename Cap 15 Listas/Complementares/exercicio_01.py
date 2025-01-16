n = int(input("Número de elementos da lista 1 e da lista 2: "))
lista1 = []
for e in range(n):
    num = int(input("Insira o próximo elemento da lista 1: "))
    lista1.append(num)


lista2 = []
for e in range(n):
    num = int(input("Insira o próximo elemento da lista 2: "))
    lista2.append(num)

lista3 = []

for e in range(n):
    lista3.append(lista1[e] + lista2[e])


print(lista3)