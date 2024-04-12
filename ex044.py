# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto.
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
''' sistema de loja '''
print("{:=^40}".format(' \033[1:31mSS GAMERS\033[m '))
preço = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO VOCÊ DESEJA:
[1] á vista dinheiro/cheque, 10% de desconto..
[2] á vista no cartão, 5% de desconto.
[3] em 2x no cartão.
[4] 3x ou mais no cartão, tem 20% de desconto.''')
opção = int(input('Qual a sua opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra foi parcelada em 2x de R${:.2f}, sem juros.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totaparc = int(input('Quantas parcelas?'))
    parcela = total / totaparc
    print('Sua compra foi parcelada em {}x de R${:.2f}, com juros.'.format(totaparc, parcela) )
else:
    total = preço
    print('Opção inválida de pagamento.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
print("\033[1:31m{:*^40}".format('OBRIGADO POR COMPRAR NA SS GAMERS.'))