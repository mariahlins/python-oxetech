nome=input("Digite seu nome: ")
while len(nome) < 3:
    nome=input("Digite um nome válido: ")

idade=int(input("Digite sua idade: "))
while idade<=0 or idade>=150:
    idade=int(input("Digite uma idade válida: "))

salario=int(input("Digite seu salário: "))
while salario<0:
    salario=int(input("Digite um valor válido: "))

sexo=input("Digite seu sexo (F ou M):")
while sexo!='F' and sexo!='M':
    sexo=input("Digite F ou M: ")

estadoCivil=input("Digite seu estado civil (S, C, V ou D): ")
while estadoCivil!='S' and estadoCivil!='C' and estadoCivil!='V' and estadoCivil!='D':
    estadoCivil=input("Digite um estado válido (S, C, V ou D): ")