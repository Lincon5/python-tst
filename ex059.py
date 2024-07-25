#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar, [ 2 ] multiplicar,[ 3 ] maior, [ 4 ] novos números e [ 5 ] sair do programa.
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
         soma = n1 + n2
         print('A soma entre {} + {} é {}'.format(n1,n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} * {} é {}'.format(n1, n2, multiplicação))

    elif opção == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
            print('Informe os números novamente:')
            n1 = int(input('Primeiro número:'))
            n2 = int(input('Segundo  número:'))
    elif opção == 5:
            print('Finalizado.')
    else:
        print('Opção inválida, tente outro novamente. ')
    print('\033[35m==\033[m' *15)
print('\033[1:31mFim do programa! Volte sempre.\033[m ')
