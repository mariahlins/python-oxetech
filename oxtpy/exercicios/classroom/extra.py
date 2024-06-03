from random import randint
guess=int(input("Digite um número entre 1 e 100: "))
number=randint(1,100)

while guess!=number:
    if guess>number:
        guess=int(input("O número que você escolheu é MAIOR que o sorteado, tente novamente: "))
    elif guess<number:
        guess=int(input("O número que você escolheu é MENOR que o sorteado, tente novamente: "))

print("Parabéns! Você acertou o número sorteado")