# Crie um programa que leia o nome de uma pessoa, mostre o primeiro e último nome.

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Prazer em te conhecer {}.'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
