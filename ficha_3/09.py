def e_par(n):
    return "Y" if n % 2 == 0 else "N"

x = int(input("Número: "))
print("Resultado:", e_par(x))
