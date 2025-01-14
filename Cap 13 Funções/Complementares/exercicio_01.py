def menor_de_idade(idade):
    """
    Função que determina se é menor ou maior de idade.

    Parâmetros:
    idade (int): Idade informada.

    Retorna:
    bool: True no caso de menor de idade e False no caso de maior de idade.
    """
    if idade < 18:
        return True
    else:
        return False
    

# --------------------------------------------
idade = int(input("Informe sua idade: "))
if menor_de_idade(idade):
    print("Menor de idade!")
else:
    print("Maior de idade!")