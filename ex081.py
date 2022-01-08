lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont = cont + 1
    r = str(input('Quer continuar: [S/N] '))
    if r  in 'Nn':
        break
print('-='*30)
print('Você digitou {} valores'.format(cont))
lista.sort(reverse=True)
print('Os valores em ordem decrecente são {}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
