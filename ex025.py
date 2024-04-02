# Crie um programa que leia que leia um nome de uma pessoa, e diga se ela tem 'Silva ' no nome.

nome = str(input('Diga seu nome completo, por favor:')).strip()
print('Seu nome tem Silva? \033[0;32m{}\033[m'.format('silva' in nome.lower()))

# o in e um operador do python.