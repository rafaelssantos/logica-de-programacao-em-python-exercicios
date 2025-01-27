conjunto = set()
n = int(input("Quantos números tem o conjunto? "))

for e in range(n):
    num = int(input("Informe o próximo número do conjunto: "))
    conjunto.add(num)

for e in conjunto:
    print(e)