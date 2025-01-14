import distancia

print("CALCULADORA")
print("1 - Conversão de quilômetros para milhas")
print("2 - Conversão de milhas para quilômetros")

opcao = int(input("Informe a opção: "))
if opcao == 1:
    km = float(input("Informe o valor em quilômetros: "))
    milhas = distancia.quilometros_para_milhas(km)
    print("Valor em milhas:", milhas)
elif opcao == 2:
    milhas = float(input("Informe o valor em milhas: "))
    km = distancia.milhas_para_quilometros(milhas)
    print("Valor em quilômetros:", km)
else:
    print("Opção inválida!")
