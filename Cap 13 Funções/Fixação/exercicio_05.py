def fatorial(num):
    """
    Função que calcula o fatorial de um número.

    Parâmetros:
    num (int): Número.
    
    Retorna:
    int: Fatorial calculado.
    """
    produto = 1
    for e in range(num, 0, -1):
        produto = produto * e
    return produto

# -----------------------
num = int(input("Informe o número: "))
fat = fatorial(num)
print(fat)