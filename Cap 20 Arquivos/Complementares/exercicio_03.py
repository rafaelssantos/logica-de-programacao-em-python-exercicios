def primo(num):
    """
        Função que avalia se um número é primo.
        Args:
            num (float): Número a ser avaliados
        Returns:
            bool: True, caso o número seja primeo e False, caso não seja primo.
    """
    divisores = 0
    for e in range(1, num + 1):
        if num % e == 0:
            divisores = divisores + 1
    if divisores > 2:
        return False
    else:
        return True


def gera_primos(n):
    """
        Função que gera uma quantidade n números primos.
        Args:
            n (int): Quantidade de números primos.
        Returns:
            list: Lista de números primos gerados.
    """
    cont = 0
    num = 2
    lista_primos = []

    while cont <= n:
        if primo(num):
            cont = cont + 1
            lista_primos.append(num)
        num = num + 1
    
    return lista_primos


# ------------------------------------------------------------
n = int(input("Quantos números primos você deseja gerar? "))

lista_primos = gera_primos(n)

with open("primos.csv", "w") as arquivo:
    for p in lista_primos:
        arquivo.write(str(p)+"\n")