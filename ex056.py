idtotal = 0
maisvelho = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-----{} PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idtotal = idtotal + idade
    if p ==1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        nomevelho = nome
        maisvelho = idade
    if sexo in 'Ff' and idade <20:
        totmulher20 = totmulher20 + idade

print('A média de idade do grupo é de {} anos.'.format(idtotal/4))
print('O homem mais velho tem {} anos e tem nome {}'.format(maisvelho,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))