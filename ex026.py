# Crie um program que leia uma frase pelo teclado  e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição  ela aparece a primeira vez.
# em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} quantas vezes nessa frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))