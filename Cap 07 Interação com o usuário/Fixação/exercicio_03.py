valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

# A troca de elementos necessita na maior parte das linguagens de programação 
# de uma variável auxiliar. No mundo real, é possível enxergar o algoritmo da seguinte forma.
# Pense em um copo com suco e um copo com café, só é possível trocar os líquido com a 
# utilização de um terceiro copo.

auxiliar = valor1
valor1 = valor2
valor2 = auxiliar

print("Primeiro valor: ", valor1)
print("Segundo valor: ", valor2)