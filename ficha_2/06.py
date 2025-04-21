num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
operacao = input("Operação (+, -, *, /): ")

if operacao == '+':
    print("Resultado:", num1 + num2)
elif operacao == '-':
    print("Resultado:", num1 - num2)
elif operacao == '*':
    print("Resultado:", num1 * num2)
elif operacao == '/':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")
