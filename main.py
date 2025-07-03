def calcular_multa_localidade(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    else:
        return 60