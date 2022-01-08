tot18 = toth = totm20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UM PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        toth = toth + 1
    if idade >= 18:
        tot18 = tot18 + 1
    if idade < 20 and sexo == 'F':
        totm20 = totm20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}.'.format(tot18))
print('Ao todo temos {} homens cadastrados.'.format(toth))
print('E temos {} mulheres com menos de 20 anos'.format(totm20))