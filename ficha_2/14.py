# Padrão 1: 5 linhas de 5 asteriscos
for i in range(5):
    print("*****")

print()  # separador

# Padrão 2: em forma de triângulo invertido
for i in range(5, 0, -1):
    print("*" * i)

print()  # separador

# Padrão 3: 3 linhas com "********"
for i in range(3):
    print("********")

print()  # separador

# Padrão 4: a b c
for letra in ['a', 'b', 'c']:
    print(letra, end=' ')
