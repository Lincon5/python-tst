# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número:'))
print('''Escolha uma das base para conversão:
[1] converter para Binário.
[2] converter para Octal.
[3] converter para Hexadecimal.''')
opção = int(input('Qual a sua opção:'))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[0;31mOpção inválida.')
