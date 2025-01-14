def copiar_arquivo(caminho_origem, caminho_destino):
    """Copia o conteúdo de um arquivo de texto para outro arquivo."""
  
    with open(caminho_origem, 'r') as arquivo_origem:
        # Lê o conteúdo do arquivo de origem
        conteudo = arquivo_origem.read()

    # Abre o arquivo de destino em modo de escrita
    with open(caminho_destino, 'w') as arquivo_destino:
        # Escreve o conteúdo no arquivo de destino
        arquivo_destino.write(conteudo)
    
    print(f"Conteúdo copiado de {caminho_origem} para {caminho_destino} com sucesso!")


def main():
    # Solicita ao usuário os caminhos dos arquivos
    caminho_origem = input("Digite o caminho do arquivo de origem: ")
    caminho_destino = input("Digite o caminho do arquivo de destino: ")

    # Copia o conteúdo do arquivo de origem para o destino
    copiar_arquivo(caminho_origem, caminho_destino)

if __name__ == "__main__":
    main()
