import analise_combinatoria

def main():
    print("Escolha a operação desejada:")
    print("1. Permutação")
    print("2. Arranjo")
    print("3. Combinação")

    opcao = int(input("Digite o número da operação: "))
    
    n = int(input("Informe o valor de n (número total de elementos): "))    
    if opcao == 1:
        resultado = analise_combinatoria.permutacao(n)
        print(f"O resultado da permutação é: {resultado}")
    elif opcao == 2:
        k = int(input("Informe o valor de k (número de elementos selecionados): "))
        resultado = analise_combinatoria.arranjo(n, k)
        print(f"O resultado do arranjo é: {resultado}")
    elif opcao == 3:
        k = int(input("Informe o valor de k (número de elementos selecionados): "))
        resultado = analise_combinatoria.combinacao(n, k)
        print(f"O resultado da combinação é: {resultado}")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()