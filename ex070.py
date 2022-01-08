print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)
tot = 0
maior1000 = 0
menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    resp = ' '
    tot = tot + preco
    cont = cont + 1
    if preco > 1000:
        maior1000 = maior1000 + 1
    if cont == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total de compras foi  R$ {}'.format(tot))
print('Temos {} produtos custando mais  de R$1000.00'.format(maior1000))
print('O produto mais barato {} que  custa R$ {}'.format(barato,menor))