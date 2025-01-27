n1 = int(input("Quantos elementos tem a primeira lista? "))
lista1 = []
for e in range(n1):
    num = int(input("Insira o próximo elemento da primeira lista: "))
    lista1.append(num)


n2 = int(input("Quantos elementos tem a segunda lista? "))
lista2 = []
for e in range(n2):
    num = int(input("Insira o próximo elemento da segunda lista: "))
    lista2.append(num)

diferenca = set(lista1) - set(lista2)

print(diferenca)