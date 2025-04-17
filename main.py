# a) importar o módulo meu_modulo
import meu_modulo

# b) importar uma função específica do módulo meu_modulo
from meu_modulo import soma

# c) importar todas as funções do módulo meu_modulo
from meu_modulo import *

# d) renomear o módulo meu_modulo
import meu_modulo as mm

# e) renomear uma função específica de meu_modulo
from meu_modulo import divisao as div

# f) usar as funções importadas no programa
a = 10
b = 3

print("Usando mm.soma:", mm.soma(a, b))
print("Usando função soma:", soma(a, b))
print("Usando função multiplicacao:", multiplicacao(a, b))
print("Usando função renomeada div:", div(a, b))
print("Divisão inteira:", divisao_inteira(a, b))
print("Potência:", potenciacao(a, b))
print("Módulo:", modulo(a, b))
