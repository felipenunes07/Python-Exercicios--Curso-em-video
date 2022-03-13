# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Me diga um número qualquer: '))
if n % 2 == 0:
    print('o Numero {} é \033[34mPar '.format(n))
else:
    print('O número {} é \033[34mÍMPAR.'.format(n))
