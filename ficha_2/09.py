inicio = int(input("Valor inicial: "))
fim = int(input("Valor final: "))
tipo = input("Tipo de contagem (crescente/decrescente): ")

if tipo.lower() == "crescente":
    for i in range(inicio, fim + 1):
        print(i, end=' ')
else:
    for i in range(inicio, fim - 1, -1):
        print(i, end=' ')
