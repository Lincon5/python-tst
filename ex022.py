# Crier um programa que leia o nome completo de uma pessoa e mostre.
# * o nome com todas as letras maiúsculas. * o nome com todas as letra minúsculas. * quantas letras ao sem considerar os espaços. * quantidade de letra no primeiro nome.

nome = str(input('Digite seu nome:')).strip()
print('Análisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu primeiro nome tem {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))