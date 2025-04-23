def num_for_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número: "))
if num_for_primo(num):
    print("É primo")
else:
    print("Não é primo")
