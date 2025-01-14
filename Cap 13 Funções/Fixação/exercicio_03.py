def operacao(a, b = 5):
    return (a + b) / b

print(operacao(10, 2))
print(operacao(10))

# Linha 4. Os parâmetros são passados de forma posicional, a = 10 e b = 2. Logo, é resolvida a expressão (10 + 2) / 2 = 6.
# Linha 5. O primeiro parâmetro é posiconal e o segundo é padrão, a = 10 e b = 5. Logo, é resolvid a expressão (10 + 5) / 5 = 3