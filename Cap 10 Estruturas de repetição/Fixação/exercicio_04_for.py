n = int(input("Informe a quantidade de números: "))

menor = int(input("Informe o primeiro número: "))       # Inicialização do menor elemento

for e in range(n-1):
    num = int(input("Informe o próximo número: "))
    if num < menor:     # Encontrado um elemento menor que o atual
        menor = num     # Menor atual

print(menor)