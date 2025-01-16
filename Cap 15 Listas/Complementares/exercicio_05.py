n1 = int(input("Informe o número de elementos da lista 1: "))
lista1 = []

for e in range(n1):
    num = int(input("Insira o próximo elemento da lista 1: "))
    lista1.append(num)

n2 = int(input("Informe o número de elementos da lista 2: "))
lista2 = []

for e in range(n2):
    num = int(input("Insira o próximo elemento da lista 2: "))
    lista2.append(num)

comum = []
for e1 in lista1:
    if e1 in lista2:
        comum.append(e1)


print("Elementos em comum")
print(comum)