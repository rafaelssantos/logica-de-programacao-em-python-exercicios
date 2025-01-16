n1 = int(input("Quantos elementos tem a primeira lista? "))

lista1 = []

for e in range(n1):
    num = int(input("Informe o próximo elemento: "))
    lista1.append(num)


n2 = int(input("Quantos elementos tem a segunda lista? "))
lista2 = []

for e in range(n2):
    num = int(input("Informe o próximo elemento: "))
    lista2.append(num)

lista3 = lista1 + lista2

print(lista3)