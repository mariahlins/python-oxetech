numero=int(input("Digite um numero: "))
soma=0
while numero>0:
    soma+=(numero%10)
    numero//=10

print(soma)