import random
sorteado = random.randint(0, 100)

t = 1
while t <= 10:
    palpite = int(input(f"Qual é o #{t} seu palpite? "))
    if palpite == sorteado:
        break
    t = t + 1

if palpite == sorteado:
    print("Você ganhou!")
else:
    print("Você perdeu!")