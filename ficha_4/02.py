def num_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n 

num = int(input("Digite um número: "))
if num_perfeito(num):
    print("É um número perfeito")
else:
    print("Não é um número perfeito")
