v = int(input('Qual é a velocidade atual do carro: '))
if v > 80:
    print('\033[31m MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('\033[31m Você deve pagar uma multa de \033[36mR${}! '.format((v-80)*7))
else:
    print('\033[32m Tenha um bom dia! Dirija com segurança!')