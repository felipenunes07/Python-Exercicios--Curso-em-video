cont = ('Zero' , 'um' , 'Dois' , 'Três' ,'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez', 'Onze' ,'Doze' ,'Treze', 'Quatorze' ,'Quinze',
        'Dezesseis' ,'Dezessete', 'Dezoito' ,'Dezenove', 'Vinte')
continuar = 0
while continuar != 'N':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente.', end=' ')
    print(f'Você digitou o número {cont[num]}')
    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()

print('Volte Sempre!!!')
