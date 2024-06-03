popA=80000
popB=200000
ano=0
while popA<=popB:
    popA+=popA*0.03
    popB+=popB*0.015
    ano=ano+1
print(ano)