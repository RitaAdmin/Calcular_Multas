import os
import time

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

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        escolha= menu()
        
        escolha= input("Escolha a opção que pretente (0 a 3): ")
        
        if escolha=="0":
            print("Sair programa com sucesso")
            break
            
        if escolha in("1","2","3"):
            try:   
                velocidade = float(input("Qual a velocidade em que seguia o seu carro (km/h): "))
            except ValueError:
                print("Erro, o numero que inseriu nao é valido por favor insira um número válido.")
                continue
            
            
            if escolha == "1":
                multa = multa_localidade(velocidade)
            
            elif escolha == "2":
                multa = multa_fora_localidade(velocidade)
            
            elif escolha == "3":
                multa = multa_autoestrada(velocidade)

            if multa == 0:
                print("Sem multa. Condução dentro do limite de velocidade.")
            else:
                print(f"Multa a pagar: {multa}€")
        else:
            print("Opção não é válida. Por favor, tente outra vez")
        
        

