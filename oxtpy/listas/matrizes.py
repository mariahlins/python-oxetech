matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#printa cada elemento individualmente
#acessa cada lista e printa os elementos da lista
for i in matriz:
    for j in i:
        print(j)

#soma de diagonais
soma1=0
soma2=0
for i in range(len(matriz)):
    soma1+=matriz[i][i]
    soma2+=matriz[i][len(matriz)-1-i]

print(f"Soma da diagonal principal: {soma1}\nSoma da diagonal secundária: {soma2}")

