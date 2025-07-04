def multa_localidade(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    else:
        return 60
    
def multa_fora_localidade(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 120
    elif velocidade > 90:
        return 60
    else:
        return 0
    
def multa_autoestrada(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade > 175:
        return 360
    elif velocidade > 150:
        return 120
    elif velocidade > 120:
        return 60
    else:
        return 0

def menu():
    print("\n Sitema de Multas")
    print("\n------------------")
    print("1-Circular em Localidades")
    print("2-Circular fora de Localidades")
    print("3-Circular em Autoestada")
    print("0-Sair")