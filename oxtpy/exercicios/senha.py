nome=input("Digite seu nome: ")
senha=input("Digite sua senha: ")

while senha==nome:
    print("Senha inválida")
    senha=input("Digite outra senha: ")

print("Informações válidas")