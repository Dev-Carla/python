salario = float(input("Salario recebido: "))
gasto = float(input("Total gasto: "))
saldo = salario - gasto

if gasto == salario:
    print("Gasto igual ao orçamento")
elif gasto < salario:
    print("Gasto dentro do orçamento")
else:
    print("Orçamento ultrapassado")

print(f"Saldo: {saldo:.2f}€")
