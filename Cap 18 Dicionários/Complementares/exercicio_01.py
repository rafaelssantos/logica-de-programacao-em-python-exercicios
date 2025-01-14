def desconto(produtos, desconto):
    for p in produtos:
        for chave, valor in p.items():
            p[chave] = p[chave] - desconto * p[chave]
        

def main():
    produtos = []
    produtos.append({"açúcar" : 7.99})
    produtos.append({"arroz" : 25.00})
    produtos.append({"feijão" : 10.50})

    print("Antes do desconto de 20%")
    print(produtos)

    desconto(produtos, 0.20)

    print("Após o desconto de 20%")
    print(produtos)

if __name__ == "__main__":
    main()