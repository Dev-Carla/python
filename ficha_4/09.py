def mensagem_personalizada(*, nome, sobrenome, saudacao):
    return f"{saudacao}, {nome} {sobrenome}!"

print(mensagem_personalizada(
    saudacao="Bom dia",
    nome="Carla",
    sobrenome="Martins"
))
