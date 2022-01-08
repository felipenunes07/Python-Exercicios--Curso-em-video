num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão: 
[ 1 ] Converter para BÍNARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Bínario é igual a {}.'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.Tente novamente.')