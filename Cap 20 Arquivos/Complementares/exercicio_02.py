def buscar_palavra_em_arquivo(caminho_arquivo, palavra_chave):
    """Verifica a existência de uma palavra-chave em um arquivo de texto."""
    # Abre o arquivo no modo leitura
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    
    # Verifica se a palavra-chave está no conteúdo
    if palavra_chave in conteudo:
        return True
    else:
        return False
    
    
def main():
    # Solicita ao usuário o caminho do arquivo e a palavra-chave
    caminho_arquivo = input("Digite o caminho do arquivo: ")
    palavra_chave = input("Digite a palavra-chave a ser buscada: ")

    # Realiza a busca da palavra-chave no arquivo
    buscar_palavra_em_arquivo(caminho_arquivo, palavra_chave)

if __name__ == "__main__":
    main()
