# faça um programa para calcular a diaraia do carro alugado.

dias = int(input('Quantos dias alugados?'))
km = float(input('Qunatos km rodados?'))
pago = (dias * 60) + (km * 0.15)
desconto = pago - (pago * 10 / 100)
print('O total a pagar é de R${:.2f}'.format(pago))
print('Pagando  o valor R${:.2F} no dinheiro tem desconte de R${:.2f}'.format(pago, desconto))


