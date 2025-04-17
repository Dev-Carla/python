import math

#VAlor de PI
print(math.pi)

# Raiz Quadrada
print(math.sqrt (16))

#Fatorail
print(math.factorial(19))

#arredondar por excesso
print(math.ceil(19.63246768))

#arredondar por Defeito
print(math.floor(19.63246768))

# Potencia
print(math.pow(5,2))

# Potencia de base e
print(math.exp(1))

# seno cos tg 
print(math.sin(45))

# seno cos tg em radianos
print(math.cos(math.radians(45)))

# seno cos tg em radianos para graus
print(math.degrees(math.pi * 2))

# converte um valor de grau para radiano
print(math.radians(360))

# Logaritmo
print(math.log(6,2))

# Truncar um Valor: Eliminar as casas decimais
print(math.trunc(45.567890))


# Comparar valores com tolerancia relativa ou abs
print(math.isclose(1,1.000001,rel_tol=1e-5))
print(math.isclose(1,1.000001,abs_tol=1e-2))