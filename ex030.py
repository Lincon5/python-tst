# Programa de par ou ímpar.
"""print('#' * 30)
n = int(input('Digite um número:'))
resultado = n % 2 # essa operação vai indentificar se o número e ímpar ou par, por que  o resultado vai ser 0 ou 1.
if resultado == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número for {} ele é ÍMPAR.'.format(n))
print('#' * 30)"""

from random import randint
n = randint(0, 100)
print('Computador escolheu o  número {}.'.format(n))
r = n % 2
if r == 0:
    print('Número {} par.'.format(n))
else:
    print('Número {} ímpar'.format(n))
print('Parabéns número {}'.format(n))