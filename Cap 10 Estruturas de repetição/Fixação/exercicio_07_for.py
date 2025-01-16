num = int(input("Informe um número: "))
cont_divisores = 0      # Elemento neutro da contagem

for e in range(1, num + 1):
    if num % e == 0:
        cont_divisores = cont_divisores + 1
    if cont_divisores >= 3:     # Não precisa continuar verificação. Já identificado que não é primo.
        break

    
if cont_divisores == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")