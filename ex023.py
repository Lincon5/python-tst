# Crie um programa que leia um número de 0 a 9999, e mostre na tela.

num = int(input('Digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade é: {}'.format(u))
print('Dezenas é: {}'.format(d))
print('Centena é: {}'.format(c))
print('Milhar é: {}'.format(m))
print('Obrigado pela tentativa!')
