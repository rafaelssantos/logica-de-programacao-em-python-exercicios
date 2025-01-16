lista = []      # Lista de strings

while True:     # Insere elementos até que seja digitada a palavra "fim"
    elemento = input("Informe um elemento: ") 
    if elemento == "fim":
        break

    lista.append(elemento)      # Adiciona string à lista

print("Lista resultante")
print(lista)