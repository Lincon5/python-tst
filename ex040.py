#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

nome = str(input('Digite seu nome:')).title()
n1 = float(input('Digite uma nota:'))
n2 = float(input('Digite uma nota:'))
m = (n1 + n2) / 2
print('OI {},sua nota foi {:.1f} e {:.1f}, e sua média foi {:.1f}'.format(nome,n1, n2, m))
if m < 5:
    print('Estude mais no proximo ano {}.\033[0;31mReprovado.'.format(nome))
elif m >=5 and m < 7:
    print('Te veremos na prova de recuperação {},\033[0;33mRecuperação.'.format(nome))
elif m >= 7:
    print('Parabéns {},\033[0;34mAprovado.'.format(nome))

# elif 7 > m >= 5: posso usar assim também na parte da recuperação.