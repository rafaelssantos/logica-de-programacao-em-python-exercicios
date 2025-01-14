def area_retangulo(base, altura):
    """
    Função que calcula a área do retângulo.

    Parâmetros:
    base (float): O valor da base do retângulo.
    altura (float): O valor da altura do retângulo.

    Retorna:
    float: A área calculada do retângulo.
    """
    area  = base * altura
    return area

# ---------------------------------------------------------------------
base = float(input("Informe a base: "))
altura = float(input("Informe a altura: "))

area = area_retangulo(base, altura)     # Chamada da função
print("A área é", area)