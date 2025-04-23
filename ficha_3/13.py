def num(n):
    return n*2, n/2, n % 2 == 0

x = float(input("Número: "))
dobro, metade, par = num(x)
print(f"Dobro: {dobro}")
print(f"Metade: {metade}")
print("É par?", par)
