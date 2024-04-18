#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite uma frase:')).strip().upper() # usando 'strip' para tirar os espaços entre as palavras, e 'upper' para colcoar as letras em maiusculas.
palavras = frase.split() # aqui separei em uma lista.
junto = ''.join(palavras) # aqui juntei tudo em uma ‘string’ só.
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # aqui fiz o inverso.
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
