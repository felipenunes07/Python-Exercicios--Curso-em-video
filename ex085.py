num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite o {}o. um valor: '.format(c)))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print('Os valores PARES digitados foram {}'.format(num[0]))
print('Os valores ÍMPARES digitados foram {}'.format(num[1]))

