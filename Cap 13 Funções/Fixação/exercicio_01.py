def area_retangulo(base, altura):
    area  = base * altura
    return area

# ---------------------------------------------------------------------
base = float(input("Informe a base: "))
altura = float(input("Informe a altura: "))

area = area_retangulo(base, altura)     # Chamada da função
print("A área é", area)
