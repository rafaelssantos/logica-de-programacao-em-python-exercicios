def metros_para_quilometros(metros):
    quilometros = metros / 1000
    return quilometros

# --------------------------------------------
metros = float(input("Informe um valor em metros: "))
quilometros = metros_para_quilometros(metros)

print("O valor em quilômetros é", quilometros)