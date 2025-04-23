equipa_1 = input("Nome da primeira equipa: ")
golos_1 = int(input(f"Golos da {equipa_1}: "))

equipa_2 = input("Nome da segunda equipa: ")
golos_2 = int(input(f"Golos da {equipa_2}: "))

if golos_1 > golos_2:
    print(f"A vitória foi da equipa {equipa_1}")
elif golos_2 > golos_1:
    print(f"A vitória foi da equipa {equipa_2}")
else:
    print("O jogo foi um empate.")
