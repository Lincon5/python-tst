""" faça um programa que leia, um ângulo qualquer e mostre na tela o valor do senmo, cosseno e tangente desse ângulo."""

"""import math
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ngulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ângulo, tangente))"""

# modelo a  baixo, fazendo usando uma importação especifica.

from math import radians, sin, cos, tan
ângulo = float(input('Digite o valor do ângulo:'))
seno = sin(radians(ângulo))
print('O valor do ângulo e {} o seno tem {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O valor do ângulo e {} o cosseno tem {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O valor do ângulo e {} o tangente tem {:.2f}'.format(ângulo, tangente))