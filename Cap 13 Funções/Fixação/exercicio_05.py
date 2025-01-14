def fatorial(num):
    produto = 1
    for e in range(num, 0, -1):
        produto = produto * e
    return produto

# -----------------------
num = int(input("Informe o número: "))
fat = fatorial(num)
print(fat)