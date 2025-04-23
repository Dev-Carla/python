def media(n1, n2, n3, tipo):
    if tipo.upper() == "A":
        return (n1 + n2 + n3) / 3
    elif tipo.upper() == "P":
        return (n1*5 + n2*3 + n3*2) / 10
    else:
        return 0

a = float(input("Nota 1: "))
b = float(input("Nota 2: "))
c = float(input("Nota 3: "))
letra = input("Tipo de média (A/P): ")
print("Resultado:", media(a, b, c, letra))
