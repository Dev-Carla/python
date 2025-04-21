inicio = int(input("Valor inicial: "))
fim = int(input("Valor final: "))

for i in range(inicio, fim + 1):
    if i % 3 != 0:
        continue
    print(i, end=' ')
