def soma(qtd):
    total = 0
    for i in range(qtd):
        valor = int(input(f"Digite o {i+1}º número: "))
        total += valor
    return total

n = int(input("Quantos números quer somar? "))
print("Soma:", soma(n))
