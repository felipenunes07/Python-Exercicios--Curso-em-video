lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0 :
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar: [S/N]:' ))
    if r in 'Nn':
        break
print('-='*30)
print('A lista completa é {}'.format(lista))
print('A lista de pares é {}'.format(pares))
print('A lista de impares é {}'.format(impares))
