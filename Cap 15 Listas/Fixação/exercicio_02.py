n = int(input("Informe a quantidade de elementos: "))
lista = []

for e in range(n):
    num = int (input("Informe um número: "))
    lista.append(num)


print("Antes da troca")
print(lista)


# Para trocar elementos é necessário ter uma variável auxiliar
aux = lista[len(lista) - 1]     # Cópia do último elemento da lista
lista[len(lista) - 1] = lista[0] # Guarda o primeiro elemento na última posição
lista[0] = aux  # Recupera a cópia do último elemento da lista

print("Depois da troca")
print(lista)
