from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while  opcao!= 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção: '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n2))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=')
print('FINALIZANDO...')
sleep(3)
print('FIM DO PROGRAMA VOLTE SEMPRE!!!')