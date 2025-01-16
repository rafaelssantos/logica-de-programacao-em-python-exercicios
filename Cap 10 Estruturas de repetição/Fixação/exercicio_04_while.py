n = int(input("Informe a quantidade de números: "))

menor = int(input("Informe o primeiro número: "))       # Inicialização do menor elemento

i = 0
while i < n - 1:
    num = int(input("Informe o próximo número: "))
    if num < menor:         # Encontrado um elemento menor que o atual
        menor = num         # Menor atua
    i = i + 1

print(menor)