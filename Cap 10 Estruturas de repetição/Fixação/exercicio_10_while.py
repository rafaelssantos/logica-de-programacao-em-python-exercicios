n = int(input("Qual a quantidade de números da sequência? "))

cont_3 = 0
cont_5 = 0
i = 0
while i < n:
    num = int(input("Informe um número: "))
    if num % 3:
        cont_3 = cont_3 + 1
    if num % 5:
        cont_5 = cont_5 + 1
    i = i + 1

print("Número de múltiplos de 3:", cont_3)
print("Número de múltiplos de 5:", cont_5)
