## Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. ##


import math
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {}.'.format(math.sqrt((a**2)+(b**2))))
