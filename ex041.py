#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação do atleta:Mirim.')
elif idade <= 14:
    print('Classificação do atleta:Infantil')
elif idade <= 19:
    print('Classificação do atleta:Júnior')
elif idade <= 25:
    print('Classificação do atleta:Sênior.')
elif idade > 25:
    print('Classificação do atleta:Master.')

# else:
#     print('Classificação do atleta:Master'), posso fazer assim também na última escolha.