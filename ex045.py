#Crie um programa que faça o computador jogar Jokenpô com você.

print("\033[1:35m{:#^50}\033[m".format(' Seja Bem Vindo ao JOKWNPÔ !'))
from random import  randint # import random: permite gerar números aleatórios. Função randint:Essa função permite gerar números inteiros aleatórios dentrovde um intervalo específico.
from time import sleep # Essa função permite suspender a execução do programa por um determinado período de tempo, especificado em segundos, você escolhe o segundo que algo irá acontecer.
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções :
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua escolha jogador?'))
print('\033[1;33mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;33mPÔ!\033[m')
sleep(1)
print('\033[1:35m-=\033[m' * 11)
print('Computador jogou {}'.format(itens[computador])) # Opção que o computador jogou.
print('Jogador jogou {}'.format(itens[jogador])) # Opção que o jogador jogou.
print('\033[1:35m-=\033[m' * 11)
if computador == 0: # computador jogou pedra.
    if jogador == 0:
        print('Empate.')
    elif jogador == 1:
        print('Jogador Venceu.')
    elif jogador == 2:
        print('Computador Venceu.')
    else:
        print('Jogada inválida.')
elif computador == 1: # computador jogou papel.
    if jogador == 0:
       print('Computador Venceu.')
    elif jogador == 1:
       print('Empate.')
    elif jogador == 2:
        print('Jogador Venceu.')
    else:
        print('Jogada inválida.')
elif computador == 2: # computador jogou tesoura.
    if jogador == 0:
        print('Jogador Venceu.')
    elif jogador == 1:
        print('Computador Venceu.')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida.')
