#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

casa = int(input('Valor da casa: R$ '))
salario = int(input('Salario do comprador: R$ '))
financiamento = int(input('Quantos anos de financiamento: '))
mensal = (casa/(12*financiamento))
print('Para pagar uma casa de de R${:.2f} em {} anos a prestaçao será de R${:.2f}.'.format(casa,financiamento,mensal))
if mensal > (0.3 * salario) :
    print('Empréstimo NEGADO!')
if mensal < (0.3 * salario) :
    print('Empréstimo CONCEDIDO!')
