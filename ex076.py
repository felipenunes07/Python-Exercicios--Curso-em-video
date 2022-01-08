listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Compasso',4.20,
            'Mochila', 120.50,
            'Caneta', 22.30,
            'Livro' , 34.90)
print('-'*40)
print(f'{''LISTAGEM DE PREÇOS'':.<30}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
