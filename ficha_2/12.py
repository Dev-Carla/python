import random

numero_secreto = random.randint(1, 10)
tentativa = 0

while True:
    tentativa = int(input("Tenta adivinhar o número (1-10): "))
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    else:
        print("Tenta outra vez...")
