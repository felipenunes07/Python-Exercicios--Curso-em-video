from time import  sleep

def contador(i,f,p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ' ,end='',flush=True)
            sleep(0.5)
            cont = cont + p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont = cont - p
        print('FIM!')


# Programa principal
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini,fim,passo)