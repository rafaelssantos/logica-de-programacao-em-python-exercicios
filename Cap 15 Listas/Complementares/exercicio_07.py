n = int(input("Número de elementos da lista: "))
lista = []

for e in range(n):
    num = int(input("Insira o próximo elemento: "))
    lista.append(num)


conjunto = set(lista)   # Transformando a lista em cojunto. Estrutura de dados sem repetição.
lista = list(conjunto)  # Transformando o conjunto em lista.

print("Lista de elementos sem repetição")
print(lista)
