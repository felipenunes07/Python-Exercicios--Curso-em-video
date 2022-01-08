a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor'))
c = int(input('Terceiro Valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi \033[34m{}\033[m.'.format(menor))
print('O maior valor digitado foi \033[31m{}\033[m.'.format(maior))