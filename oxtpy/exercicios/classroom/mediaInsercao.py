cont=0
soma=0
while True:
    num=int(input())
    if num<0:
        break
    else:
        cont=cont+1
        soma+=num
print(f"Media geral: {soma/cont}")