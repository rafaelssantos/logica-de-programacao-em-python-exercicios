def calcular_imc(peso, altura):
    imc  = peso / (altura ** 2)
    return imc

# ------------------------------------------------------
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = calcular_imc(peso, altura)
print(imc)