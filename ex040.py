p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda Nota: '))
media = (p1+p2)/2
print('Tirando {} e {}, a média do aluno é  {}.'.format(p1,p2,media))
if media >= 6:
    print('O aluno esta \033[34mAPROVADO!!!')
else:
    print('O aluno está \033[31mREPROVADO!!!')