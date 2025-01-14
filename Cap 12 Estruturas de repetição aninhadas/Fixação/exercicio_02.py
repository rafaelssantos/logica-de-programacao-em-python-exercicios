num = 1                         # Início da sequência de números
for linha in range(3):          # Laço externo controla as linhas
    for coluna in range(3):     # Laço interno controla as colunas
        print(num, end=' ')     # Imprime o número na mesma linha
        num = num + 1           # Incrementa o número
    print()                     # Quebra a linha após cada conjunto de três números