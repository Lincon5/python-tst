# 006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Primeira maneira de fazer.
#n = int(input('Digite um numero,por favor:'))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('o dobro de {} vale {}.'.format(n, d))
#print('O triplo de {} vale {}.'.format(n, t))
#print('A raiz quadrada de {} vale {:.2f}'.format(n, r))

#Segunda maneira de fazer.
#n = int(input('Digite um número:'))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('O dobro de {} vale {}. \nO triplo de {} vale{}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, d, n, t, n, r))

#Terceira maneira de fazer.
#n = int(input('Digite um número:'))
#print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))

#Quarta maneira de fazer usando o POW que é potencia.
n = int(input('Digite um número:'))
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))









