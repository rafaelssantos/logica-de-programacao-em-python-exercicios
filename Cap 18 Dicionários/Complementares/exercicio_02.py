def somar_dicionarios(dicionario1, dicionario2):
    """
        Função que cria um novo dicionário com a união dos dois dicionários.
    """

    dicionario_resultante = dicionario1.copy()  # Faz uma cópia do primeiro dicionário
    
    # Para cada chave no segundo dicionário
    for chave2, valor2 in dicionario2.items():
        if chave2 in dicionario_resultante:
            # Se a chave já estiver no primeiro dicionário, soma os valores
            dicionario_resultante[chave2] = dicionario_resultante[chave2] + valor2
        else:
            # Se a chave não existir no primeiro dicionário, adiciona no novo dicionário
            dicionario_resultante[chave2] = valor2

    return dicionario_resultante

# ----------------------------------------------------------------------

dicionario1 = {'a': 10, 'b': 20, 'c': 30}
dicionario2 = {'b': 5, 'c': 10, 'd': 15}

resultado = somar_dicionarios(dicionario1, dicionario2)
print(resultado)
