# Faça um programa que leia um númeor inteiro e diga se ele e primo ou não.

num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('\033[35mEle vai ser primo.\033[m')
else:
    print('\033[31mEle não vai ser primo.\033[m')
