from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.',end=' ')
    print('DEU PAR'if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 ==0:
            print('\33[34mVocê VENCEU\33[m')
            v += 1
        else:
            print('\33[31mVocê PERDEU!\33[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\33[34mVocê Venceu\33[m')
            v += 1
        else:
            print('\33[31mVocê PERDEU!\33[m')
            break
    print('Vamos jogar novamente...')
print('\33[31mGAME OVER!\33[m Você venceu {} vezes.'.format(v))