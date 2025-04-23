import math

def area_circulo(raio):
    return math.pi * raio ** 2

r = float(input("Raio: "))
print("Área:", area_circulo(r))
