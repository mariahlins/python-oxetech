str=input("Digite uma palavra: ")
i=0
j=len(str)-1
palindromo=True
while i<j:
    if str[i]!=str[j]:
        palindromo=False
        break
    i+=1
    j-=1
if palindromo:
    print("É palíndromo")
else:
    print("Não é palíndromo")
