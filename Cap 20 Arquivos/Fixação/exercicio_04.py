entrada_usuario = input("Informe o usuário: ")
entrada_senha = input("Informe sua senha: ")

caminho_password_conf = "password.conf"
usuario = None
senha = None

with open(caminho_password_conf) as arquivo:
    usuario = arquivo.readline().replace("\n", "")
    senha = arquivo.readline().replace("\n", "")

if entrada_usuario == usuario:
    if entrada_senha == senha:
        print("Acesso liberado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário incorreto!")