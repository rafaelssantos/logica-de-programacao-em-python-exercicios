n = int(input("Informe a quantidade de elementos: "))
lista = []

for e in range(n):
    num = int (input("Informe um número: "))
    lista.append(num)


chave = int(input("Informe o elemento a buscar: "))

if chave in lista:
    print("Elemento encontrado.")
else:
    print("Elemento não encontrado.")