numero = int(input("Digite um número entre 1 e 10: "))
while numero<0 or numero>10:
    numero=int(input("Digite um número válido: "))

for i in range(1,11):
    print(f"{numero} X {i} = {numero * i}")