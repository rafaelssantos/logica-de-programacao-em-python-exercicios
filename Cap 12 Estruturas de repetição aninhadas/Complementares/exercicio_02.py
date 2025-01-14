print("Tabela de Multiplicação (1 a 5):\n")

for i in range(1, 6):       # Laço externo: percorre os multiplicadores
    for j in range(1, 6):   # Laço interno: percorre os multiplicandos
        resultado = i * j
        print(f"{i} x {j} = {resultado}", end='\t')  # Formatação em colunas
    print()  # Quebra de linha ao final de cada linha da tabela