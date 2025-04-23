def preco_com_desconto(preco):
    return preco * 0.9  

preco = float(input("Preço original: "))
final = preco_com_desconto(preco)

print(f"Preço com 10% de desconto: {final:.2f}$")
