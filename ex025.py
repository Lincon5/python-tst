# Crie um programa que leia que leia um nome de uma pessoa, e diga se ela tem 'Silva ' no nome.

nome = str(input('Diga seu nome completo, por favor:')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

# o in e um operador do python.