def formar_endereco(*, rua, numero, bairro, cidade, estado):
    return f"{rua}, {numero} - {bairro}, {cidade} - {estado}"

print(formar_endereco(
    estado="Santiago",
    cidade="Praia",
    bairro="Tira Chapéu",
    rua="Capela São José",
    numero=16
))
