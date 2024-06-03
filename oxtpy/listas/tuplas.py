# Acessa o primeiro e o ultimo elemento
tupl=(1,2,3,4,5,6,7,8,9)
print(tupl[0],tupl[len(tupl)-1])

#conta elementos
tupla=(0,0,0,1,2,2,3,3,3,4,4,4,4,5,5)
src=int(input("Digite o número de busca (0-5):  "))
print(f"O número {src} apareceu {tupla.count(src)} vezes na tupla")