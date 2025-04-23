def velocidade_media(distancia, tempo, unidade="km/h"):
    velocidade = distancia / tempo
    return f"{velocidade} {unidade}"



print(velocidade_media(100, 2))

