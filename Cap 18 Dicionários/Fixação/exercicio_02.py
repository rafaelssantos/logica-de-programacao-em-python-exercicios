print("CADASTRO DE PRODUTOS")

n = int(input("Quantos produtos deseja cadastrar? "))

produtos = [] # Lista de produtos

for e in range(n):
    produto = {}
    produto["Descrição"] = input("Informe a descrição: ")
    produto["Valor"] = float(input("Informe o valor: "))
    produto["Código de barras"] = int(input("Informe o código de barras: "))
    produtos.append(produto) # Adiciona produto a lista de produtos
    print("Cadastro realizado com sucesso!")

print("PRODUTOS CADASTRADOS")
print(produtos)