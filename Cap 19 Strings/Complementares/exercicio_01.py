string = input("Informe uma string: ")

if string.lower() == string.lower()[::-1]:
    print("Palíndromo.")
else:
    print("Não é palíndromo.")