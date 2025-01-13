litros = float(input("Qual quantidade abastecida em litros? "))
preco_por_litro = float(input("Qual o preço por litro? "))

valor_a_ser_pago = litros * preco_por_litro

print(f"O valor a ser pago é de R$ {valor_a_ser_pago:.2f}")