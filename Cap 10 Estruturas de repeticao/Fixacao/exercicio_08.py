soma = 0

while True:
    num = input("Insira um número ou 'Fim': ")
    if num == "Fim":
        break
    else:
        soma = soma + int(num)

print("Soma: ", soma)