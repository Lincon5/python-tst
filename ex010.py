#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.40
print('Você com R${:.2f} pode comprar U${:.2f}'.format(real, dolar))


