# Crie um programa de adivinhação.

"""from random import randint
from time import  sleep # essa importação faz o código pensar antes de responder.
computador = randint(0, 5) # faz o pc pensar.
print('-' * 58)
print('Vou pensar em um número de 0 a 5. Agora tente adivinhar...')
print('-' * 58)
jogador = int(input('Em que número pensei?')) # jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! você acertou.')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}!'.format(computador, jogador))"""

from random import randint
rifa = randint(0,100)
print('*' * 40)
print('Bem vindo a rifa show de felicidade!')
print('*' * 40)
participante =int(input('Escolha seu número premiado.'))
if participante == rifa:
    print('Parabéns, você acabou de ganhar um PS5.')
else:
    print('Não foi dessa vez, número sorteado foi {} e não o {}.'.format(rifa, participante))

# Código para fazer rifas.
#from random import randint
#n = randint(0, 50)
#print('Computador escolheu o  número {}.'.format(n))
#print('Parabéns número {}'.format(n))