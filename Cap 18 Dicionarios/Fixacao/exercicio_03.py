contatos = {} # Dicionário de contatos

print("CONTATOS")
while True:
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar todos")
    print("0 - Sair")
    opcao = int(input("Opção desejada: "))

    if opcao == 1:
        nome = input("Insira o nome do contato: ")
        telefone = input("Insira o telefone do contato: ")
        contatos[nome] = telefone
    elif opcao == 2:
        nome = input("Insira o nome do contato: ")
        contatos.pop(nome)
    elif opcao == 3:
        nome = input("Insira o nome do contato: ")
        if nome in contatos:
            print(contatos[nome])
        else:
            print("Contato não encontrado.")
    elif opcao == 4:
        for c in contatos.items():
            print(c)
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")