from time import sleep
from random import randint
item = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Sua Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(item[computador]))
print('Jogador jogou {}'.format(item[jogador]))
print('-='*11)
if jogador == 0 and computador == 1:
    print('\033[31mCOMPUTADOR VENCE')
elif  jogador == 1 and computador == 0:
    print('\033[32mJOGADOR VENCE')
elif jogador == 0 and computador == 2:
    print('\033[32mJOGADOR VENCE')
elif jogador == 2 and computador == 0:
    print('\033[31mCOMPUTADOR VENCE')
elif jogador == 1 and computador == 2:
    print('\033[31mCOMPUTADOR VENCE')
elif jogador == 2 and computador == 1:
    print('\033[32mJOGADOR VENCE')
elif jogador == computador:
    print('\033[34mEMPATE')

