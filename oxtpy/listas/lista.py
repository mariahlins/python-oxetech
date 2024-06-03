#soma todos os elementos da lista
lista=[1,2,3,4,5,6,7,8,9]
soma=0
for i in lista:
    soma+=i

print(soma)


#encontra e remove duplicatas
dupli=[1,2,2,3,4,4,5,5,5,5,6]
i=0
while i < len(dupli):
    if dupli.count(dupli[i]) > 1:
        while dupli.count(dupli[i]) > 1:
            dupli.remove(dupli[i])
    i+=1

print(dupli)