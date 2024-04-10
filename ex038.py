#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
if n1 > n2:
    print('Primeiro número é maior que o segundo.')
elif n2 > n1:
    print('Segundo número é maior que o primeiro.')
else:
    print('Os dois são iguais.')

