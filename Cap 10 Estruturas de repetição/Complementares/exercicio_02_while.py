n = int(input("Qual é a quantidad de números que será informada? "))

soma = 0
i = 0
while i < n:
    num = float(input("Informe um número: "))
    soma = soma + num
    i = i + 1

media = soma / n
print("A média é", media)