def area_quadrado(lado):
    """
    Função que calcula a área do quadrado.

    Parâmetros:
    lado (float): O valor da base do quadrado.

    Retorna:
    float: A área calculada do quadrado.
    """
    area = lado * lado
    return area

def area_triangulo(base, altura):
    """
    Função que calcula a área do triângulo.

    Parâmetros:
    base (float): O valor da base do triângulo.
    altura (float): O valor da altura do triângulo.

    Retorna:
    float: A área calculada do triângulo.
    """
    area = (base * altura) / 2
    return area

def area_retangulo(base, altura):
    """
    Função que calcula a área do retângulo.

    Parâmetros:
    base (float): O valor da base do retângulo.
    altura (float): O valor da altura do retângulo.

    Retorna:
    float: A área calculada do retângulo.
    """
    area = base * altura
    return area
# -------------------------------------------------------
print("Calculadora de área de polígonos")
print("1 - Quadrado")
print("2 - Triângulo")
print("3 - Retângulo")

opcao = int(input("Informe a opção escolhida: "))

if opcao == 1:
    lado = float(input("Informe o lado: "))
    area = area_quadrado(lado)
    print(area)
elif opcao == 2:
    base = float(input("Informe o valor da base: "))
    altura = float(input("Informe o valor da altura: "))
    area = area_triangulo(base, altura)
    print(area)
elif opcao == 3:
    base = float(input("Informe o valor da base: "))
    altura = float(input("Informe o valor da altura: "))
    area = area_retangulo(base, altura)
    print(area)
