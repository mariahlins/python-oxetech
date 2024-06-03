salario = float(input('Digite o valor do salário\n'))

print(f"Salário antes do reajuste: R${salario}")

if salario<=280:
    aumento=1.2
    percentual=20
elif salario>280 and salario<=700:
    aumento=1.15
    percentual=15
elif salario>700 and salario<=1500:
    aumento=1.1
    percentual=10
elif salario>1500:
    aumento=1.05
    percentual=5

print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R${salario*aumento - salario}")
print(f"Novo salário após o aumento: R${salario*aumento}")