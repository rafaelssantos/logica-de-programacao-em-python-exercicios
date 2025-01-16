def exibir_menu():
    print("\n=== Lista de Compras ===")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")
    print("========================")

def adicionar_item(lista):
    item = input("Digite o nome do item para adicionar: ").strip()
    lista.append(item)
    print(f"'{item}' adicionado à lista.")

def remover_item(lista):
    item = input("Digite o nome do item para remover: ").strip()
    if item in lista:
        lista.remove(item)
        print(f"'{item}' removido da lista.")
    else:
        print(f"'{item}' não está na lista.")

def exibir_lista(lista):
    if lista:
        print("\nItens na lista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print("\nA lista de compras está vazia.")


def main():
    lista = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            remover_item(lista)
        elif opcao == "3":
            exibir_lista(lista)
        elif opcao == "4":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
