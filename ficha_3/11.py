def num(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

x = float(input("Número: "))
print("Resultado:", num(x))
