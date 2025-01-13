a = float(input("Informe o coeficiente de A de uma equação do segundo grau: "))
b = float(input("Informe o coeficiente de B de uma equação do segundo grau: "))
c = float(input("Informe o coeficiente de C de uma equação do segundo grau: "))
print(f"{a}x² + {b}x + {c} = 0")

delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** (0.5)) / (2 * a)
x2 = (-b - delta ** (0.5)) / (2 * a)

print(f"As raízes da equação são {x1} e {x2}.")

