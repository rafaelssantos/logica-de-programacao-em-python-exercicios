n = int(input("Qual é a quantidad de números que será informada? "))

soma = 0
for e in range(n):
    num = float(input("Informe um número: "))
    soma = soma + num

media = soma / n
print("A média é", media)