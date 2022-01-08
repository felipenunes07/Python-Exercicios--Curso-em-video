print('LOJAS GUANABARA')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    print('Sua compra de R${} vai custar {} no final.'.format(preco,preco*0.9))
elif opcao == 4:
    parcelas = int(input('quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.1f} COM JUROS'.format(parcelas,(preco/parcelas)*1.2))
    print('Sua compra de {} vai custar R${} no final.'.format(preco,preco*1.2))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${} SEM JUROS'.format(preco/2))
elif opcao == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(preco,preco*0.95))
else:
    print('Opção INVALIDA de pagamento. Tente novamente.')