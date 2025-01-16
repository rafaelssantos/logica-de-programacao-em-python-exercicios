def calcular_imc(peso, altura):
    """
    Função que calcula o Índice de Massa Corpórea (IMC).

    Params:
    - peso (float): Peso em quilogramas.
    - altura (float): Altura em metros.

    Returns:
    - float: IMC calculado.
    """
    imc  = peso / (altura ** 2)
    return imc

# ------------------------------------------------------
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = calcular_imc(peso, altura)
print(imc)