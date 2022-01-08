from random import randint
computador = randint(0,10)
print('''Sou seu computador ...
Acabei de pensar em um número entre 0 e 10.
Será que consegue advinhar qual foi: ''')
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    cont = cont + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(cont))