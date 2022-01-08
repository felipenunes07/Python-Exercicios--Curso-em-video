temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar: [S/N]'))
    if r in 'Nn':
        break
print('-='*30)
print('Ao todo, você cadastrou {} pessoas'.format(len(princ)))
print('O maior  peso foi de {} Kg.Peso de '.format(maior),end='')
for p in princ:
    if p[1] == maior:
        print('[{}] '.format(p[0]))
print('O menor  peso foi de {} Kg '.format(menor),end='')
for p in princ:
    if p[1] == menor:
        print('[{}]'.format(p[0]))
