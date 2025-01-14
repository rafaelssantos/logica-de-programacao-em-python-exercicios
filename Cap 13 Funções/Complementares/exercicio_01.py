def menor_de_idade(idade):
    if idade < 18:
        return True
    else:
        return False
    

# --------------------------------------------
idade = int(input("Informe sua idade: "))
if menor_de_idade(idade):
    print("Menor de idade!")
else:
    print("Maior de idade!")