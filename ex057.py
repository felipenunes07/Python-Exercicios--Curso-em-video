sexo = str(input('Informe o sexo [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados INVALIDOS.Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))