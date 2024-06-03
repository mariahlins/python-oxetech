import random

def desenho(tentativas):
    estagios = [
        """
          -----
          |   |
          |   O
          |  /|\\
          |  / \\
          |
        --------
        """,
        """
          -----
          |   |
          |   O
          |  /|\\
          |  / 
          |
        --------
        """,
        """
          -----
          |   |
          |   O
          |  /|\\
          |  
          |
        --------
        """,
        """
          -----
          |   |
          |   O
          |  /|
          |  
          |
        --------
        """,
        """
          -----
          |   |
          |   O
          |   |
          |  
          |
        --------
        """,
        """
          -----
          |   |
          |   O
          |   
          |  
          |
        --------
        """,
        """
          -----
          |   |
          |   
          |   
          |  
          |
        --------
        """
    ]
    print(estagios[tentativas])

palavras=['amora', 'banana', 'caju', 'damasco', 'abacate', 'abacaxi', 'morango']
palavra=random.choice(palavras).lower()
oculta=['*'] * len(palavra)  

tentativas=6 
erros=[]

while tentativas > 0 and '*' in oculta:
    print("\nPalavra: " + " ".join(oculta))
    print(f"Você ainda tem {tentativas} tentativas restantes.")
    if erros:
        print(f"Letras erradas: {', '.join(erros)}")
    
    letra=input("Digite uma nova letra: ").lower()

    if not letra.isalpha() or len(letra)!=1:
        print("Entrada inválida. Digite uma única letra.")
        continue

    if letra in erros or letra in oculta:
        print("Você já digitou essa letra. Tente novamente.")
        continue

    if letra in palavra:
        for idx, char in enumerate(palavra):
            if char==letra:
                oculta[idx]=letra
    else:
        erros.append(letra)
        tentativas-=1

    desenho(tentativas)

if '*' not in oculta:
    print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
