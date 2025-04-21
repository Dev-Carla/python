num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
operacao = input("Operação (+, -, *, /): ")

match operacao:
    case '+':
        print("Resultado:", num1 + num2)
    case '-':
        print("Resultado:", num1 - num2)
    case '*':
        print("Resultado:", num1 * num2)
    case '/':
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")
