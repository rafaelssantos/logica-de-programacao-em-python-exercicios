n = int(input("Informe o número de elementos da lista: "))
lista = []

for e in range(n):
    num = int(input("Insira o próximo elemento: "))
    lista.append(num)

menor = lista[0]
maior = lista[0]

for e in lista:
    if e < menor:
        menor = e
    if e > maior:
        maior = e

print(f"O menor elemento é {menor}.")
print(f"O maior elemento é {maior}.")