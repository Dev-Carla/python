comprimento = float(input("Comprimento: "))
altura = float(input("Altura: "))
preco_m2 = float(input("Preço por metro quadrado: "))

area = comprimento * altura
total = area * preco_m2

print(f"Área: {area} m²")
print(f"Preço total: {total:.2f}€")

if area >= 150:
    print("Terreno de grande dimensão")
else:
    print("Terreno de pequena dimensão")
