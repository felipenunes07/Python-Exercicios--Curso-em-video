print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+ r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima \033[34mPODEM FORMAR triângulo.', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1!= r2!= r3!= r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR triângulo.')
