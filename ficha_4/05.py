def calcular_idade(ano_nascimento):
    return 2025 - ano_nascimento


nasc = int(input("Ano de nascimento: "))
idade = calcular_idade(nasc)

print(f"Idade: {idade} anos")
