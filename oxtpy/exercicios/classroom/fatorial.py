numero=int(input("Digite um número: "))
num=numero

fatorial=1
while num!=1:
    fatorial*=num
    num-=1

print(f"O fatorial de {numero} é: {fatorial}")