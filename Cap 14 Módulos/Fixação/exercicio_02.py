import random

num = random.randint(0, 10)
tentativa = None

for e in range(1, 4):
    print("Tentativa", e)
    tentativa  = int(input("Informe o número: "))
    if tentativa == num:
        break

if tentativa == num:
    print("Você ganhou!")
else:
    print("Você perdeu!")
    print("O número gerado foi", num)