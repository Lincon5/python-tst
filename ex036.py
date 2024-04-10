#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: R$'))
salário = float(input('Salário dpo comprador: R$'))
anos = int(input('Quantos anos deseja finaciar?'))
prestação = valor / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar a casa de R${:.2f} em {} anos a prestação ficará de R${:.2f}, por mês.'.format(valor, anos, prestação))
if prestação <= mínimo:
    print('\033[0;35mEmpréstimo APROVADO!\033[m')
else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')