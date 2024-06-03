str=input("Digite uma frase: ")
str=str.lower()
cont=0
for i in str:
    if i in 'aeiou':
        cont+=1
print(f"A frase digitada tem {cont} vogais")