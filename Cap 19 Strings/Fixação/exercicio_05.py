frase = input("Informe uma frase: ")
vogais = frase.lower().count("a") + frase.lower().count("e") + frase.lower().count("i") + frase.lower().count("o") + frase.lower().count("u")
print("O número total de vogais é", vogais)