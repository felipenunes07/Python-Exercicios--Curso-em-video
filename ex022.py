nome = input('Digite o seu nome completo: ').strip()
print('Seu nome em maiusculas é {}.'.format(nome.upper()))
print('Seu nome em minuscula é {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(separa[0])))

