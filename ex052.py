num = int(input('Digite um número: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[034m',end='')
        tot = tot+1
    else:
        print('\033[31m',end='')
    print('{} '.format(c),end='')
print('\n\033[mO numero {} foi dividio {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele É ')
else:
    print('E por isso ele NÃO É PRIMO')