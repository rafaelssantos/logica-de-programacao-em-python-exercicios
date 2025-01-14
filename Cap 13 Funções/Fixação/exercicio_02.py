def divisao(a, b):
    return a / b

print(divisao(10, 2))
print(divisao(b=10, a=2))

# Chamada da linha 4 utiliza parâmetros posicionais. Desta forma, a = 10 e b = 2. Resulta em 5.
# Chamada da linha 5 utiliza parâmetros nomeados. Desta forma, a = 2 e b = 10. Resulta em 0,2.
