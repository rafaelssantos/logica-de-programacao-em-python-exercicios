n = int(input("Número de elementos da lista: "))

lista = []

for e in range(n):
    num = int(input("Insira o próximo elemento: "))
    lista.append(num)


lista_par = []
lista_impar = []

for e in lista:
    if e % 2 == 0:
        lista_par.append(e)
    else:
        lista_impar.append(e)

print("Lista dos pares")
print(lista_par)

print("Lista dos ímpares")
print(lista_impar)