# Programa que pede a senha até o usuário acertar.

senha = input("Digite a senha: ")

while senha != "1234":
    print("Senha incorreta!")
    senha = input("Digite a senha: ")

print("Acesso permitido!")