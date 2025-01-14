import random
import struct

def gerar_lista_aleatoria(n=100):
    """Gera uma lista de números inteiros aleatórios."""
    lista  = []
    for e in range(n):
        lista.append(random.randint(0, n))
    return lista

def salvar_em_arquivo_binario(lista, caminho_arquivo):
    """Salva a lista de números inteiros em um arquivo binário."""
    with open(caminho_arquivo, 'wb') as f:
        for numero in lista:
            # Usa struct.pack para converter o número inteiro para bytes e gravar no arquivo
            f.write(struct.pack('i', numero))

def main():
    # Solicita ao usuário a quantidade de números e o caminho do arquivo
    n = int(input("Digite a quantidade de números desejada: "))
    caminho_arquivo = input("Digite o caminho do arquivo para salvar os números: ")

    # Gera a lista de números aleatórios
    lista_numeros = gerar_lista_aleatoria(n)

    # Salva a lista no arquivo binário
    salvar_em_arquivo_binario(lista_numeros, caminho_arquivo)

    print(f"{n} números foram gerados e salvos no arquivo {caminho_arquivo}.")

if __name__ == "__main__":
    main()
