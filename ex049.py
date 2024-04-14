#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Ddigite um número para ver a tabuada: "))
for n in range(1, 11):
    print('{} x {:2} = \033[0:31m{}\033[m'.format(num, n, num*n))


