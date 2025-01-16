n = int(input("Quantos elementos você deseja a somar? "))

i = 0
soma = 0        # 0 é o elemento neutro da soma
while i < n:
    num = int(input("Informe um número: "))
    soma = soma + num   # Acumulação da soma
    i = i + 1

print(soma)