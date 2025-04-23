compri = float(input("Comprimento: "))
alt = float(input("Altura: "))
preco_m2 = float(input("Preço por metro quadrado: "))

area = compri * alt
total = area * preco_m2

print(f"Área: {area} m²")
print(f"Preço total: {total:.2f}€")

if area >= 150:
    print("Tereno de grande dimenao")
else:
    print("Tereno de pequena dimensao")
