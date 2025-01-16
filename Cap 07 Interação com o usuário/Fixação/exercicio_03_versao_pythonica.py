valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

# Python permite a troca de valores entre variáveis de forma Pythônica com a utilização de
# uma atribuição em tupla
valor1, valor2 = valor2, valor1

print("Primeiro valor: ", valor1)
print("Segundo valor: ", valor2)