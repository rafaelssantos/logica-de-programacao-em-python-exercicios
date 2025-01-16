n = int(input("Qual a quantidade de números da sequência? "))

# Dois contadores. Um para cada contagem de divisores.
cont_3 = 0      # Elemento neutro da contagem
cont_5 = 0      # Elemento neutro da contagem

i = 0
while i < n:
    num = int(input("Informe um número: "))
    if num % 3:
        cont_3 = cont_3 + 1     # Contando um múltiplo de 3.
    if num % 5:
        cont_5 = cont_5 + 1     # Contando um múltiplo de 5.
    i = i + 1

print("Número de múltiplos de 3:", cont_3)
print("Número de múltiplos de 5:", cont_5)
