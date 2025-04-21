equipa1 = input("Nome da primeira equipa: ")
golos1 = int(input(f"Golos da {equipa1}: "))

equipa2 = input("Nome da segunda equipa: ")
golos2 = int(input(f"Golos da {equipa2}: "))

if golos1 > golos2:
    print(f"A vitória foi da equipa {equipa1}")
elif golos2 > golos1:
    print(f"A vitória foi da equipa {equipa2}")
else:
    print("O jogo foi um empate.")
