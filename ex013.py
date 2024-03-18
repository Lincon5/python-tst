# Ajuste de salário de funcionários, com novo ajuste de 15%.

#salário = float(input('Qual é o salário do funcionário? R$'))
#novo = salário + (salário * 15 / 100)
#print('um funcionario que ganhava R${:.2f}, com o ajuste de 15% de aumento, passou a receber  R${:.2f}'.format(salário, novo))

valor = float(input('Qual valor do produto? R$'))
desconto = valor - (valor * 20 / 100)
parcelado = valor + (valor * 45 / 100)
print('Produto custa R${:.2F}, pagando avista ele sai a R${:.2f}'.format(valor,  desconto))
print('Produto custa R${:.2f}, pagando ele parcelado em 12X está saindo a R${:.2f}'.format(valor, parcelado))
