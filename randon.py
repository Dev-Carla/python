import random

#Gerar num inteiros aleatorios 
print(random.randint(1,10))

#Gerar num reais aleatorios num intervalo
print(random.uniform(1,2))

#Gerar num reais aleatorios num intervalo
print(random.uniform(1,2).__round__(2))

# Escolher Valores aleatorios numa lista
lista = ["Beatriz","Carla", "Cyara"]
print (random.choice(lista))

# Escolher Valores aleatorios numa string
nome = "Carla  Guilhereme"
print (random.choices(nome))