'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''


p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda Nota: '))
media = (p1+p2)/2
print('Tirando {} e {}, a média do aluno é  {}.'.format(p1,p2,media))
if media >= 6:
    print('O aluno esta \033[34mAPROVADO!!!')
else:
    print('O aluno está \033[31mREPROVADO!!!')
