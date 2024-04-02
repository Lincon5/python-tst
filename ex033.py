# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('*' *40)
a = int(input('Digite um número:'))
b = int(input('Digite mais um número:'))
c = int(input('Digite outro número:'))
# verificar quem é o menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificar quem é o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número foi o {}, maior foi {}.'.format(menor, maior))
print('*' *40)
