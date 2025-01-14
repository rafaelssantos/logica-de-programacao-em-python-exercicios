def metros_para_quilometros(metros):
    """
    Função que converte metros para quilômetros.

    Parâmetros:
    metros (float): O valor em metros.

    Retorna:
    float: O valor em quilômetros.
    """
    quilometros = metros / 1000
    return quilometros

# --------------------------------------------
metros = float(input("Informe um valor em metros: "))
quilometros = metros_para_quilometros(metros)

print("O valor em quilômetros é", quilometros)