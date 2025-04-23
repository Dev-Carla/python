def num_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

print("Números perfeitos de 1 até 1000:")
for num in range(1, 10000):
    if num_perfeito(num):
        print(num)
