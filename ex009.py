#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
#n = int(input('Digite um número para sua tabuada:'))
#t1 = n * 1
#t2 = n * 2
#t3 = n * 3
#t4 = n * 4
#5 = n * 5
#t6 = n * 6
#t7 = n * 7
#t8 = n * 8
#t9 = n * 9
#t10 = n * 10
#print('Resultado: \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} '.format(t1 ,t2, t3, t4, t5, t6, t7, t8, t9, t10))

#Maneira mas bonita de fazer.

n = int(input('Digite um número para sua tabuada:'))
print('-' * 13)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {} = {}'.format(n, 10, n*10))
print(('-' * 13))
print('Sua tabuada está pronta!')

