"""programa de sorte"""
import random

n1 = str(input('Digite um nome:'))
n2 = str(input('Digite um nome:'))
n3 = str(input('Digite um nome:'))
n4 = str(input('Digite um nome:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
escolhido2 = random.choice(lista)
print('O aluno escolhido foi {} e {}'.format(escolhido, escolhido2))