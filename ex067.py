tabuada = int(input('Quer ver a tabuada de qual valor: '))
print('-'*40)
while tabuada >0:
    for c in range(1,11):
        print(' {} x {} = {}'.format(tabuada,c,tabuada*c))
    print('-' * 40)
    tabuada = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')